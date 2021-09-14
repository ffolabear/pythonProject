import dload

# 이미지 파일을 저장해줌
# dload.save("https://www.nps.gov/bela/learn/nature/images/PolarBear.jpg")

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

driver.get("http://www.naver.com")