import psycopg2

def connection_db():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="db_recu",
        user="admin",
        password="admin"
    )
    return conn
