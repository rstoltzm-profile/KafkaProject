# Project for getting Kafka container up and running

### Guide: Apache Kafka development setup example
https://hub.docker.com/r/bitnami/kafka

1. kafka cluster starts up - port 9092:9092, runs healthcheck
2. wait for kafka healthcheck
3. producer - generates random cosine data, sends to kafka topic "sensor_data"
4. consumer - consumes from "sensor_data" data and dumps into consumer_log.txt



```bash
# build
docker-compose build

# commands
docker-compose up
docker-compose down

# full rebuild
docker-compose down; docker-compose build; docker-compose up

# check containers
docker ps
docker exec -it <id> bash

# inside container
cd /opt/bitnami/kafka/bin
./kafka-topics.sh --bootstrap-server kafka:9092 --list
./kafka-topics.sh --bootstrap-server kafka:9092 --topic sensor_data --describe
./kafka-get-offsets.sh --bootstrap-server kafka:9092 --topic sensor_data

./kafka-consumer-groups.sh --bootstrap-server kafka:9092 --list
./kafka-consumer-groups.sh --bootstrap-server kafka:9092 --group my-group --describe
```