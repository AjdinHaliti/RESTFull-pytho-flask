import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text , password text, email text)"
cursor.execute(create_table)

user = (1, 'Ajdin', 'password', 'ah27098@seeu.edu.mk')
insert_query = "INSERT INTO users VALUES (?, ?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'Ajdinn', 'passsword', 'ahh27098@seeu.edu.mk'),
    (3, 'Ajdi', 'passwor', 'ah27098@seeu.edu.mka' )
]

cursor.executemany(insert_query, users)

select_query = "SELECT email FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()