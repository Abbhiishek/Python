print(
    """                                                    😀😀 Welcome To Day 01 Of Leraning Python 😀😀

                                                                       Topics Covered : 😎
                                                                       1.Print Function
                                                                       2.EXcercise 01
                                                                       3.backslash
                                                                       4.String Manipulation
                                                                       5.Indentations
                                                                       6.Code Intelligence
                                                                       7.EXcercise 02
                                                                       8.Input Functions
                                                                       9.comments


    """
)

print("                                                     This is a Print Statment.")

# This is a print functions (predefined functions! )
print('''

This is a print functions (predefined functions! )


print is the function name and inside the paranstes we pass the thing we want to print.


we have used " " to tell the system that its just a text that we have to print it's not hard coded code 

its have to be {STRINGS}

THE "" SHOULD HE OPENED AND CLOSED 

LIKE : print("this will not run and give error as we didn't close the value we want to pass )





SomeThing to Ponder:
   - Print statement not only print strings it can print any value stored in the variable for that :
      we just have to place that variable name in the brackets without quotation!


      cooool man !


''')
###########################################################################################################################################################

#                                                             codingrooms.com assignments EXcercise 01

print('''
                                                                 codingrooms.com assignments EXcercise 01


Example Output
After you have written your code, you should run your program and it should print the following:

Day 1 - Python Print Function
The function is declared like this:
print('what to print')

''')

#Write your code below this line 👇
print(" \nExcercise 01 from CodingRooms 👇 \n ") #\n is backslash and it is used to have a line break and shift the afterward content to next line in the compiler !!!  
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print(
'''
What i have learn't from this 👇:

Its appers that the whole 3 lines are in single block but they aree in different as they load with some time 

in line { print("print('what to print')") } we have used '' instead of "" as we can use both but we have to make sure that the opening and closing  quotation should be same , as in this line we want to print a ' ' so we used " " as opening and closing quotes  


alternatively we can use vice versa .......


Also , backslash n is used to have a line break and shift the afterward content to next line in the compiler !!!  

''')

###########################################################################################################################################################

#showing the use cases of the \n 
print('''

showing the use cases of the backslash👇

like if i want to print "Hello World !" 4 times 

1st Approach is to do this:

print("Hello World !")
print("Hello World !")
print("Hello World !")
print("Hello World !")

2nd Approach is to  do use backslash:
print("Hello World !{backslash}Hello World !{backslash}Hello World !{backslash}Hello World !")

Lets see the Outputs for the following :



''')
print("1st Approach")

print("Hello World !")
print("Hello World !")
print("Hello World !")
print("Hello World !")

print("2nd  Approach")
print("Hello World !\nHello World !\nHello World !\nHello World !")

# no difference in the output

print(" You can see there is no Difference in the output but we have difference in the code")

###########################################################################################################################################################

# String Manipulation and Code Intelligence
print("String Manipulation and Code Intelligence👇")

print('''

------------------------------------------------------------------------------------------

We can combine two string in print statement using '+' e.g. print("Hello"+"World")

Doing this the word Hello World is printed as HelloWorld no spaces are there in between but we can make it happer 


1st approach :

------- >>> print("Hello "+"World")

- The first approach is to add a space after Hello within the quotation to make it in considerations

2nd approach :

------- >>> print("Hello"+"World ")

- The second approach is to add a space after World within the quotation to make it in considerations

3rd  approach :

------- >>> print("Hello" + " " + "World ")

- The third approach is to add a blank space within quotes around with + to combine three different Strings in one place to make it in considerations.
- In this case the whole thing is focused in the addon as the separter in nothing but a blank space added within a quotes.



''')
###########################################################################################################################################################

# String Concatenation is a method of taking the strings and merging them into one.

print("String Concatenation is a method of taking the strings and merging them into one.")

#Indentations IN PYTHON 

print("Indentations IN PYTHON  👇 ")

print('''

In python Programming language we have spaces and that's matter the most (also known as Indentations)

like if we start our print statement not from the start of a line  , rather after some spaces 

like 
   print("Hello World !")
- This is going to give us a error called : IndentationError!
- Indentation is one of the success key to have python !


''')
print("Code Intelligence 🔻")
print('''
Code Intelligence is used to auto complete the code , all text-editor have one of these

- It makes Coding quite easy and Joyful !  
- Its also indicate some error before running the code ( Awesome !)
-Its indicate by some red lines below the coded code . 


''')

###########################################################################################################################################################
#                                                      codingrooms.com assignments EXcercise 02



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

###########################################################################################################################################################

#                                                        Input Functions Overview

print("                                                 Input Functions Overview")
print("""
There is most of time that you want to take a input from the user and then do something with that and give the output !

so How do we take Inputs from the user in python ?  

                            -> In python we do that by calling Input function
---------------------------------------------------------------------------------------------------------------------------------------
- Sytntax Goes like this :


                    input("The message on the behalf of which you want the Input from The user !")


---------------------------------------------------------------------------------------------------------------------------------------------

                                                   >PRINT VS INPUT<

    When we call the print function the job is to print the stuff and move to next line of code whereas , in case of Input 
    function the the stuff is simply printed like print function but in addtion to that it want a input from the user and 
    return that in the code and then move to next line of code .

---------------------------------------------------------------------------------------------------------------------------------------------

                                                      Input () Function

                                                 input("A promot for the user") 

    Also , we can store the input from the user into some thing called variables(refer to variables.py)

----------------------------------------------------------------------------------------------------------------------------------------------

                                               Stored_input=input("HEY READER!")

    The code above actually take the input from the user on the behalf of the msg {HEY READER!} and send it to code and python store 
    that in the Variable called Stored_input

---------------------------------------------------------------------------------------------------------------------------------------
                                        print ("Hello " + input ("What is your name?"))

    The code above simply  print the String Hello  and then it moves to second part for sting Concatenation  , then it promot for the input from the user
    giving the meassge   -> What is your name? <-  the input from the user is replaced into  -> input ("What is your name?") <-  and then 
    sting Concatenation is done and finally the output is given by the print function

    >>>What is your name?Abhishek #Here Abhishek is the input from the user
    >>>Hello Abhishek ! #The Output we get from the coded code

""")
###########################################################################################################################################################

