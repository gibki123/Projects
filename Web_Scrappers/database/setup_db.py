import psycopg2
import configparser
import os


def connect():
    db_config = configparser.ConfigParser()
    db_config.read('./database/db.ini')
    print(os.getcwd())
    return psycopg2.connect(
        database=db_config['postgresql']['db'],
        user=db_config['postgresql']['user'],
        password=db_config['postgresql']['passwd'],
        host=db_config['postgresql']['host'],
        port=db_config['postgresql']['port'],
        connect_timeout=db_config['postgresql'].getint(
            'conn_timeout')
    )


def disconnect(conn):
    if (conn):
        conn.close()


def verify_connection(cursor):
    cursor.execute("select version()")
    data = cursor.fetchone()
    print("Connection established to: ", data)


def list_all_public_tables(cursor):
    cursor.execute(
        "SELECT * FROM information_schema.tables WHERE table_schema='public';")
    tables = cursor.fetchall()
    print("------Public tables------")
    for table in tables:
        print(table)
    print("-------------------------")


def create_table(cursor):
    cursor.execute(""" CREATE TABLE IF NOT EXISTS news_data_table (
    id SERIAL PRIMARY KEY,
    asset_name VARCHAR(10) NOT NULL,
    headline TEXT NOT NULL,
    news_text TEXT NOT NULL,
    authors VARCHAR(100)[] NOT NULL,
    source_url TEXT NOT NULL,
    source_name VARCHAR(50) NOT NULL,
    date_and_time TIMESTAMP NOT NULL,
    per_source_id SERIAL NOT NULL,
    is_by_relavance BOOLEAN NOT NULL, 
    category VARCHAR(50) NOT NULL,
    subheadline VARCHAR(400) NOT NULL,
    no_comments INTEGER NOT NULL,
    no_views INTEGER NOT NULL
    );
    """)


def drop_table(cursor, table_name):
    cursor.execute(f""" DROP TABLE IF EXISTS {table_name} CASCADE""")

def main():
    try:
        conn = None
        conn = connect()
        cursor = conn.cursor()

        verify_connection(cursor)
        list_all_public_tables(cursor)
        create_table(cursor)
        # drop_table(cursor, 'news_data_table')
        list_all_public_tables(cursor)

        conn.commit()

    except psycopg2.DatabaseError as e:
        print(f"Database error {e}")
        exit(1)

    finally:
        disconnect(conn)


if __name__ == "__main__":
    main()
