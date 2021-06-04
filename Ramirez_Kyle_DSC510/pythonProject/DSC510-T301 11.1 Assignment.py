# Week 11
# 11.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 29-May-2021
# Your program must have a welcome message for the user.
# Your program must have one class called CashRegister.
# Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
# Your program should have two getter methods.
# getTotal – returns totalPrice
# getCount – returns the itemCount of the cart
# Your program must create an instance of the CashRegister class.
# Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
# Your program should print the total number of items in the cart.
# Your program should print the total $ amount of the cart.
# The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.

import sys
import locale


class CashRegister:

    def __init__(self):
        self.price = 0.0
        self.total = 0

    def addItem(self, amount):
        self.price = self.price + amount

    def get_total_price(self, price):
        self.price = price
        return self.price

    def add_count(self, total):
        self.total = self.total + total

    def get_count(self, total):
        self.total = total
        return self.total

    @classmethod
    def userInput(cls):

        while True:
            getInput = input("What is the price of the item you wish to add?: ")
            try:
                getInput = float(getInput)
                register1 = CashRegister()
                register1.addItem(amount=getInput)
                register2 = CashRegister()
                register2.add_count(total=1)
                break
            except ValueError:
                try:
                    getInput = str(getInput)
                    getInput = getInput.upper()
                    if getInput == "DONE":
                        register1 = CashRegister.get_count()
                        register2 = CashRegister.get_total_price()
                        print("Here is your total and the number of items purchased")
                        print(f'Total amount is {register1()}')
                        print(f'Cost is {locale.currency(register2)}')
                        sys.exit()
                    else:
                        print("You did not enter price or DONE as they are the only valid responses")
                except ValueError:
                    print("You did not enter a price or DONE as they are the only valid responses")
        # return userInput

    def __repr__(self):
        return repr([self.price, self.total])


def main():
    print("Welcome, Enter the price for each item in your cart. Type and enter DONE when you're finished")
    while True:

        getInput = CashRegister.userInput


if __name__ == "__main__":
    main()
