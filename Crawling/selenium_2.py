# selenium 복습
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = "https://section.cafe.naver.com/ca-fe/home"

driver = webdriver.Chrome()
driver.get(url) # bs4에서 req = requests.get(url)와 동일
html = driver.page_source   # bs4에서 html = req.text와 동일
time.sleep(1)

print(html)

driver.quit()