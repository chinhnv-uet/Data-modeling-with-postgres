import psycopg2
from sqlQuery import create_table_queries
from sqlQuery import drop_table_queries

def establishConnection(connectInfo):
    conn = psycopg2.connect(**connectInfo)
    cursor = conn.cursor()
    print("Connect to postgres successfully")
    return conn, cursor

def dropTable(conn, cursor):
    for dropTabQuery in drop_table_queries:
        cursor.execute(dropTabQuery)
    conn.commit()
    print("Drop table successfully")
    
def createTable(conn, cursor):
    for createTabQuery in create_table_queries:
        cursor.execute(createTabQuery)
    conn.commit()
    print("Create table successfully")


def execute():
    connectInfo = {
        "host": "localhost",
        "port": "5432",
        "dbname": "chinhnv",
        "user": "chinhnv",
        "password": "123456"
    }
    conn, cursor = establishConnection(connectInfo)
    dropTable(conn, cursor)
    createTable(conn, cursor)
    