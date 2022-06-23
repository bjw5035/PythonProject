from selenium import webdriver
import time

url = r'https://www.naver.com'
browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get(url)

browser.find_element_by_css_selector('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2) > a ').click()
time.sleep(2)


