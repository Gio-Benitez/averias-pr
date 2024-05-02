import psycopg2
from decouple import config

def get_connection():
    conn = psycopg2.connect(
        database=config('POSTGRES_DATABASE'),
        user=config('POSTGRES_USER'),
        password=config('POSTGRES_PASSWORD'),
        host=config('POSTGRES_HOST'),
        port="5432"
    )
    return conn
