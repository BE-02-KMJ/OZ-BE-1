# selenium 이용
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib.request

# 기본 옵션
options = Options()
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f'User-Agent={user}')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches",["enable-automation"]) 
driver = webdriver.Chrome(options=options)

# 크롤링 코드
url = "https://kream.co.kr/"
driver.get(url)

# 다양한 기능 넣어주기
# 1. 돋보기 누르기
driver.find_element(By.CSS_SELECTOR, ".btn_search").click() 
time.sleep(0.5) # 인간미 넣어주기 (트래픽감지 방지)

# 2. 브랜드 검색 * 추후 여러개 브랜드 넣을 예정
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림") # 브랜드명 입력
time.sleep(0.3)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)   # enter 실행
# enter를 입력해도 좋지만 \n로 브랜드명에 같이 넣어줘도 작동함.
time.sleep(0.1)

# 3. 스크롤 계속 내려서 정보 가져오기_키보드 키 이용, 반복 작업(for문)
for i in range(10): # 20번 반복
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)  # 키보드 키 이용해서 스크롤
    time.sleep(0.5)

# 4. 각 상품 정보 가져오기
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card")
num = 1
for i in items :
    product_name = i.select_one(".translated_name")
    brand = i.select_one(".product_info_brand.brand")
    product_price = i.select_one(".amount")
    deal = i.select_one(".status_value")
    star = i.select_one(".wish_figure")
    review = i.select_one(".review_figure")
    if "후드" in product_name.text :
        print(f'<{num}>')
        print(f'브랜드 : {brand.text}')
        print(f'제품명 : {product_name.text}')
        print(f'가격 : {product_price.text}')
        print(f'{deal.text}')
        print(f'위시량 : {star.text}')
        print(f'리뷰 : {review.text}')
        print()
        num += 1
    
    # 5. 상품 사진 저장하기
    images = driver.find_element(By.CSS_SELECTOR,".image.full_width").get_attribute("src")
    urllib.request.urlretrieve(images, "img.png")

driver.quit()