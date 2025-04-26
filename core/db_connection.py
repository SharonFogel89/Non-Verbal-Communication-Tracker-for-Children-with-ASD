import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="nonverbal_db",
            user="postgres",
            password="P0st2o25",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error to connect to the database:", e)
        raise
