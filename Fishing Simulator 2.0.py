import random as rand

def lobster():
    x = rand.randrange(1, 11)
    if x == 1:
        return 125000
    elif 2 <= x <= 8:
        return 50000
    else:
        return -10000

def kelp():
    x = rand.randrange(1, 6)
    if 1 <= x <= 3:
        return 45000
    else:
        return -10000

def urchin():
    x = rand.randrange(1, 5)
    if 1 <= x <= 3:
        return 30000
    else:
        return -5000

def simulate_fishing_operation(total=0, year=0, years_profit=0):
    fish = ['Lobster', 'Bullwhip Kelp', 'Urchin']

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
            years_profit = 0

    if total <= 0:
        print("The total profit is negative at year-end."
              "The owner will close the fishing operation and look for a new business venture.\n")
    if total >= 325000:
        print("The total profit reaches at least $325,000 at year-end. The owner will happily retire.\n")
    if years_profit >= 5:
        print("There are five consecutive years of positive profit. The manager will happily retire.\n")

def run_simulation():
    repeat = "yes"
    while repeat.lower().strip() == "yes":
        simulate_fishing_operation()
        repeat = input("\nWould you like to run another simulation (yes/no)? ")

if __name__ == '__main__':
    run_simulation()
