#                                 codingrooms.com assignments EXcercise 03


print('''
                          codingrooms.com assignments EXcercise 03


                                     Instructions

Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

e.g.

https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow

Warning. Your program should work for different inputs. e.g. any name that you input.

                      Example Input
>>>>>>>>>>>>>>>>>>>>>> Angela
                     Example Output
>>>>>>>>>>>>>>>>>>>>>>   6
''')


print("      SOLUTIONS")

print('''

-So firstly we need an input statement that will take the input from the user
-secondly we will store that input into a variable which we will use later for finding the length
-To find the len of a string , in python there is a predefined function named len() which will come handy and we will use that also .
-afterward we will store the length in another variable and we will it print
Questions: how do we make it print: 
>>>>> print statement actually also allow to refer to any variable above it and we can use that variable and whenever we pass the variable 
      into the argument , the value stored in the varibale will be printed ! simple isn't ! 


SO the code that might work is :

                    name=input("what is your name")
                    number=len(name)
                    print(number)

Shocked to see that it all did in just three lines 


                                   MAKE IT INTO THE ACTION: 


''')
name=input("what is your name")
number=len(name)
print(number)