'''
    You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5

                     = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

Example Input
test_h = 3
test_w = 9
Example Output
You'll need 6 cans of paint.


'''

#Write your code below this line 👇

import math
def paint_calc(wall_height, wall_width, coverage_per_can):
    wall_area = wall_height * wall_width
    paint_needed = math.ceil(wall_area / coverage_per_can)
    print(f"You'll need {paint_needed} cans of paint.")
    # return int(math.ceil((wall_height * wall_width) / coverage_per_can))





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(wall_height=test_h, wall_width=test_w, coverage_per_can=coverage)