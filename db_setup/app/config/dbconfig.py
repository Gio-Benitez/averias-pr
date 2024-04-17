import psycopg2


def get_connection():
    conn = psycopg2.connect(
        database="averiaspr_db",
        user="root",
        password="password",
        host="averiaspr_db",
        port="5432"
    )
    return conn
