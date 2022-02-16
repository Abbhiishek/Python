import random 
from time import *
from ascii import *
from treaure import Start
from lost_lady import *
from school import *
from asking_name import ask_name





print("Welcome to the Game Of Choice !")
choice_number= int(input('''

                                   __     _           _          
                                  / _|   | |         (_)         
  __ _  __ _ _ __ ___   ___  ___ | |_ ___| |__   ___  _  ___ ___ 
 / _` |/ _` | '_ ` _ \ / _ \/ _ \|  _/ __| '_ \ / _ \| |/ __/ _ |0
| (_| | (_| | | | | | |  __/ (_) | || (__| | | | (_) | | (_|  __/
 \__, |\__,_|_| |_| |_|\___|\___/|_| \___|_| |_|\___/|_|\___\___|
  __/ |                                                          
 |___/                                                           

Hey This is Abhishek , the developer of Game of guesses !!!!

we have Bunch of Options for You to get started with the game :    

Enter 0 for Treaure Hunt , 1 for Lost Lady , 2 for Getting to School 

'''))
sleep(2)
ask_name()
if choice_number == 0:
    starting=random.choice(Start)
    print(starting)


# elif choice_number == 1:



# elif choice_number == 2:

# else:
#     print








print(boat)