from selenium import webdriver
import pyautogui
import pyperclip
import time
from selenium.webdriver.chrome.service import Service

# 셀레니움 버전차이로 인한 소스 변경
url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
service = Service(executable_path='C:\chromedriver.exe')

driver = webdriver.Chrome(service=service)


time.sleep(3)
