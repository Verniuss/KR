# Week 2
# 2.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 10-June-2021
# Display the text “Hello World! I wonder why that is always the default coding text to start with”
# Add two numbers together
# Subtract a number from another number
# Multiply two numbers
# Divide between two numbers
# Concatenate two strings together (any words)
# Create a list of 4 items (can be strings, numbers, both)
# Append an item to your list (again, can be a string, number)
# Create a tuple with 4 items (can be strings, numbers, both)

def main():
    adding_Numbers = 4 + 5
    subtracting_Numbers = 5 - 3
    multiply_Numbers = 5 * 3
    divide_Numbers = 6 / 2
    string1 = "Hello"
    string2 = "World"
    concat_Word = string1 + " " + string2
    numbers_List = [2, 5, 6, 7]
    numbers_Tuple = (5, 10, 2, 6)

    print("Hello World! I wonder why that is always the default coding text to start with")
    print(adding_Numbers)
    print(subtracting_Numbers)
    print(multiply_Numbers)
    print(divide_Numbers)
    print(concat_Word)
    print(numbers_List)
    numbers_List.append(8)
    print(numbers_List)
    print(numbers_Tuple)


if __name__ == "__main__":
    main()
