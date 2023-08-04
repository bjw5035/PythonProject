import sys
import tkinter

from tkinter import *


window = tkinter.Tk()
window.title("GUI")
window.geometry("400x400")

# 레이블을 이용한 텍스트 출력
lb_1 = tkinter.Label(text="test")
lb_1.pack()

# 클릭시 작동하는 버튼(종료)
def close():
    window.destroy()

button = tkinter.Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
button.pack()


window.mainloop()


