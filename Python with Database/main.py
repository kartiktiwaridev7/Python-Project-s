import mysql.connector

def get_connection ():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "kartik9276",
        database = "first"
    )

    return conn