# create  a random work using turtle


import random
import turtle

colours = ["red", "blue", "green", "yellow", "orange", "purple", "black", "white"]

direction = [0, 90, 180, 270]





def draw_art():
    window = turtle.Screen()
    window.bgcolor("#2A2550")

    kachua = turtle.Turtle()
    kachua.shape("turtle")
    kachua.pensize(4)
    kachua.color("#DEB6AB")
    kachua.speed(15)

    # for i in range(1, 37):
    #     kachua.forward(100)
    #     kachua.right(10)


    for i in range(1000):
        kachua.color(random.choice(colours))
        kachua.forward(random.randint(1, 100))
        kachua.right(random.choice(direction))


    window.exitonclick()

draw_art()



