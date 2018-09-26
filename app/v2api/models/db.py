import psycopg2
def connect():
    c = psycopg2.connect (dbname='fastfoodfastdb', user='postgres', host='localhost', password='awiti')
    return c 
conn = connect()
print(conn)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
            (user_id serial PRIMARY KEY, 
            username VARCHAR (50) UNIQUE NOT NULL, 
            password VARCHAR (50) NOT NULL, 
            email VARCHAR (355) UNIQUE NOT NULL);''' 
            )
conn.commit()
cur.close()


cur = connect()
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS orders
            (order_id serial PRIMARY KEY, 
            description VARCHAR (50) UNIQUE NOT NULL, 
            status VARCHAR (50) NOT NULL, 
            address VARCHAR (355) UNIQUE NOT NULL, 
            deliveryTime VARCHAR (400) UNIQUE NOT NULL);''' 
            )
conn.commit()
cur.close()

cur = connect()
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS meals
            (meal_id serial PRIMARY KEY, 
            mealcategory VARCHAR (100) UNIQUE NOT NULL);''' 
            )
conn.commit()
cur.close()
conn.close()
