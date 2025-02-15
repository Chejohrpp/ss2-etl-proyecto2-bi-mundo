import psycopg2
from db.config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def default_conn():
    config = load_config()
    connect(config)

if __name__ == '__main__':
    config = load_config()
    connect(config)