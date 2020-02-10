import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port='3306',
    user='root',
    password='',
    database='python-example'
)
print(mydb)

myCur = mydb.cursor()

# sql = "CREATE DATABASE `python-example`"
# sql = "SHOW TABLES"f

# sql = "CREATE TABLE users (name VARCHAR(255), age INTEGER(3))"

# myCur.execute(sql)

# for element in myCur:
#     print(element)

