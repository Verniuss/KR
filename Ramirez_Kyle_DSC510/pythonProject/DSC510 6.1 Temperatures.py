# Week 6
# 6.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 21-Apr-2021
# Assignment is to create a program that will:
# Allow the user to input a series of temperatures along with a sentinel value
# (do not use a number for a sentinel value) which will stop the user input.
# Evaluate the temperature list to determine the largest and smallest temperature.
# Print the largest temperature.
# Print the smallest temperature.
# Print a message that tells the user how many temperatures are in the list.

# The def getTemperature retrieves an input from the user. Checks to see if the input is a number or a string,
# if it's a number: it stores the number into a list,
# if it's a string: it checks to see if the string is the word stop (converts it to uppercase)
# if it's a string that's not stop: tells the user they need to either enter a number or type stop
def getTemperature():
    while True:
        tempInput = input("What temperature do you want to add in degrees celsius?: ")
        try:
            tempInput = float(tempInput)
            break
        except ValueError:
            try:
                tempInput = str(tempInput)
                tempInput = tempInput.upper()
                if tempInput == str("STOP").upper():
                    tempInput == "STOP"
                    break
                else:
                    print('You did not enter a number or STOP. Please ensure a number is entered at this prompt.')
            except ValueError:
                print('You did not enter a number or STOP. Please ensure a number is entered at this prompt.')
    return tempInput


temperatures = []


def main():

    tempInput = 0
    while True:
        tempInput = getTemperature()
        if tempInput != str("stop").upper():
            temperatures.append(tempInput)
        else:
            print("\nThere are ", len(temperatures), " temperatures added by the user."
                  "\nThe maximum value entered by the user is", max(temperatures),
                  "\nThe minimum value entered by the user is", min(temperatures))
            break


if __name__ == "__main__":
    main()
