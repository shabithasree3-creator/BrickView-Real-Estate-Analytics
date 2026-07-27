import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sha10"
    )

    print("Connected successfully!")

except Exception as e:
    print(e)