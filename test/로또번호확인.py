from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.title("로또회차")
win.geometry("300x200")

ent = Entry(win)
ent.pack()

def ent_p():
    # a = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
    req = requests.get(url)
    print(req)

btn = Button(win)
btn.config(text="버튼")
btn.config(command= ent_p)
btn.pack()

win.mainloop()