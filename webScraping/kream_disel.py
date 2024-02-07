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
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options = Options()
options.add_argument(f'User-Agent={user}')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches",["enable-automation"])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

# 크롤링 코드 - 최신 상품들
url = "https://kream.co.kr"
driver.get(url)
time.sleep(0.5)

# 1. 돋보기 누르기
driver.find_element(By.CSS_SELECTOR, ".btn_search").click() 
time.sleep(0.5) # 인간미 넣어주기 (트래픽감지 방지)

# 2. 브랜드 검색 - 디젤
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("디젤") # 브랜드명 입력
time.sleep(0.3)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)   # enter 실행
# enter를 입력해도 좋지만 \n로 브랜드명에 같이 넣어줘도 작동함.
time.sleep(0.1)