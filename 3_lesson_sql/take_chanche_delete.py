import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port="3306",
    user='root',
    password="",
    database="python-example"
)

myCyr = mydb.cursor()

# sql = "SELECT id,date FROM articles"
# sql = "SELECT * FROM articles WHERE title  <> 'Первая статья'"
# sql = "SELECT * FROM articles WHERE title  LIKE '%статья%'"
# sql = "SELECT * FROM articles WHERE title NOT LIKE  '%Вторая%' AND id > 2"
# sql = "SELECT * FROM articles WHERE title NOT LIKE  '%Вторая%' OR id > 2"
# sql = "SELECT * FROM articles WHERE title NOT LIKE  '%s' OR id < %s"
# sql = "SELECT * FROM articles WHERE title NOT LIKE  '%s' OR id < %s ORDER BY  id ASK"
# sql = "SELECT * FROM articles WHERE title NOT LIKE  '%s' OR id < %s ORDER BY  id DESC"
# sql = "SELECT id, data FROM articles LIMIT 2"
# sql = "SELECT id, data FROM articles LIMIT 2 OFFSET 2 "  # пропустить первые 2 записи и вывести 2 записи
# myCyr.execute(sql, (4, 3))

# res = myCyr.fetchone()
# res = myCyr.fetchall()

# print(res)

# for element in res:
#    print(element)

# myCyr.execute(sql)f

# --------------------------------------------------------------------------------------------------------
# Обновить данные в SQL

# sql = "UPDATE articles SET title = %s WHERE id = %s"
# myCyr.execute(sql, ('updated_text', 3))
# mydb.commit()
# ----------------------------------------------------------------------------------------------------------
# Удаление данных
# sql = "DELETE from articles WHERE title = %s" # удалить что-то по такому-то параметру
# sql = "DELETE from articles" # удалить все из
# myCyr.execute(sql, ("Первая статья", ))
sql = "DROP TABLE articles"  # удалить таблицу
myCyr.execute(sql)
mydb.commit()
