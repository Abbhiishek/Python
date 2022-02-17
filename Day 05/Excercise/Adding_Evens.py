total= 0 
for n in range(1, 101 , 2):
    total+=n
print(total)


#Another way to do this :

total2=0
for i in range(0 , 101):
    if i %2 ==0 :
        total2  +=   i
print(total2)