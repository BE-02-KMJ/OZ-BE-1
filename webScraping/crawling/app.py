from flask import Flask, render_template
import pymysql
import json

app = Flask(__name__)

db = pymysql.connect (
    host='localhost',
    user='root',
    password='alswjd6984!',
    db='kream',
    charset='utf8mb4'
)

cur = db.cursor()
sql = "SELECT * FROM kream_item"
cur.execute(sql)

kream_data = cur.fetchall()
kream_data = json.dumps(kream_data)

@app.route('/')
def index():
	return render_template('index.html', data_list = kream_data)

if __name__ == '__main__':
	app.debug = True
	app.run