import psycopg2
from psycopg2 import pool

def create_tables(config):

    """ create tables in the PostgreSQL database"""

    commands = (
        """
        CREATE TABLE book (
            upc INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(4000) NOT NULL,
            product_type VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            price_without_tax REAL,
            price_with_tax REAL,
            tax REAL,
            number_of_reviews INTEGER NOT NULL
        )
        """,
        """ 
        CREATE TABLE book_state (
            id SERIAL PRIMARY KEY,
            upc INTEGER NOT NULL,
            availability VARCHAR(100) NOT NULL,
            quantity INTEGER NOT NULL,
            CONSTRAINT fk_book
                FOREIGN KEY(upc)
                    REFERENCES book(upc)
        )
        """
    )

    DB_NAME = config.get('database').get('dbname')
    USER = config.get('database').get('user')
    HOST = config.get('database').get('host')
    PASSWORD = config.get('database').get('password')

    conn = None
    try:

        postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user=USER,
                                                         password=PASSWORD,
                                                         host=HOST,
                                                         port="5432",
                                                         database=DB_NAME)
        
        if (postgreSQL_pool):
            print("Connection pool created successfully")

        conn = postgreSQL_pool.getconn()
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.close()

        conn.commit()

        print('Tables created')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)