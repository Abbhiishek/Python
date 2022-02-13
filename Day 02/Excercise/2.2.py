
#                                 codingrooms.com assignments EXcercise 02


print('''
codingrooms.com assignments EXcercise 02


Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


Example Input
weight = 80
height = 1.75
Example Output
80 ÷ (1.75 x 1.75) = 26.122448979591837
26

Hint
Check the data type of the inputs.
Try to use the exponent operator in your code.
Remember PEMDAS.
Remember to convert your result to a whole number (int).

''')

#                                    Write your code below this line 👇



print('''                             Solution


            height = input("enter your height in m: ")
            weight = input("enter your weight in kg: ")
            bmi=int(weight)/(float(height)**2)
            bmi=round(bmi)
            print(bmi)



''')
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi=int(weight)/(float(height)**2)
bmi=round(bmi)
print(bmi)