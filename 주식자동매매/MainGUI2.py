import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *


# 탑레벨 win 인스턴스 생성
win = tk.Tk()
win.geometry("500x500")
win.title("Main GUI")


# Label 사용
label = tk.Label(win, text="테스트", width=10, height=5, fg="black")
label.pack()


# 버튼 close
def close():
    print("종료되었습니다.")
    win.destroy()
    # win.quit()
    # exit()

button = tk.Button(height="5", width="10", text="종료", command=close())
button.pack()



# 창 종료 시까지 유지
win.mainloop()







# ------------------------------------------------------------- bak
# window = tk.Tk()
# window.title("GUI")
# window.geometry("400x400")
#
# # 레이블을 이용한 텍스트 출력
# lb_1 = tk.Label(text="test")
# lb_1.pack()
#
# # 클릭시 작동하는 버튼(종료)
# def close():
#     window.destroy()
#
# button = tk.Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
# button.pack()
#
#
# window.mainloop()


