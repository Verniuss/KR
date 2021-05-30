# Week 10
# 10.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 23-May-2021
# Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
# The program will receive a JSON response which includes various pieces of data.
# You should parse the JSON data to obtain the “value” key.
# The data associated with the value key should be displayed for the user (i.e., the joke).
# Your program should allow the user to request a Chuck Norris joke as many times as they would like.
# You should make sure that your program does error checking at this point.
# If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails,
# display a message for the user. There are other ways to handle this.
# Think about included string functions you might be able to call.

import sys
import requests
from pprint import pprint


def userInput():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.request("Get", url)
    joke = response.json()
    jokes = joke.items()
    while True:
        getInput = input("Would you like to hear a Chuck Norris joke?: ")
        try:
            getInput = str(getInput)
            getInput = getInput.upper()
            if getInput == "Y":
                for key, value in jokes:
                    if key == 'value':
                        pprint(value)
                break
            elif getInput == "N":
                print("That's it for Chuck Norris Jokes")
                sys.exit()
            else:
                print("You did not enter Y or N as they are the only valid responses")
                break
        except ValueError:
            print("You did not enter Y or N as they are the only valid responses")
            break
    return userInput()


def main():
    print("Welcome, type Y for a new joke and N to quit")
    YN = userInput()


if __name__ == "__main__":
    main()
