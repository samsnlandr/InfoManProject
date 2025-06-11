import mysql.connector

def dbconnect():
    return mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "pass",
    database = "bpi_draft_v6"
)