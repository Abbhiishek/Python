import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to the Turtle Game")

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

all_turtles = []

is_race_on = True

for i in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Turtle Race", prompt="Enter your bet for turtle: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            # if the winner is same as the user_bet then the user win
            if user_bet == winner:
                print(f"You win ! {user_bet} Won the race")
            else:
                print(f" You Lost ! {winner} Won the race")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# if user_bet == "red":
#     new_turtle.write("You win!", font=("Arial", 16, "normal"))


screen.exitonclick()
