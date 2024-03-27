import pymysql.cursors

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="alswjd6984!",
    database="oz_flask",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
