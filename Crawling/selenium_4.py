# selenium의 여러 옵션
# selenium은 JavaScript와 기능적으로 매우 비슷하기 때문에
# 여기서 사용하는 것은 JS에서도 사용 가능하다고 볼 수 있다.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options   # selenium option 불러오기
from bs4 import BeautifulSoup

options = Options()

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# 1. 화면 자동 종료 해제 옵션
# : 보통 time을 사용하여 몇초만 뜨고 꺼지기 때문에 항상 보기 위한 옵션이다.
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches",["enable-automation"])    # 시크릿 모드

# 2. 화면 크기 설정 
# : 요즘 반응형 웹이 많은데
# 이 경우 페이지의 크기가 어느정도 작아지면 모바일 버전으로 바뀌는 경우가 있기 때문에
# 화면 크기를 설정하고 해당 요소들을 가져오도록 하는 것이 안전하다.
options.add_argument("--start--maximized")
# options.add_argument("--start-fullscreen")    # 전체화면
# options.add_argument("window-size=300, 300")

# 3. 브라우저 화면이 나오지 않은 상태에서 크롤링 하게 만들어주는 옵션
# options.add_argument("--headless")

# 4. 음소거 옵션
options.add_argument("--mute-audio")

# 5. 시크릿 모드
options.add_argument("incognito")

# 6. 유저 정보 넣기
options.add_argument(f'User-Agent={user}')  # 이게 안 먹힐 경우 f-string 없애고
# 1) options.add_argument('User-Agent='+ user)
# 2) options.add_argument('user-agent='+ user) 사용

url = "https://naver.com"
driver = webdriver.Chrome(options=options)
driver.get(url)

driver.quit()