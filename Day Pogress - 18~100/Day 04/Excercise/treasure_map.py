from time import *
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print("Looks like you have got some treasure buried in somewhere  ,,, look here is the map :")
sleep(2)
print(f"{row1}\n{row2}\n{row3}")
sleep(2)
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal=int(position[0])-1
vertical=int(position[1])-1
map[horizontal][vertical]="🏴"



#Write your code above this row 👆
sleep(2)
print("Hiding the treasure ......")
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")