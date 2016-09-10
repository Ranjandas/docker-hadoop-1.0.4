# docker-hadoop-1.0.4

To run docker 1.0.4 on hadoop follow the below steps.

* Clone the repo
  
  ```
  git clone https://github.com/Ranjandas/docker-hadoop-1.0.4.git
  ```

* Use `docker-compose` to bring up the cluster and watch the logs.
 
  ```
  docker-compose up -d && docker-compose logs -f
  ```

* If using boot2docker use the boot2docker IP to access the web interfaces

  ```
  Namenode Web UI : http://<boot2docker ip>:50070
  Jobtracker Web UI : http://<boot2docker ip>:50030
  ```

* If running on on a Linux system where containers are directly accessible

  Get the master container IP as shown

  ```
  docker exec -it master.example.com ifconfig
  ```

  Access web interfaces


  ```
  Namenode Web UI : http://<master container ip>:50070
  Jobtracker Web UI : http://<master container ip>:50030
  ```
