import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://naver.com"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# 문법 1) find : select_one과 비슷하다.
soup.find(class_="link_service", text="쇼핑") # class_ (언더바) 주의! ★
soup.find(id="link_service")
# 동적 크롤링시 정확한 위치 지정해줄 필요 있다.

# 문법 2) find_all : select와 비슷하다.
soup.find_all