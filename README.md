# kafkaDemo

Prereq:
  1) Install Kafka
  2) Install Zookeeper


To run:
  1) change server.properties file to:
      add line/uncomment -> advertised.listeners=PLAINTEXT://localhost:9092
     
  2) bin/zookeeper-server-start.sh config/zookeeper.properties
 
  3) JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties  

  4) Run `python3 producer.py`
  
  5) Run `python3 consumer.py`
 
 

I tried using Docker, however, docker results into menssages not being sent to Kafka Topic. 
