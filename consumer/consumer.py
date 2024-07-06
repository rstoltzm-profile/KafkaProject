from kafka import KafkaConsumer
from json import loads
from time import sleep

try:
    consumer = KafkaConsumer(
        'sensor_data',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    while True:
        with open('consumer_log.txt', 'a') as f:
            for message in consumer:
                # Write the message value to the log file
                f.write(str(message.value) + '\\n')
                # Print the consumed message
                f.flush()
                print("Consumed message: " + str(message.value), flush=True)
        sleep(5)

except Exception as e:
    print(f"Error: {e}")