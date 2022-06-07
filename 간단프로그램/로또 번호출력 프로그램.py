from tkinter import *
# import tkinter as t


win = Tk()
win.title("로또번호 출력 프로그램")
# win.geometry("500x400+900+400")
win.geometry("250x260")

frame_display = win.Frame()
frame_display.pack()
# entry = Entry(win, width=30, border=1, relief="solid")
# entry.grid()

def event1():
    print("test")

btn1 = Button(win, text="출력", command=event1, width=4, height=2)
# btn1.grid(column=1, row=1)
btn1.pack()

def event2():
    print("취소 완료")


btn2 = Button(win, text="취소", command=event2, width=4, height=2)
# btn2.grid(column=1, row=2)
btn2.pack()

win.mainloop()
