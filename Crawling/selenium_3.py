from selenium import webdriver
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url

driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)

# 스크롤 코드 (거의 외운다고 생각하면 된다.)
# driver.execute_script("window.scrollTo(0,4000)")
# time.sleep(1)

# 스크롤 끝까지 내리기
for i in range(5) : #대략 4,5번 스크롤을 내려야 맨 끝까지 내릴 수 있다.
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

view = soup.select(".view_wrap")
num = 1
for i in view:
    ad = i.select_one(".link_ad")
    if ad :
        continue
    else :
        title = i.select_one(".title_link._cross_trigger")
        name = i.select_one(".name")
        print(num)
        print(f'제목 : {title.text}')
        print(f'작성자 : {name.text}')
        print(f'링크 : {title['href']}')
        print()
        num += 1

driver.quit()