import requests
from bs4 import BeautifulSoup

# 접속하고자 하는 주소 입력 → url
url = "https://www.naver.com"

# get 방식을 이용해서 서버에게 resource를 보내도록 요청.
# requests의 경우 정적 페이지에서는 처음에 사용되고 잘 사용되지 않음.
# requests로 넘어오는 내용은 페이지 소스 보기의 내용과 동일.
req = requests.get(url)   # requests요청을 url 주소로 보내기.
# print(req)

# get 방식을 통해서 가져온 데이터 중 우리가 필요한 데이터는 텍스트 형태의 자료.
html = req.text
# print(html)

# BeautifulSoup 함수에는 2가지 파라미터 필요. (html, html.parser)
# 파서로 컴퓨터가 이해할 수 있는 트리구조로 변경하는 것이 진행.
soup = BeautifulSoup(html, "html.parser")

# select_one은 원하는 태그(class, id, tag) 찾아주는 것.
query = soup.select_one("#query")
print(query)