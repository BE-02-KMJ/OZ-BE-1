import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# 관련 뉴스 제목과 링크 가져오기
# titles = soup.select(".news_tit")

# for i in titles:
#     print(i.text)   # 뉴스 제목
#     print(i['href'])    # 뉴스 링크

#     print()

keyword_box = soup.select(".keyword_box_wrap.type_color") # 클래스가 여러개인 경우 클래스별로 .으로 구별해줘야함.
for i in keyword_box :
    name = i.select_one(".name.elss").text
    category = i.select_one(".etc_area").text
    title = i.select_one(".title_link._cross_trigger._foryou_trigger").text
    print(f'블로그 작성자는 : {name}')
    print(f'분야 : {category}')
    print(f'제목 : {title}')
    print()
