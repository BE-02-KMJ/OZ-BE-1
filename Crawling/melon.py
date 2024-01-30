import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# 실시간 멜론 TOP 100
url_live = "https://www.melon.com/chart/index.htm"
req_live = requests.get(url_live, headers=header_user)

html_live = req_live.text
soup_live = BeautifulSoup(html_live, "html.parser")

charts1 = soup_live.select(".lst50")
charts2 = soup_live.select(".lst100")
chart = charts1 + charts2
# 위 세줄 코딩을 chart = soup.find_all(class_=["lst50", "lst100"]로 대체 가능.)

year = soup_live.select_one(".year").text
hour = soup_live.select_one(".hour").text

print()
print(f'{year} {hour} 멜론 TOP100')
print()

for i in chart: # for i in enumerate(chart, 1)로 수정 가능.
    rank = i.select_one(".rank")
    title = i.select_one(".ellipsis.rank01 > span > a") #.ellipsis.rank01 a로 적어도 된다.
    name = i.select_one(".checkEllipsis > a")
    album = i.select_one(".ellipsis.rank03 > a")
    change = i.select_one(".rank_wrap")
    print(f'<{rank.text} 위>\n제목 : {title.text}\n가수 : {name.text}\n앨범 : {album.text}')
    print(f'변동 : {change['title']}')
    print()

# 1이랑 l이랑 구분하기, class 구분 .으로 하기★


# 주간 멜론 TOP100
url_week = "https://www.melon.com/chart/week/index.htm"
req_week = requests.get(url_week, headers=header_user)

html_week = req_week.text
soup_week = BeautifulSoup(html_week, "html.parser")

genre = soup_week.select_one("#GN0000").text
date = soup_week.select_one(".yyyymmdd").text

rank1 = soup_week.select(".lst50")
rank2 = soup_week.select(".lst100")
rank = rank1 + rank2

print(f'     주간 멜론 TOP100 {date} - {genre}')

for j in rank :
    rang = j.select_one(".rank")
    title = j.select_one(".ellipsis.rank01 > span > a") #.ellipsis.rank01 a로 적어도 된다.
    name = j.select_one(".checkEllipsis > a")
    album = j.select_one(".ellipsis.rank03 > a")
    change = j.select_one(".rank_wrap")
    print(f'<{rang.text} 위>\n제목 : {title.text}\n가수 : {name.text}\n앨범 : {album.text}')
    print(f'변동 : {change['title']}')
    print()