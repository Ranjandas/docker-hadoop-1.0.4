FROM centos:6

MAINTAINER Ranjandas A P <thejranjan@gmail.com>


ENV JDK_VERSION 1.6.0

ENV TINI_VERSION v0.10.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--", "/entrypoint.py"]

RUN yum install -y https://archive.apache.org/dist/hadoop/core/hadoop-1.0.4/hadoop-1.0.4-1.x86_64.rpm && \
	yum install -y java-${JDK_VERSION}-openjdk-devel && \
	yum clean all

ADD files/entrypoint.py /
RUN chmod +x /entrypoint.py
