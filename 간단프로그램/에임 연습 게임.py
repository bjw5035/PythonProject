import random
import tkinter as t
import random as r

win = t.Tk()
win.title("Aim_Game")
win.geometry("600x200+1000+500")
win.option_add("*Font", "궁서 20")

# Label
lab = t.Label(win)
lab.config(text="표적 개수")
lab.grid(column=0, row=0, padx=20, pady=20)

# Entry
ent = t.Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

# global을 이용해서 전역변수로 쓸수 있게 함
# 기본적으로 입력받는 값은 문자열로 인식하기 때문에 필요에 따라서 형변환을 해줘야 함
def btn_f():
    global num_t
    num_t = int(ent.get())

    # win 안에 있는 List이다, 위젯 전체를 뜻함(grid_slaves) , grid를 사용 했기 때문에 grid_slaves(pack, place등을 사용했다면 pack_slaves 또는 place_slaves사용)
    # destroy 모든 요소를 지운다는 뜻.
    for wg in win.grid_slaves():
        wg.destroy()
    win.geometry("600x500+1000+500")
    ran_btn()

#랜덤한 위치에서 버튼이 생성
def ran_btn():
    global btn
    btn = t.Button(win)
    btn.config(bg="red")
    btn.config(command=ran_box)
    btn.place(relx= random.random(), rely=random.random())

def ran_box():
    btn.destroy()
    ran_btn()
    if btn == ent:
        btn.close()

# Button
btn = t.Button(win)
btn.config(text="시작")
btn.config(command=btn_f)
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()
