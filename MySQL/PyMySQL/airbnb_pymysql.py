import pymysql

# 데이터 베이스 연결
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='alswjd6984!',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor :
    # 문제 1 - 새로운 제품 추가
    sql = "INSERT INTO products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
    cursor.execute(sql,('Python Book', 29.99, 10))
    connection.commit()
    # 문제 1 확인
    cursor.execute("SELECT * FROM products")
    for book in cursor.fetchall() :
        print(book)

    # 문제 2 - 고객 목록 조회
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)

    # 문제 3 - 제품 재고 업데이트
    sql = "UPDATE products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    cursor.execute(sql, (1, 1))
    connection.commit()

    # 문제 4 - 고객별 총 주문 금액 계산
    sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM orders GROUP BY customerID"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

    # 문제 5 - 고객 이메일 업데이트
    sql = "UPDATE customers SET email = %s WHERE customerID = %s"
    cursor.execute(sql, ('update@email.com', 1))
    connection.commit()

    # 문제 6 - 주문 취소
    sql = "DELETE FROM orders WHERE orderID = %s"
    cursor.execute(sql, (15))
    connection.commit()

    # 문제 7 - 특정 제품 검색
    sql = "SELECT * FROM products WHERE productName LIKE %s"
    cursor.execute(sql, ('%Book%'))
    data = cursor.fetchall()
    for row in data :
        print(row)

    # 문제 8 - 특정 고객의 모든 주문 조회
    sql = "SELECT * FROM orders WHERE customerID = %s"
    cursor.execute(sql, (1))
    data = cursor.fetchall()
    for row in data :
        print(row)

    # 문제 9 - 가장 많이 주문한 고객 찾기
    sql = """
    SELECT customerID, COUNT(*) AS orderCount 
    FROM orders 
    GROUP BY customerID 
    ORDER BY orderCount DESC 
    LIMIT 1
    """
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)

cursor.close()