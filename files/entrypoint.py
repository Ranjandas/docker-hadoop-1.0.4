#!/usr/bin/env python

import os
import subprocess
import time


def format_hdfs():
    print "Formatting HDFS if not already formatted"

    HDFS_NAME_DIR="/tmp/hadoop-hdfs/dfs/name"

    if os.path.isfile(os.path.join(HDFS_NAME_DIR, "current/VERSION")):
	print "HDFS Already Formatted. Nothing to do."
    else:
        print "Formatting HDFS"
	subprocess.call(["su", "-", "hdfs", "-c", "hadoop namenode -format"])
    


def start_masters():
    format_hdfs()

    print "Starting master services"
    print "Starting Namenode"


    subprocess.call(["service", "hadoop-namenode", "start"])

    print "Starting Secondary Namenode"
    
    subprocess.call(["service", "hadoop-secondarynamenode", "start"])

    print "Creating and setting permission for /tmp"
    subprocess.call(["su", "-", "hdfs", "-c", "hadoop fs -mkdir /tmp"])
    subprocess.call(["su", "-", "hdfs", "-c", "hadoop fs -chmod 777 /tmp"])

    print "Starting Job Tracker"
    subprocess.call(["service", "hadoop-jobtracker", "start"])


def start_slaves():
    print "Starting Datanode"

    subprocess.call(["service", "hadoop-datanode", "start"])

    print "Starting Tasktracker"

    subprocess.call(["service", "hadoop-tasktracker", "start"])



if __name__ == "__main__":

    ROLE = os.getenv("ROLE")

    if ROLE == "master":
        print "Starting master services"
	start_masters()
    elif ROLE == "slave":
        print "Starting slave services"
        start_slaves()
    else:
        print "ROLE not found or incorrect."

    #subprocess.call(["tail", "-F", "/var/log/hadoop/*/*.log"], shell=True)
    os.system("tail -F /var/log/hadoop/*/*.log")
