import os
import time


class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def __str__(self):
        return f'The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money'

    def pay(self, choice):
        """
        pay the coffee machine for the coffee
        :param choice:  1 , 2 , 3
        :return: None
        """
        # create a method to pay the bill
        if choice == '1':
            print("Your bill is Rs.250")
            bill = int(input())

            if bill > 250:
                print("Here is your change", bill - 250)
        elif choice == '2':
            print("Your bill is Rs.350")
            bill = int(input())

            if bill > 350:
                print("Here is your change", bill - 350)

        elif choice == '3':
            print("Your bill is Rs.450")
            bill = int(input())

            if bill > 350:
                print("Here is your change", bill - 450)






    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        choice = input()
        if choice == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.coffee < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
                time.sleep(10)
                self.pay(choice)
                print("Here is your coffee! \n  ☕  Enjoy ")

        elif choice == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.coffee < 20:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
                time.sleep(10)
                self.pay(choice)
                print("Here is your coffee! \n  ☕  Enjoy ")
        elif choice == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')

            elif self.coffee < 12:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')
                time.sleep(10)
                self.pay(choice)
                print("Here is your coffee! \n  ☕  Enjoy ")

        elif choice == 'back':
            return

        else:
            print('Invalid choice!')
        # Clearing the Screen
        os.system('')
        self.buy()

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())
        self.fill()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        self.take()

    def main(self):
        print('Write action (buy, fill, take, remaining, exit):')
        choice = input()
        if choice == 'buy':
            self.buy()
        elif choice == 'fill':
            self.fill()
        elif choice == 'take':
            self.take()
        elif choice == 'remaining':
            print(self)
        elif choice == 'exit':
            return
        else:
            print('Invalid choice!')
        self.main()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
print(coffee_machine.__str__())
print(coffee_machine.__init__(544, 454554, 5445546, 456456546, 456546546))
# while True:
coffee_machine.main()
