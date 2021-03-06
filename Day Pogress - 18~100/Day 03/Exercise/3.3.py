from time import *
#                                 codingrooms.com assignments EXcercise 03


print('''
codingrooms.com assignments EXcercise 03
πͺThis is a Difficult Challenge πͺ
Instructions
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 Γ· 4 = 500 (Leap)

2000 Γ· 100 = 20 (Not Leap)

2000 Γ· 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 Γ· 4 = 525 (Leap)

2100 Γ· 100 = 21 (Not Leap)

2100 Γ· 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input 1
2400
Example Output 1
Leap year.
Example Input 2
1989
Example Output 2
Not leap year.


# π¨ Don't change the code below π
year = int(input("Which year do you want to check? "))
# π¨ Don't change the code above π

#Write your code below this line π

''')

#                                    Write your code below this line π

#                                                   Solution
print('''

# π¨ Don't change the code below π
year = int(input("Which year do you want to check? "))
# π¨ Don't change the code above π

#Write your code below this line π


if year % 4 == 0:
    if year % 100 :
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")


Lets check the program 

''')
sleep(2)

# π¨ Don't change the code below π
year = int(input("Which year do you want to check? "))
# π¨ Don't change the code above π

#Write your code below this line π


if year % 4 == 0:
    if year % 100==0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

