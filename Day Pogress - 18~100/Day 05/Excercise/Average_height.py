height=input("Input a list of students : ").split()
for n in range (0, len(height)):
    height[n]=int(height[n])
sum = 0
len = 0
for number in height:
    len+=1
    sum+=number
avg=sum/len
avg=round(avg)
print("The Total Average Height :" + str(avg))