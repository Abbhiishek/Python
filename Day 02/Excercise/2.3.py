#                                 codingrooms.com assignments EXcercise 03


print('''
codingrooms.com assignments EXcercise 03


Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.

''')

#                                    Write your code below this line 👇


print('''

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age=int(age)
rem_age= 90 - age
days=rem_age*365
weeks=rem_age*52
months=rem_age*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")



''')

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age=int(age)
rem_age= 90 - age
days=rem_age*365
weeks=rem_age*52
months=rem_age*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")