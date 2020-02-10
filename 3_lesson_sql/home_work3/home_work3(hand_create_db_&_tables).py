import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    port='3306',
    user='root',
    password='',
    database="itprogerDB"
)
print(myDB)

myCur = myDB.cursor()

# sql = "CREATE DATABASE `itprogerDB`"

# ----------------Создание таблиц----------------
# sql = "CREATE TABLE items (id INT, title VARCHAR(255), price INT, category VARCHAR(100))"
# sql = "ALTER TABLE `items` ADD PRIMARY KEY (`id`)"
# sql = "CREATE TABLE users (id INT, login VARCHAR(100), pass VARCHAR(100))"
# sql = "ALTER TABLE `users` ADD PRIMARY KEY (`id`)"
# myCur.execute(sql)
# ----------------Ввод данных----------------
sql_users = "INSERT INTO `users` (id, login, pass) VALUES (%s, %s, %s)"
users = [
    ("1", "john", "some_pass"),
    ("2", "alex", "some_pass")
]
myCur.executemany(sql_users, users)
sql_items = "INSERT INTO `items` (id, title, price, category) VALUES (%s, %s, %s, %s)"
items = [
    ("1", "Кружка мужская", "300", "cups"),
    ("2", "Кепка красная", "150", "hats"),
    ("3", "Кепка синяя", "200", "hats"),
    ("4", "Кружка женская", "400", "cups"),
    ("5", "Красная футболка", "550", "shirts"),
    ("6", "Футболка 'Рик и Морти'", "700", "shirts")
]
myCur.executemany(sql_items, items)
myDB.commit()
# ----------------Выбор данных---------------------------
sql_select_user = "SELECT * FROM users WHERE login = 'john'"
myCur.execute(sql_select_user)
result_users = myCur.fetchall()
for user in result_users:
    print(user)

sql_select_items = "SELECT * FROM items WHERE category = 'hats'"
myCur.execute(sql_select_items)
result_items = myCur.fetchall()
for item in result_items:
    print(item)

# ----------------Создание таблицы orders----------------
sql = "CREATE TABLE `orders` (id INT, user_id INT, item_id INT)"
sql_key = "ALTER TABLE `orders` ADD PRIMARY KEY (`id`) "
myCur.execute(sql)
myCur.execute(sql_key)
sql_values = "INSERT INTO `orders` (user_id, item_id ) VALUES (%s, %s)"
values = [
    ("1", "1"),
    ("1", "2"),
    ("1", "3"),
    ("2", "3")
]
myCur.executemany(sql_values, values)
myDB.commit()

sql = "SELECT `login`, `title` FROM `users`,`items`, `orders` WHERE `users`.`id` = `orders`.`user_id` AND " \
      "`items`.`id` = `orders`.`item_id` "
myCur.execute(sql)
res = myCur.fetchall()
print("Все заказы: ")
for name, order in res:
    print(name, " - ", order)
