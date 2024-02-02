import pymysql

# DB connection : 데이터 베이스 연결 설정하기
connection = pymysql.connect(host='localhost',
    user='root',
    password='alswjd6984!',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

# 1. 데이터 조회(SELECT)
def get_customers():
    cursor = connection.cursor()
    sql = 'SELECT * FROM customers'
    cursor.execute(sql)
    # fetchone : 모든 customers 테이블 데이터 가져오기.
    # fetchone : 하나만 가져오기
    customers = cursor.fetchone()   
    print('customers : ', customers)
    print('Number : ', customers['customerNumber'])
    print('Name : ', customers['customerName'])
    print('Country : ', customers['country'])
    print('City : ', customers['city'])
    cursor.close()

# get_customers()

# 2. 데이터 삽입 (INSERT)
def add_customer() :
    cursor = connection.cursor()
    name = 'Minjung'
    country = 'South Korea'
    city = 'Seoul'
    sql = f"INSERT INTO customers(customerNumber, customerName, country, city) VALUES (500, '{name}', '{country}', '{city}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# add_customer()

# 3. 데이터 수정 (UPDATE)
def update_customer() :
    cursor = connection.cursor()
    name = 'MJ'
    lastName = 'Salazar'
    firstName = 'Rosa'
    sql = f"UPDATE customers SET customerName='{name}', contactLastName='{lastName}', contactFirstName='{firstName}' WHERE customerNumber=500"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# update_customer()

# 4. 데이터 삭제 (DELETE)
def delete_customer() :
    cursor = connection.cursor()
    sql = 'DELETE FROM customers WHERE customerNumber = 500'
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# delete_customer()