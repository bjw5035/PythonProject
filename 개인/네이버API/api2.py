import requests

url = "https://openapi.naver.com/v1/search/blog"
params = {
    'query' : '', 'display': '10'
    ,'start': '1', 'sort': 'sim'
}
headers = {
    'X-Naver-Client-Id' : 'PWi_PEhUBBjD2GwaIQqd'
    ,'X-Naver-Client-Secret' : 'P_vFEb9YBW'
}

response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    global data
    global items
    data = response.json()
    items = (data['items'])
    item = items[0]
    print(item)

for item in items:
    title = item['title'].replace('<b>', '').replace('</b>', '')
    bloggername = item['bloggername']
    bloggerlink = item['bloggerlink']
