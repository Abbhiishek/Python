import random
import colorgram
import turtle

# Extract 600 colors from an image.
colors = colorgram.extract('profile-pic.png', 600)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb  # e.g. (255, 151, 210)
hsl = first_color.hsl  # e.g. (230, 255, 203)
proportion = first_color.proportion  # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

# print(rgb)
# print(hsl)
# print(proportion)
# print(first_color)

Added_colors = []
for color in colors:
    """
    This loops through the colors and adds them to a list
    
    """
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    new_color = (r, g, b)
    Added_colors.append(new_color)
    # print(color.rgb)

print(Added_colors)

# Creating a turtle instance
turtle.colormode(255)
window = turtle.Screen()
t = turtle.Turtle()
t.shape("classic")
turtle.bgcolor("black")
t.penup()
t.hideturtle()
t.speed("fast")
t.setheading(255)
t.forward(300)
t.setheading(0)


for i in range(500):
    t.dot(20, random.choice(Added_colors))
    t.forward(50)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


window.exitonclick()