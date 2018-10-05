
USERSTABLE = '''CREATE TABLE IF NOT EXISTS users
            (
                user_id serial PRIMARY KEY, 
                username VARCHAR (50) UNIQUE NOT NULL, 
                email VARCHAR (50) UNIQUE NOT NULL, 
                password VARCHAR (355) UNIQUE NOT NULL,
                userRole varchar(30) NOT NULL DEFAULT 'client',
                createddate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
        )''' 

ORDERSTABLE = '''CREATE TABLE IF NOT EXISTS orders
            (
                order_id serial PRIMARY KEY, 
                description VARCHAR (50) UNIQUE NOT NULL, 
                status VARCHAR (50) NOT NULL, 
                address VARCHAR (355) UNIQUE NOT NULL, 
                deliveryTime VARCHAR (400) UNIQUE NOT NULL
        )''' 

MEALSTABLE = '''CREATE TABLE IF NOT EXISTS meals
            (
                meal_id serial PRIMARY KEY, 
                mealcategory VARCHAR (100) UNIQUE NOT NULL
        )''' 

queries = [USERSTABLE, ORDERSTABLE, MEALSTABLE]
