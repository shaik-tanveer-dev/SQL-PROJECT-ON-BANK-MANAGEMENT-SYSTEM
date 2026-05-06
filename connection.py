
import mysql.connector as SQLC

# step 1
# database config
db_config = SQLC.connect(
    host = 'localhost',
    username = 'root',
    password = 'Tanveer@2004', # your mysql workbench password
    database = 'bank1'
)

# step 2 
# cursor object creation
cursor = db_config.cursor()

print(db_config)
print(cursor)
# step 3 
# execute method
cursor.execute("CREATE DATABASE BANK1;")
print(cursor)

query = "insert into accounts(account, name , amount) values(%s, %s, %s)"
cursor.execute(query,(101, "tanveer", 2000) )
db_config.commit()