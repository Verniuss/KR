# DSC 510
# Week 5
# 5.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 17-Apr-2021
# Assignment is to create a program that will:
# The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
# Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
#       This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
#       This function will print the calculated value for the end user.
# Define a function named calculateAverage which takes no parameters.
#       This function will ask the user how many numbers they wish to input.
#       This function will use the number of times to run the program within a for loop in order to calculate the total and average.

# Addition Calculation
def additionCalculation(arg1, arg2):
    calculatedAnswer = arg1 + arg2
    return calculatedAnswer


# Subtraction Calculation
def subtractionCalculation(arg1, arg2):
    calculatedAnswer = arg1 - arg2
    return calculatedAnswer


# Multiplication Calculation
def multiplicationCalculation(arg1, arg2):
    calculatedAnswer = arg1 * arg2
    return calculatedAnswer


# Division Calculation
def divisionCalculation(arg1, arg2):
    calculatedAnswer = arg1 / arg2
    return calculatedAnswer


# Gets first argument for +, -, *, / calculations
# While True sets up conditions to prevent the user from entering anything that's not a number
def getArgument1():
    while True:
        arg1 = input("What is your first addition argument?: ")
        try:
            arg1 = float(arg1)
            break
        except ValueError:
            print('You did not enter a number. Please ensure a number is entered at this prompt.')
    return arg1


# Gets second argument for +, -, *, / calculations
# While True sets up conditions to prevent the user from entering anything that's not a number
def getArgument2():
    while True:
        arg2 = input("What is your second addition argument?: ")
        try:
            arg2 = float(arg2)
            break
        except ValueError:
            print('You did not enter a number. Please ensure a number is entered at this prompt.')
    return arg2


# Calculates the average
def calculateAverage():

    # Checks to make sure the user is entering in a number. If not it asks them to enter
    # it again and loops until they enter a number.
    # This step asks the user how many numbers they want to enter
    while True:
        total = float(input("How many numbers do you want to enter?: "))
        try:
            total = float(total)
            break
        except ValueError:
            print('You did not enter a number. Please ensure a number is entered at this prompt.')

    count = 0
    totalNumbers = 0

    # Checks to make sure the user is entering in a number. If not it asks them to enter
    # it again and loops until they enter a number.
    while count < total:
        while True:
            number = float(input("Enter a number you want calculated into the average: "))
            try:
                number = float(number)
                break
            except ValueError:
                print('You did not enter a number. Please ensure a number is entered at this prompt.')

        count = count + 1
        totalNumbers = totalNumbers + number

    average = totalNumbers / total
    return average


def main():
    # Created 2 lists, one with and the other without Avg. Reason being is there are some unique steps in excluding list vs including.
    inputsTypesExcludingAvg = ("+", "-", "*", "/")
    inputsTypesIncludingAvg = ("+", "-", "*", "/", "Avg")

    # This while true ensures that the user does not enter something outside the including list. Otherwise it will end the program.
    while True:
        calculationType = input("What type of calculation do you wish to perform? "
                                "Submit a + for addition, a - for subtraction, a * "
                                "for multiplication, a / for division, and a avg for average: ")
        try:
            # Include average for this. To make certain the user is only using the correct input variables
            calculationType not in inputsTypesIncludingAvg
        except ValueError:
            print("Try again. This time make sure to type in either "
                  "a +, -, *, /, or avg as your entry type.")
            continue
        else:
            break

    # Various if statements that ask the user what 2 arguments they wish to calculate by the calculation type they selected.
    if calculationType in inputsTypesExcludingAvg:
        print("you have selected", calculationType)
        arg1 = getArgument1()
        arg2 = getArgument2()

        if calculationType == "+":
            calculatedAnswer = additionCalculation(arg1, arg2)
            print(calculatedAnswer)

        if calculationType == "-":
            calculatedAnswer = subtractionCalculation(arg1, arg2)
            print(calculatedAnswer)

        if calculationType == "*":
            calculatedAnswer = multiplicationCalculation(arg1, arg2)
            print(calculatedAnswer)

        if calculationType == "/":
            calculatedAnswer = divisionCalculation(arg1, arg2)
            print(calculatedAnswer)

    # Average calculation step. Asks user how many numbers they want to enter.
    # Then runs through a loop to allow them to enter each number. Result prints out the average of the numbers entered.
    if calculationType == "avg":
        average = calculateAverage()
        print("The average of the numbers selected is.", average)

    if calculationType not in inputsTypesIncludingAvg:
        print("You must enter either a +, -, *, /, or avg to proceed with this program")


if __name__ == "__main__":
    main()
