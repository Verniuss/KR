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


getInputs = CashRegister.userInput


