from kafka import KafkaConsumer
import json
import helper
from psycopg2.extras import RealDictCursor
import psycopg2


def getConsumer():



    uri = "postgres://avnadmin:y7n6ux2p3ut6hbg7@pg-ff8016c-rushijdave96-69df.aivencloud.com:15480/defaultdb?sslmode=require"

    db_conn = psycopg2.connect(uri)
    c = db_conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS kafkademo1( 
            name VARCHAR (255) NOT NULL
            )""")

    db_conn.commit()

    consumer = KafkaConsumer(
        "t1",
        bootstrap_servers=["0.0.0.0:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="test-1"
    )

    
    test = ""
    print('Starting the Consumer')
    for msg in consumer:
        # print(msg.value)
        test = json.loads(msg.value)
        # print(test['name'])
        query = """INSERT INTO kafkademo1 (name) VALUES (%s) """
        val = [f"{test['name']}"]
        c.execute(query, val)
        db_conn.commit()

    c.close()
    db_conn.close()

if __name__ == '__main__':
    
    getConsumer()
    