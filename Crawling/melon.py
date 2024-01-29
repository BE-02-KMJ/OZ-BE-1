import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

charts1 = soup.select(".lst50")
charts2 = soup.select(".lst100")
chart = charts1 + charts2
# 위 세줄 코딩을 chart = soup.find_all(class_=["lst50", "lst100"]로 대체 가능.)

year = soup.select_one(".year").text
hour = soup.select_one(".hour").text

print()
print(f'{year} {hour} 멜론 TOP100')
print()

for i in chart: # for i in enumerate(chart, 1)로 수정 가능.
    rank = i.select_one(".rank")
    title = i.select_one(".ellipsis.rank01 > span > a") #.ellipsis.rank01 a로 적어도 된다.
    name = i.select_one(".checkEllipsis > a")
    album = i.select_one(".ellipsis.rank03 > a")
    print(f'<{rank.text} 위>\n제목 : {title.text}\n가수 : {name.text}\n앨범 : {album.text}')
    print()

# 1이랑 l이랑 구분하기, class 구분 .으로 하기★