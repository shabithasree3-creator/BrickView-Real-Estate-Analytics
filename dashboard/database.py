import mysql.connector
import pandas as pd
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sha10",
        database="brickview"
    )
    return conn
def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df