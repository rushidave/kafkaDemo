from kafka import KafkaProducer
import json
from data import get_registered_user
import time
from kafka.errors import KafkaError

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = ['0.0.0.0:9092'], value_serializer=json_serializer)


if __name__ == '__main__':
    count = 0
    while count < 10:
        try:
            registered_user = get_registered_user()
            print(registered_user)
            producer.send("t1", registered_user)
            time.sleep(0.1)
            count += 1
        except KafkaError as e:
            print("Encountered an error", e)