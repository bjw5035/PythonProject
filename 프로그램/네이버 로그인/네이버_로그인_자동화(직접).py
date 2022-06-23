from selenium import webdriver
import pyautogui
import pyperclip
import time

url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get(url)


id = browser.find_element_by_css_selector('#id')
id.click()
pyperclip.copy('send2ugfd')
pyautogui.hotkey('Ctrl', 'v')
time.sleep(3)

pw = browser.find_element_by_css_selector('#pw')
pw.click()
pyperclip.copy('quswodn93!@')
pyautogui.hotkey('Ctrl', 'v')
time.sleep(3)

btn = browser.find_element_by_css_selector('#log\.login')
btn.click()