from selenium import webdriver
import time
import pyautogui
import pyperclip

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
# browser = webdriver.Chrome('C:\chromedriver')
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.maximize_window() # 화면 최대화
browser.get(url)

# 아이디 입력창
id = browser.find_element_by_css_selector("#id")
id.click()
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = browser.find_element_by_css_selector("#pw")
pw.click()
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)

# 로그인 버튼
login_btn = browser.find_element_by_css_selector("#log\.login")
login_btn.click()