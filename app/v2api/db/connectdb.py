import os
import psycopg2

#importing the tables in form of queries
from .db import queries

def dbconnect():
    """connect to db"""
    url = os.getenv('DATABASE_URL')
    return psycopg2.connect(url)


def initializedb():
    try:
        connection = dbconnect()
        connection.autocommit = True

        #activating the cursor
        cursor = connection.cursor()

        for query in queries:
            cursor.execute(query)
        # makes changes permanent on the database
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error", error)
    
