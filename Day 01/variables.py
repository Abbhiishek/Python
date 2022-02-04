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
name=input("naam kya hain ree tera : ")
print("Your name is "+name)
print("Lets move to next Part")

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