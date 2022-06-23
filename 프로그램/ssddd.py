import requests
import tables
from mysql import *

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1018'
req = requests.get(url)

tables.Table()

if req.status_code == 200:
    data = req.json()
    print(data)
