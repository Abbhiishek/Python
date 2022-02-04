#                                 codingrooms.com assignments EXcercise 01



print('''
codingrooms.com assignments EXcercise 02


Instructions

Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.
Warning: The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.

Example Output


When you run your program, it should print the following:

>>>Day 1 - String Manipulation
>>>String Concatenation is done with the "+" sign.
>>>e.g. print("Hello " + "world")
>>>New lines can be created with a backslash and n.

The Code that was given for the debugging is :

                print(Day 1 - String Manipulation")
                print("String Concatenation is done with the "+" sign.")
                   print{'e.g. print ("Hello " + "world")")
                print(("New lines can be created with a backslash and n.")

''')

print("      SOLUTIONS")
print('''

- There is a bunch of Errors that we need to fix as we have :
     1. in first line we have missed a " at the starting of the value
     2.In second line we have used the same " " for showing the + , that will not work as it will take that as code so we can use
     a second option which is a single quote ' ' 
     3. In line 3 we have Intendations error and also after print we have used a { which is not the way a function works so we have
     have to change that to ( and at the end of the line we have to use single quote to match the opening quote and not raise codded code block 
     4. In line 4 by mistake we have given double starting bracket at the start of print statement , we have to delete one 



- SO The Final code Looks Like :
                    print("Day 1 - String Manipulation")
                    print('String Concatenation is done with the "+" sign.')
                    print('e.g. print ("Hello " + "world")')
                    print("New lines can be created with a backslash and n.")


Let's have a look at the Output :

''')

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print ("Hello " + "world")')
print("New lines can be created with a backslash and n.")
