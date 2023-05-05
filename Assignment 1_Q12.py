import turtle

def boga(t,x,y,side):
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()

    for i in range(4):
        t.forward(side)
        t.left(90)
    t.penup()

def fundh():
    t = turtle.Turtle()
    x = 5
    y = 5
    z = -10
    for i in range(10):
        boga(t,(i - 3)* y,(i - 2)* x,(i - 20)* z)
    turtle.done()
fundh()
