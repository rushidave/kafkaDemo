from psycopg2.extras import RealDictCursor
import psycopg2


uri = "postgres://avnadmin:y7n6ux2p3ut6hbg7@pg-ff8016c-rushijdave96-69df.aivencloud.com:15480/defaultdb?sslmode=require"

db_conn = psycopg2.connect(uri)
c = db_conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS kafka2( 
        name VARCHAR (255) NOT NULL
        )""")

db_conn.commit()
c.close()
db_conn.close()