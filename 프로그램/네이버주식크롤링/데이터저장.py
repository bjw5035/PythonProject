import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\Users\send2\PythonProject\간단프로그램\네이버주식크롤링\주식_data.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화 된 시트

# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'
]

row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(price)
    ws[f'B{row}'] = int(price)
    row += 1

wb.save(fpath)


