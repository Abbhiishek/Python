############DEBUGGING#####################

# Describe Problem
def my_function():
    """
    The problem is that range function don't go to the last number in this case it will
      end up with i = 19. so the check for the if statement will never be true.
      
    """
    for i in range(1, 20):
        if i == 20:
            print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
"""the randint function will generate a random number between 1 and 6. including both 1 and 6.
   so the dice_num will be a random number between 1 and 6.
   but the list only have index from 0 to 5
   so the dice_num will be a random number between 0 and 5.
   else for dice_num = 6, the index will be 6.
   which is not present in the list.
   
   so the dice_num will be a random number between 0 and 5.
   
   solutuion: 
   dice_num = randint(0, 5))
   """
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if 1980 < year < 1994:
    print("You are a millenial.")
elif year > 1994:
    """
    if year > 1994:
        print("You are a millenial.")
        
        but if the year is 1994 no check gives you true
        so the program doesn't print anything.
        solution:
        if year > 1980 and year < 1994:
            print("You are a millenial.")
            
        elseif year >= 1994:
            print("You are a Gen Z.")
    """
    print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you?")
"""
the default value of age is in string so we have to convert ingto inrt
.
"""
# solution
age = int(age)
if age > 18:
    # print("You can drive at age {age}.")
    print(f"You can drive at age {age}.")

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
