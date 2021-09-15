from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

url = "https://search.naver.com/search.naver?&where=news&query=코로나%20확진자"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

for article in articles:
    title = article.select_one('div.news_area > a').text
    url = article.select_one('div.news_area > a')['href']
    company = article.select_one('a.info.press').text.split(' ')[0].replace('언론사', '')
    thumbnail = article.select_one('img')['src']

    ws1.append([title, url, company, thumbnail])


wb.save(filename='저장하고 싶은 파일이름')
driver.quit()

