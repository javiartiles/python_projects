# ------------------------------------ #
# Javier Artiles Manrique de Lara
# MSBA 502 - Analytics Programming I
# Homework 1: Citadel Gift Shop
# ------------------------------------ #

# This variable will storage how much money the client will need to pay.
money = 0

print("Welcome to The Citadel's Gift Shop! Let's work on your order.")

# I ask the clients if they want to buy the first product
question = input("\nWould you like to buy any Plumbuses (yes/no)? ")

# I use an "if" condition because I have different options.
if question == "Yes" or question == "yes" or question == "Y" or question == "y":
    # Depending on the amount of gallons price will change, so I ask the clients to tell how much they want.
    unit = float(input("How many gallons of Plumbuses would you like to buy? "))

    # Let's create the formulas in order to calculate the amount of money it will cost the product and to reassign
    # the "money" variable.
    if unit < 5:
        money = money + (unit * 20)

    elif unit < 15:
        money = money + (unit * 17.5)

    else:
        money = money + (unit * 15.25)

# We close the "if" condition when the answer is "No".
elif question == "No" or question == "no" or question == "N" or question == "n":
    print("Let's move to the next product")

# It is necessary to understand that clients could not answer the way I want.
else:
    print("ERROR! Your answer does not work, we will consider it as a NO.")

# Then, I repeat the same structure for the second and third product.

# 2nd product.
question = input("\nWould you like to buy any Meeseeks Boxes (yes/no)? ")

if question == "Yes" or question == "yes" or question == "Y" or question == "y":
    unit = float(input("How many gallons of Meeseeks Boxes would you like to buy? "))

    if unit < 10:
        money = money + (unit * 1.75)

    elif unit < 18:
        money = money + (unit * 1.5)

    else:
        money = money + (unit * 1.25)

elif question == "No" or question == "no" or question == "N" or question == "n":
    print("Let's move to the next product")

# It is necessary to understand that clients could not answer the way I want.
else:
    print("ERROR! Your answer does not work, we will consider it as a NO.")

# 3rd product.
question = input("\nWould you like to buy any Portal Fluid (yes/no)? ")

if question == "Yes" or question == "yes" or question == "Y" or question == "y":
    unit = float(input("How many gallons of Portal Fluid  would you like to buy? "))

    if unit < 3:
        money = money + (unit * 8)

    elif unit < 7:
        money = money + (unit * 7)

    else:
        money = money + (unit * 6)

elif question == "No" or question == "no" or question == "N" or question == "n":
    print("Let's move to the next product")

# It is necessary to understand that clients could not answer the way I want.
else:
    print("ERROR! Your answer does not work, we will consider it as a NO.")

# When all the conditions finish, it displays how much money costs everything.
print("\nYour final total is " + str(money) + " dollars.")

print("\nThanks for visiting Citadel's Gift Shop! We hope to see you again.")
