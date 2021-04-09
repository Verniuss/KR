# DSC 510
# Week 4
# 4.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 9-Apr-2021
# Assignment is to create a program that will:
# 1. Display a welcome message to the user.
# 2. Retrieve the company name from the user.
# 3. Retrieve the number of feet of fiber optic cable to be installed from the user.
# 4. Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# 5. Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# 6. Adding bulk conditions if the user purchases more than 500ft = $0.50/ft, 250ft = $0.70/ft, 100ft = $0.80/ft
# 7. Add a Main Function and a Cost Function

def calculate_cost(cable_cost_by_feet, feet_of_fiber):
    cost_of_purchase = cable_cost_by_feet * feet_of_fiber
    return cost_of_purchase


def main():
    # Displayed welcome Message
    print("Welcome! Please continue if you wish to purchase some fiber optic cable")

    # Prompt the user the company of purchase they are interested in
    print("What company do you wish to purchase from?")
    purchasing_company = input("Please type your preferred company of purchase")
    print("You have selected", purchasing_company)

    # Prompt the user the number of feet they wish to purchase
    # loops back to user so it doesn't error out and not finish the program if they don't type in a number
    # Check if they entered a number. If not kick back to user to change their response to a number
    while True:
        feet_of_fiber = input("How many feet of fiber optic cable do you wish to purchase?")
        try:
            feet_of_fiber = float(feet_of_fiber)
            break
        except ValueError:
            print('You did not enter a number. Please ensure a number is entered at this prompt.')

    # Calculate the cost of the purchase
    if feet_of_fiber > 500:
        cable_cost_by_feet = 0.5
    elif feet_of_fiber > 250:
        cable_cost_by_feet = 0.7
    elif feet_of_fiber > 100:
        cable_cost_by_feet = 0.8
    else:
        cable_cost_by_feet = 0.87

    cost_of_purchase = calculate_cost(cable_cost_by_feet, feet_of_fiber)

    # Print a receipt for the user that includes company name, number of feet, calculated cost, and total cost
    print("\nSee your receipt of purchase from", purchasing_company,
          "\nYou have purchased", feet_of_fiber, "feet of fiber for installation",
          "\nYour total cost is $", cost_of_purchase)


if __name__ == "__main__":
    main()
