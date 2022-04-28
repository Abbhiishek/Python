from re import L, T, U
from time import *
from tkinter import E
#                                 codingrooms.com assignments EXcercise 05


print('''
codingrooms.com assignments EXcercise 05


💪 This is a Difficult Challenge 💪
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


''')

#                                    Write your code below this line 👇

#                                                   Solution
print('''                           Solution


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name=(name1+name2).lower()
T=combined_name.count("t")
R=combined_name.count("r")
U=combined_name.count("u")
E=combined_name.count("e")
true_sum= T+R+U+E

L=combined_name.count("l")
O=combined_name.count("o")
V=combined_name.count("v")
E=combined_name.count("e")

love_sum=L+O+V+E
lovescore=int(str(true_sum)+str(love_sum))


if lovescore <10 or lovescore >90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore >=40 and lovescore <=50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")

    
Lets check the program 

''')
sleep(2)
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name=(name1+name2).lower()
T=combined_name.count("t")
R=combined_name.count("r")
U=combined_name.count("u")
E=combined_name.count("e")
true_sum= T+R+U+E

L=combined_name.count("l")
O=combined_name.count("o")
V=combined_name.count("v")
E=combined_name.count("e")

love_sum=L+O+V+E
lovescore=int(str(true_sum)+str(love_sum))


if lovescore <10 or lovescore >90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore >=40 and lovescore <=50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")