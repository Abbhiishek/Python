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


Lets see the code in action::::::
''')
a=input("a:")
b=input("b:")
temp=a
a=b
b=temp
print("a: " + a)
print("b: " + b)
