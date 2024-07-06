from time import sleep
from json import dumps
from kafka import KafkaProducer
import math
import time
import random

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

start_time = time.time()

print("producer started")

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    sensor_value = math.cos(elapsed_time) + random.normalvariate(0, 0.1)  # cosine wave with some noise
    data = {'sensor_id': random.randint(1, 100), 'value': sensor_value}
    producer.send('sensor_data', value=data)
    print("Produced message: " + str(data), flush=True)
    sleep(1)
