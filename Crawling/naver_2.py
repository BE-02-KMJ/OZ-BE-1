import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

# 컴퓨터가 아닌 사람이 접속한 것처럼 보이게 하기 위해서 user 정보 입력해서 그것으로 접속하기.
header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
req = requests.get(url, headers=header_user)

# print(dir(req)) : 여러 기능 확인.
# print(req.raise_for_status) : 기능 check 1
# print(req.headers) : 기능 check 2
# print(req.request) : 기능 check 3