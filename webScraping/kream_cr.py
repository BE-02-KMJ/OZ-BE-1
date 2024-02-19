from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlopen
import time

# 기본 옵션
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options = Options()
options.add_argument(f'User-Agent={user}')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches",["enable-automation"])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

# 크롤링 코드 - 최신 상품들
url = "https://kream.co.kr/exhibitions/2082"
driver.get(url)
time.sleep(0.5)

# 스크롤 내려서 정보 가져오기
for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)  # 키보드 키 이용해서 스크롤
    driver.implicitly_wait(1)
    time.sleep(0.5)

# 각 상품 정보 가져오기
# 이름, 브랜드, 가격, 즐겨찾기, 리뷰, 이미지
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card.exhibition_product")
item_list = []
num = 1

for i in items :
    product_name = i.select_one(".product_info_product_name > .name").text
    brand = i.select_one(".product_info_brand.brand").text
    product_price = i.select_one(".amount").text
    img_src = i.select_one(".picture.product_img").img['src']
    if not img_src.startswith('http'):  # img_src가 'http'로 시작하지 않으면
        img_src = url + img_src  # 루트 URL을 추가합니다.
    # try:
    #     with urlopen(img_src) as respond:
    #         with open('C:/Users/PC/Desktop/OZ-BE/webScraping/img/'+str(num)+'.jpg', 'wb') as f:
    #             img = respond.read()
    #             f.write(img)
    #     print(f'{num} OK')
    # except Exception as e:
    #     print(f"Error occurred with URL {img_src}: {e}")
    # num += 1

    item = [img_src, brand, product_name, product_price]
    item_list.append(item)

driver.quit()

# pymysql로 MySQL 데이터 베이스에 연결
import pymysql
import re
from datetime import datetime

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='alswjd6984!',
    db='kream',
    charset='utf8mb4'
)

connection.cursor()

# 데이터 베이스에 데이터 삽입
def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()

for i in item_list :
    execute_query(connection, "INSERT INTO kream_item (img, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0],i[1],i[2],i[3]))