import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user='root',
    password="",
    database='userDB'
)

print(mydb)

myCur = mydb.cursor()

# sql = "CREATE DATABASE `exampleDB`"
# sql = "DROP DATABASE `usersDB`"
# sql = "CREATE DATABASE `userDB`"
# sql = "CREATE TABLE Users (userID INT)"
# sql = "CREATE TABLE Products (id INT NOT NULL),(price INT NIT NULL),(intro VARCHAR(255)),(text TEXT),(foto VARCHAR(100)),(PRIMARY KEY (id)) "
# sql = "CREATE TABLE Product (id INT NOT NULL, price INT NOT NULL)"
# sql = "ALTER TABLE `Product` ADD `price` INT(255) NOT NULL AFTER `price`; "
# sql = "ALTER TABLE `Product` ADD `intro` VARCHAR(255) AFTER `price`; "
# sql = "ALTER TABLE `Product` ADD `text` TEXT AFTER `intro`; "
# sql = "ALTER TABLE `Product` ADD `foto` VARCHAR(100) AFTER `text`; "
# sql = "ALTER TABLE `Product` ADD PRIMARY KEY (`id`);"
# sql = "TRUNCATE TABLE Product"
# sql = "DROP TABLE Product"
# sql = "SELECT * FROM Users"

sql = ""

# myCur.execute(sql)
# myCur.executemany(sql, users)
# mydb.commit()
