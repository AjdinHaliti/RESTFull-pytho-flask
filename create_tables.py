import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

#vtm katu ka dallim te int dhe INTEGER (MUST BE INTEGER)
user_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, email text)"
cursor.execute(user_table)

car_table = "CREATE TABLE IF NOT EXISTS cars (name text PRIMARY KEY, price real, cartype text, engintype text)"
cursor.execute(car_table)

#test data
#cursor.execute("INSERT INTO cars VALUE ('bmw', '10000', 'coupe', 'Twin Turbo 3.0')")

connection.commit()

connection.close()

