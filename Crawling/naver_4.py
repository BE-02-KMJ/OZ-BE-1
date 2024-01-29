# BeautifulSoup (정적 크롤링) 복습
import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")


name = soup.select(".name")
title = soup.select(".title_area")
link = soup.select(".title_link._cross_trigger")
for i in zip(name, title, link) :
    print(f'출처: {i[0].text}')
    print(f'제목: {i[1].text}')
    print(f'링크: {i[2]['href']}')
    print()