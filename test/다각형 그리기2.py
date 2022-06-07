import turtle

turtle.shape("turtle")
turtle.bgcolor("lightblue")
turtle.pensize(10)

#turtle.textinput, turtle.numinput
polygon = int(turtle.numinput("다각형 그리기", "몇 각형을 그릴까요?"))

for i in range(polygon):
    turtle.forward(100)
    turtle.left(360/polygon)


turtle.done()