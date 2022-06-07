import turtle

turtle.shape("turtle") #triangle, square, arrow, circle, turtle
turtle.bgcolor("pink")

turtle.color("blue")
for i in range(4): # 0, 1, 2, 3
    turtle.forward(100) # 앞으로 100만큼 이동
    turtle.left(90) # 왼쪽으로 90도 회전

turtle.color("red")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.color("white")
for i in range(5):
    turtle.forward(100)
    turtle.left(360/5)

turtle.done()