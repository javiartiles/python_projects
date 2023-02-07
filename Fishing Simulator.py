# ------------------------------------ #
# Javier Artiles Manrique de Lara
# MSBA 502 - Analytics Programming I
# Homework 3: Fishing Simulator
# ------------------------------------ #

import random as rand

repeat = "yes"

# For this programme I will create functions for each fish.

# Losbter function:

def lobster():
    x = rand.randrange(1, 11)

    if x == 1:
        money = 125000

    elif 2 <= x <= 8:
        money = 50000

    else:
        money = -10000

    return money


# Kelp function:

def kelp():
    x = rand.randrange(1, 6)

    if 1 <= x <= 3:
        money = 45000

    else:
        money = -10000

    return money


# Urchin function:

def urchin():
    x = rand.randrange(1, 5)

    if 1 <= x <= 3:
        money = 30000

    else:
        money = -5000

    return money


while repeat.lower().strip() == "yes":

    total = 0
    annual = 0
    year = 0
    fish = ['Lobster', 'Bullwhip Kelp', 'Urchin']
    years_profit = 0

    # While loop to repeat until one of the stopping conditions are met
    while 0 <= total < 325000 and years_profit < 5:

        fishing_year = year % 4

        if fishing_year == 0:
            annual_profit = lobster()

        elif fishing_year == 1 | fishing_year == 3:
            annual_profit = kelp()

        else:
            annual_profit = urchin()

        total += annual_profit

        print(f"** Year {year + 1} **")
        print(f"\nFocus this year: {fish[fishing_year]}")
        print(f"This year's profit (or loss): ${annual_profit}")
        print(f"Total profit (or loss): ${total}\n")

        year += 1

        if annual_profit > 0:
            years_profit += 1

        else:
            consecutive_years_profit = 0

    if total <= 0:
        print(
            "The total profit is negative at year-end."
            "The owner will close the fishing operation and look for a new business venture.\n")

    if total >= 325000:
        print("The total profit reaches at least $325,000 at year-end. The owner will happily retire.\n")

    if years_profit >= 5:
        print("There are five consecutive years of positive profit. The manager will happily retire.\n")

    repeat = input("\nWould you like to run another simulation (yes/no)? ")