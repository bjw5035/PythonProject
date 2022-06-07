import turtle as t # 별칭

t.bgcolor("pink")
t.color("red")

t.begin_fill() # 도형 내부 색상채우기(시작)
for i in range(3):
    t.forward(200)
    t.right(360/3)
t.end_fill() # 끝날때를 지정해주기

t.forward(100)
t.color("green")
t.begin_fill()
t.circle(100) # ()안에 반지름
t.end_fill()

t.goto(130, 130) # x좌표, y좌표
t.color("chocolate")
t.begin_fill()
t.circle(70)
t.end_fill()

t.color("gold")
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

t.done()