import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='python-example'
)

myCur = mydb.cursor()

sql = 'INSERT INTO articles (title, intro, data) VALUES (%s, %s, %s)'
articles = [
    (
        "Первая статья",
        "Hello text",
        "2020-12-12"
    ),
    (
        "Вторая статья",
        "Hello text",
        "2020-08-09"
    ),
    (
        "Третья статья",
        "Hello text",
        "2020-09-09"
    ),
    (
        "Чевертая статья",
        "Hello text",
        "2020-06-06"
    )
]

myCur.executemany(sql, articles)
mydb.commit()
