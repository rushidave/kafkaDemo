# kafkaDemo

Prereq:
  1) Install Kafka
  2) Install Zookeeper

Install
  1) `pip install --user --requirement requirements.txt`
  2) Create Kafka Topic t1 using: `$ bin/kafka-topics.sh --create --topic t1 --bootstrap-server localhost:9092`
  3) Check if the topic is created using: `$ bin/kafka-topics.sh --bootstrap-server localhost:9092 --list`

To run:
  
  1) Edit server.properties file located inside `kafka_2.13-2.7.0/config`:
      - add line/uncomment -> `advertised.listeners=PLAINTEXT://localhost:9092`
      - add line/uncomment -> `zookeeper.connect=localhost:2181`
     
  2) To start zookeeper run the following command in terminal: `bin/zookeeper-server-start.sh config/zookeeper.properties`
 
  3) In new terminal, run the following command to start kafka: `JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties`

  4) Run `python3 producer.py`
  
  5) Run `python3 consumer.py`
 
#Comments 

I tried using Docker, however, docker results into messages not being sent to Kafka Topic. 
