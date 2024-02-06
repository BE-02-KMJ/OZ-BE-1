import pymysql

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='alswjd6984!',  # 데이터베이스 비밀번호
    db='testdatabase')       # 데이터베이스 이름

# # 목록 조회 (READ)
# try:
#     with connection.cursor() as cursor:
#         # 앨범 목록 조회
#         query = "SELECT 앨범, 연도 FROM albums;"
#         cursor.execute(query)
#         # 결과 출력
#         for row in cursor.fetchall():
#             print(row)
# finally:
#     connection.close()

# # 새 앨범 추가 (CREATE)
# try:
#     with connection.cursor() as cursor:
#         # 새 앨범 추가
#         query = "INSERT INTO albums (앨범, 연도, 최고순위) VALUES ('New Album', '2024', '1');"
#         cursor.execute(query)
#         connection.commit()
# finally:
#     connection.close()

# # 앨범 정보 업데이트 (UPDATE)
# try:
#     with connection.cursor() as cursor:
#         # 앨범 정보 업데이트
#         query = "UPDATE albums SET 최고순위 = '2' WHERE 앨범 = 'New Album';"
#         cursor.execute(query)
#         connection.commit()
# finally:
#     connection.close()

# 특정 앨범 삭제 (DELETE)
try:
    with connection.cursor() as cursor:
        # 특정 앨범 삭제
        query = "DELETE FROM albums WHERE 앨범 = 'New Album';"
        cursor.execute(query)
        connection.commit()
finally:
    connection.close()