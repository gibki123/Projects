import psycopg2
import configparser


def main():
    config = configparser.ConfigParser()
    config.read('db.ini')

    conn = psycopg2.connect(
        database=config['postgresql']['db'],
        user=config['postgresql']['user'],
        password=config['postgresql']['passwd'],
        host=config['postgresql']['host'],
        port=config['postgresql']['port'],
        connect_timeout=config['postgresql'].getint('conn_timeout')
    )

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Executing an MYSQL function using the execute() method
    cursor.execute("select version()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Connection established to: ", data)

    # Closing the connection
    conn.close()


if __name__ == "__main__":
    main()
