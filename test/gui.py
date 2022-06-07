from tkinter import *

win = Tk()
win.title("테스트")
win.geometry("540x280+600+400")

btn = Button(win, text="버튼", padx=10, pady=10)
btn.pack()

win.mainloop()