from time import *

print("Seting Up the CALCULATOR")
sleep(2)
print("Hey Welcome to TIP CALCULATOR")
sleep(2)
print('''
 _   _                 _            _       _             
| | (_)               | |          | |     | |            
| |_ _ _ __   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| __| | '_ \ / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |_| | |_) | (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \__|_| .__/ \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
      | |                                                 
      |_|       
 
                                              ''')
sleep(2)
print("Welcome TO TIP CALCULATOR.")
sleep(2)
bill=float(input("What is your Total Bill :"))
sleep(2)
percentage=float(input("What Percentage Tip Would you Like To Give ? :"))
Amount=bill+(percentage*bill)/100
sleep(2)
no_people=int(input("How many people to spilt the bill :"))
Amount_each=Amount/no_people
sleep(2)
print("Calculating....")
sleep(2)
print("Still Calculating....")
sleep(2)
print(f"Each Of You Should Pay :{Amount_each}")