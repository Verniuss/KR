# DSC 510
# Week 2
# 2.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 22-Mar-2021
# Assignment is to create a program that will:
# 1. Display a welcome message to the user.
# 2. Retrieve the company name from the user.
# 3. Retrieve the number of feet of fiber optic cable to be installed from the user.
# 4. Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# 5. Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.

# Displayed welcome Message
print("Welcome! Please continue if you wish to purchase some fiber optic cable")

# Prompt the user the company of purchase they are interested in
print("What company do you wish to purchase from?")
purchasing_company = input("Please type your preferred company of purchase")
print("You have selected", purchasing_company)

# Prompt the user the number of feet they wish to purchase
feet_of_fiber = input("How many feet of fiber optic cable do you wish to purchase?")
print("You have selected", feet_of_fiber)

# Calculate the cost of the purchase
cable_cost_by_feet = 0.87
cost_of_purchase = float(feet_of_fiber) * float(cable_cost_by_feet)

# Print a receipt for the user that includes company name, number of feet, calculated cost, and total cost
print("\nSee your receipt of purchase from", purchasing_company,
      "\nYou have purchased", feet_of_fiber, "feet of fiber for installation",
      "\nYour total cost is $", cost_of_purchase)

