# selenium 이용
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# 기본 옵션
options = Options()
# 모바일 버전 user-agent.
user = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
options.add_argument(f'User-Agent={user}')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches",["enable-automation"]) 
driver = webdriver.Chrome(options=options)

# 크롤링 코드
url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(3)

# 이벤트 페이지 닫기
if driver.current_url != url:
    driver.get(url)

# 팝업 페이지 닫기
driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(0.2)

# 멜론 차트 보기
driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(0.4)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 더보기 버튼 클릭 (2번째 요소 선택 - 리스트 형이라 가능한 부분)
more_btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click() #.service_list_more.noline.sprite.hide

items = soup.select(".list_item")
num = 1
for i in items :
    singer = i.select_one(".name.ellipsis")
    title = i.select_one(".title.ellipsis")
    print('멜론차트 TOP100')
    print(f'<{num} 위>')
    print(f'가수 : {singer.text}')
    print(f'제목 : {title.text.strip()}')
    print()
    num += 1

driver.quit()