#                                                        Commenting

print("                                    Commenting")

print('''
=========================================================================================================================


- if we want a line in the code that to be avoided by the interpreter and will not be considered while running the program
  the Commenting Concept comes in ....

- We just have to add a # in front of line to make that line comment

- If we use # in any line where some code is written then after the # all the things will be not considered 
  like : 
     print("hello" + #this is a comment)

    In this code after the # all the things will be considered as the comments and not to be considered while running
    as in the code the closing bracket is also after the # the code give the Error : SyntaxError

    - So its advised to use comments in new separate line or after the code is finished for that particular line .

- We have also a option of multi line commenting which comes handy when we have to comment a large content 
 
-  we can use """ {the content to 
          comments, supports multiline } """  , you can use single quote thrice also as now i am using that for 
          print statement (refer to printing.py), will give errors

=========================================================================================================================
                             So what's the practical use of the commenting ?

        1. actually comments are used to refer to the task that the code do 
        2. You can use that for you well wish.
        3. It can be used to Markdown something in the code , to make some notes , marking some code changes and so on ...
        
''')

###########################################################################################################################################################

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


print("                                          SOLUTIONS")

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


                    If you want to test the code head to the Excercise/Exercise 3 - Input Function.py


''')
###########################################################################################################################################################

#                                              variables

print("                                    variables")

print("""
We have seen in the Input section that we ask the user for the input and then we pass that data to code , but here we have a problem 

if we are taking the input from the user then its obvious that we are going to use that later but here we can't as we havn't stored the data 
anywhere and here comes the roles of variables 

- Variables are the unique identifer that we can refer in our code , we can make variable store some data 

earlier , 
      input("this will be input ")

      we used to take the input and pass it on to the code but we dont have the reference to that value so we are unable to 
      asccess later in our code.


      name=input("this will be input ")
      In this case we are as earlier taking the input but this time we are storing the value passed by the user to a variable called name
      so that we can asccess that value later in our code 
      so we can do :
      print(name) -> will print the value you have passed when its asked for the input!

      cool !


      Lets Try it Out : Go to Variables.py for code in action


""")
# name=input("naam kya hain ree tera : ")
# print("Your name is "+name)
# print("Lets move to next Part")

print("""

- A varaible in python programming is basically a named location (in storage in form of byte tape)that refers to a value
  or store a value and whose values can be used and processed during program excecution .
- variables are also known as symbolic variables
- Creating a Variable

            declare a variable that mean you created a variable 
            
            int a , b ,c ,d ;



            inizalise a variable
            a=1;
            b=2;
            .
            .
            .
            .
        Also , python is a interpreted language so we also can omit the decalaration and datatype(will be covered later ) is going to be assigned by the intepreter
        only inizalisation also works for python -> 

- Lvalues & Rvalues 

        lvalues:these are the expression that can come on the left hand side of an assignmnet 

                       -> are the object to which you are going to or want to store or assign a value or expression.

        rvalues:these are the expression that can come on the right  hand side of an assignmnet 

                       -> these are the literals and expressions that are assigned to the lvalues 


        a = 100

        _100 = a  (not reccommended)

        These are the things you can do:

            abhishek = "Mr. Kushwaha"
            sum = 0
            "Python"= language

        These you are not allowded to do !

            "Mr. Kushwaha" = abhishek
            0 =  sum
            "Python"= language


- Multiple Assignments

        1.we can assign the same value :

                a = 10
                b = 10
                c = 10

               ->  a = b = c = 10

        2. mutliple assignment main multiple and different value
                a = 10
                b = 20
                c = 30

               -> a ,b ,c =10 ,20 ,30


                     >->         we can change or alter the values stored in the variable by just assigning a new content to it     <-<
""")

###########################################################################################################################################################

#                                 codingrooms.com assignments EXcercise 04


print('''
                                 codingrooms.com assignments EXcercise 04




                                            Instructions


Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

                                      Example Input
                                        a: 3
                                        b: 5
                                    Example Output
                                    a: 5
                                    b: 3




                                    Given Code Base: 

                                    # 🚨 Don't change the code below 👇
                                    a = input("a: ")
                                    b = input("b: ")
                                    # 🚨 Don't change the code above 👆

                                    ####################################
                                    #Write your code below this line 👇




                                    #Write your code above this line 👆
                                    ####################################

                                    # 🚨 Don't change the code below 👇
                                    print("a: " + a)
                                    print("b: " + b)
''')

print("                                           SOLUTIONS")
print('''

- We have to use the variables to store the inputs from the user
- so now we have two variables which contain two different or same content and we have to swap it . 
- in general we do that by using a third variable that will store the imformation 
- so first we will transfer varaible 1 content to that third variables
- secondly we store the second variables content to first variables
- at last we will tranfer the third variable content to second one when
- at last the third variable should not have any content 

lets looks at the correct code :


            a=input("a:")
            b=input("b:")
            temp=a
            a=b
            b=temp
            print("a: " + a)
            print("b: " + b)

This is all the code that you need to swap two numbers /.....

To see it in action head over to Excercise 04 python file


''')