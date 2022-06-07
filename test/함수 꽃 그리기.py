import turtle as t

t.speed(0)
def petal():
    for i in range(2):
        t.circle(150, 110)
        t.left(70)

def draw_flower():
    t.color("pink")
    t.begin_fill()
    for i in range(6):
        petal()
        t.left(360/6)
    t.end_fill()

    t.goto(0, -30)
    t.color("deeppink")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

t.ht()
t.bgcolor("forestgreen")
draw_flower()
t.done()
