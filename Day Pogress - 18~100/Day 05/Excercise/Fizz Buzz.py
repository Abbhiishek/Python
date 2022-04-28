fizzbuss = 0
fizz = 0
buss = 0
for n in range (1 , 101):
    if n % 3 == 0 and n%5==0:
        print("FizzBuzz")
        fizzbuss += 1
    elif n % 3 == 0 :
        print("Fizz")
        fizz += 1
    elif n % 5 == 0 :
        print("Buzz")
        buss += 1
    else:
        print(n)

print(f"The number of FizzBuzz are :" + str(fizzbuss))
print(f"The number of Fizz are :" + str(fizz))
print(f"The number of Buzz are :" + str(buss))