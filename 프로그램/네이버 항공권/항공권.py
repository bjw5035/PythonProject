from selenium import webdriver

# 네이버 항공편
url = r'https://flight.naver.com/'

browser = webdriver.Chrome('C:\chromedriver.exe')
browser.get(url)
browser.implicitly_wait(10)

## 출발지 선택 (김포)
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.start').click()
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.autocomplete_autocomplete__ZEwU_.is_departure > div.autocomplete_content__3RhAZ > section > section > button:nth-child(1)').click()
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.autocomplete_autocomplete__ZEwU_.is_departure > div.autocomplete_content__3RhAZ > section > section > div > button:nth-child(1)').click()

## 도착지 선택 (제주)
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.end > i').click()
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.autocomplete_autocomplete__ZEwU_.autocomplete_is_arrival__JR22W > div.autocomplete_content__3RhAZ > section > section > button:nth-child(1)').click()
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.autocomplete_autocomplete__ZEwU_.autocomplete_is_arrival__JR22W > div.autocomplete_content__3RhAZ > section > section > div > button:nth-child(2)').click()

## 가는 날 선택


browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > button > span').click()

