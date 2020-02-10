import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="mydb"
)

print(mydb)

myCur = mydb.cursor()

# Выбор пользователя
sql_select_user = "SELECT * FROM users WHERE login = 'john'"
myCur.execute(sql_select_user)
result_users = myCur.fetchall()
for user in result_users:
    print(user)

# Выбор товара
sql_select_items = "SELECT * FROM items WHERE category = 'hats'"
myCur.execute(sql_select_items)
result_items = myCur.fetchall()
for item in result_items:
    print(item)

# sql_create = "CREATE TABLE `orders` ( `id` INT NOT NULL AUTO_INCREMENT , `user_id` INT, `item_id` INT, PRIMARY KEY (`id`)) ENGINE = MyISAM;"
# myCur.execute(sql_create)

# Ввод данных в таблицу Order
sql_values = "INSERT INTO `orders` (user_id, item_id ) VALUES (%s, %s)"
values = [
    ("1", "1"),
    ("1", "2"),
    ("1", "3"),
    ("2", "3")
]
myCur.executemany(sql_values, values)
mydb.commit()


# Выбор данных на основе таблицы Orders
sql = "SELECT `login`, `title` FROM `users`,`items`, `orders` WHERE `users`.`id` = `orders`.`user_id` AND " \
      "`items`.`id` = `orders`.`item_id` "
myCur.execute(sql)
res = myCur.fetchall()
print("Все заказы: ")
for name, order in res:
    print(name, " - ", order)
