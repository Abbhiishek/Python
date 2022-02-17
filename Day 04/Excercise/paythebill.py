import random
#asking for the names from the users:

names= input("Give me everybody name with space : ").split(" ")
person_who_pays=random.randint(0,len(names))

person_who_pays= names[person_who_pays]

print(f"{person_who_pays} is going to buy the meal today.")


# another way to doo : 
'''

            person_who_pays= random.choice(names)
            print(f"{person_who_pays} is going to buy the meal today.")



'''