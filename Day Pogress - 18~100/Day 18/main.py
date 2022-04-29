# create a turtle program that draws a square


import turtle


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_circle(some_turtle):
    for i in range(1, 37):
        some_turtle.circle(100)
        some_turtle.right(10)




# create a turtle program that draws a house with mountains

def draw_mountain(some_turtle):
    for i in range(1, 37):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_house(some_turtle):
    for i in range(1, 37):
        some_turtle.forward(100)
        some_turtle.right(90)



def draw_art():
    window = turtle.Screen()
    window.bgcolor("#2A2550")

    kachua = turtle.Turtle()
    kachua1 = turtle.Turtle()
    kachua.shape("turtle")
    kachua1.shape("classic")
    kachua.color("#DEB6AB")
    kachua1.color("#B9F8D3")
    kachua.speed(20)
    kachua1.speed(20)
    for i in range(1, 37):
        draw_square(kachua)
        kachua.right(10)

    kachua.color("#FF6FB5")

    draw_circle(kachua)
    kachua.forward(100)
    draw_circle(kachua)
    kachua1.backward(100)
    # draw_circle(kachua1)
    # kachua1.left(100)
    # kachua1.forward(100)
    # draw_circle(kachua1)



    window.exitonclick()


draw_art()


# create a turtle program that draw love


def draw_love(some_turtle):

        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art1():

    window = turtle.Screen()
    window.bgcolor("black")

    kachua = turtle.Turtle()
    kachua.shape("turtle")
    kachua.color("red")
    kachua.speed(20)
    for i in range(1, 37):
        draw_love(kachua)
        kachua.right(10)

    window.exitonclick()

draw_art1()