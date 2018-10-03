import os
import psycopg2


from .db import queries

def dbconnect():
    """connect to db"""
    url = os.getenv('DATABASE_URL')
    # print(url)
    return psycopg2.connect(url)


def initializedb():
    try:
        connection = dbconnect()
        connection.autocommit = True

        #activating the cursor
        cursor = connection.cursor()

        for query in queries:
            cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error")
        print(error)
