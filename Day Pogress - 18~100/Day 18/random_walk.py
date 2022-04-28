# create  a random work using turtle


import random
import turtle

colours = ["red", "blue", "green", "yellow", "orange", "purple", "black", "white"]

direction = [0, 90, 180, 270]


# create a wall check function and if the turtle is at the edge of the screen, it will turn around


def wall_checker(some_turtle):

    """
    still need to fix the wall checker
    :param some_turtle:
    :return: None
    """
    if some_turtle.xcor() > 300 or some_turtle.xcor() < -300:
        some_turtle.left(180)
    if some_turtle.ycor() > 300 or some_turtle.ycor() < -300:
        some_turtle.left(180)



def draw_art():
    turtle.colormode(255)
    window = turtle.Screen()
    window.bgcolor("#2A2550")

    kachua = turtle.Turtle()
    kachua.shape("classic")
    kachua.pensize(15)
    kachua.color("#DEB6AB")
    kachua.speed("fastest")

    # for i in range(1, 37):
    #     kachua.forward(100)
    #     kachua.right(10)

    for i in range(1000):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_colours = (r, g, b)
        kachua.color(random_colours)
        kachua.forward(random.randint(1, 100))
        wall_checker(kachua)
        kachua.right(random.choice(direction))
        wall_checker(kachua)

    window.exitonclick()


draw_art()
