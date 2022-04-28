import turtle

kaucha = turtle.Turtle()
kaucha.shape("turtle")
screen = turtle.Screen()
kaucha.color("blue")


def forward():
    kaucha.forward(100)


def backward():
    kaucha.backward(100)


def left():
    kaucha.left(90)


def right():
    kaucha.right(90)

def clear():
    kaucha.clear()
    kaucha.penup()
    kaucha.home()
    kaucha.pendown()


screen.listen()
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(screen.bye, "q")
screen.onkey(clear, "space")



screen.mainloop()

screen.exitonclick()
