import requests
from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.Chrome('C:/chromedriver.exe')

browser.get('https://www.naver.com')
browser.implicitly_wait(10)

# browser.find_element_by_css_selector("a.nav").click()

