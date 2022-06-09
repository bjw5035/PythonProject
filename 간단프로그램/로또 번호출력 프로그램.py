import tkinter as t
from bs4 import BeautifulSoup as bf

win = t.Tk()
win.title("로또번호 출력 프로그램")
win.geometry("500x400+900+400")

ent = t.Entry()


def event1():
    print("test")

btn1 = t.Button(win, text="출력", command=event1, width=4, height=2)
btn1.place(relx=0.4, rely=0.3)


def event2():
    print("취소 완료")

btn2 = t.Button(win, text="취소", command=event2, width=4, height=2)
btn2.place(relx=0.5, rely=0.3)

win.mainloop()
