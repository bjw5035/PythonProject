from tkinter import *

win = Tk()
win.title("Daum Log-in")
win.geometry("400x300")
win.option_add("*Font", "궁서 20")

# 로고(아무 이미지)
lab_d = Label(win)
img = PhotoImage(file= "C:\\Users\\send2\\OneDrive\\바탕 화면\\배경화면이미지\\바다.jpg", master=win)
img = img.subsample(8)
lab_d.config(image=img)
lab_d.pack()

# id 라벨
lab1 = Label(win)
lab1.config(text="Id")
lab1.pack()

# id
ent1 = Entry(win)

ent1.pack()

# pw라벨
lab2 = Label(win)
lab2.config(text="Pw")
lab2.pack()

# pw
ent1 = Entry(win)

ent1.pack()

# 로그인 버튼
btn = Button(win)
btn.config(text="로그인")
btn.pack()

win.mainloop()