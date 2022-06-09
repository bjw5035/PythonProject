import tkinter as t

win = t.Tk()
win.geometry("400x400")
win.title("pack")
win.option_add("*Font", "궁서 20")

x = 0.4
y = 0.4

btn = t.Button(win)
btn.config(text="({},{})".format(x,y))
btn.place(relx= x, rely= y)

win.mainloop()
