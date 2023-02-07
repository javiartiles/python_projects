# ------------------------------------ #
# Javier Artiles Manrique de Lara
# MSBA 502 - Analytics Programming I
# Homework 2: Galaxy Analyzer
# ------------------------------------ #

# First, I create different variables for the income ranges
income_20000 = 0
income_20000_40000 = 0
income_40000_60000 = 0
income_60000_80000 = 0
income_80000 = 0

# Second, lists to storage the planets and galaxies income data
incomes_planets = []
incomes_galaxies = []

# Third, variables that storage the value the user will input
number_of_galaxies = 0
planets_in_galaxy = 0

# Last, variables that will be useful to print the additional info
income_g = 0 # Total income for each galaxy
total_income = 0 # Total income (sum of galaxies incomes)
total_planets = 0 # Sum of planets

# ------------------------------------ #
# --- Let's start with the program --- #
# ------------------------------------ #
repeat = 'yes'

print("Welcome to the Galaxy analyzer!\n")

while repeat.lower().strip() == 'yes':

    number_of_galaxies = int(input("How many galaxies would you like to analyze? "))

    # As the user could want to analyze more than 1 galaxies, I start with a loop
    # that will be running depending on the user input
    for i in range(1, number_of_galaxies + 1):

        planets_in_galaxy = int(input(f"\nHow many planets are in galaxy {i}: "))

        # This second loop is created in order to take into account that there may be more than 1 planet per galaxy
        for j in range(1, planets_in_galaxy + 1):
            # Variable that storages the income of each planet
            income_p = int(input(f"What was planet {j}'s income last year? "))

            income_g += income_p
            total_planets += 1
            incomes_planets.append(income_p)

        total_income += income_g
        incomes_galaxies.append(income_g/planets_in_galaxy)

    # This new loop will storage the number of galaxies depending on the income range
    for k in range(0, number_of_galaxies):

        if incomes_galaxies[k] < 20000:
            income_20000 += 1

        elif 20000 <= incomes_galaxies[k] < 40000:
            income_20000_40000 += 1

        elif 40000 <= incomes_galaxies[k] < 60000:
            income_40000_60000 += 1

        elif 60000 <= incomes_galaxies[k] < 80000:
            income_60000_80000 += 1

        else:
            income_80000 += 1

    # Let's print all the information related with the variables created
    print("\nNumber of planets:", total_planets)
    print("Planets per galaxy:", total_planets/number_of_galaxies)
    print("\nAverage planetary income:", total_income/total_planets)
    print("Average galactic income:", total_income/number_of_galaxies)

    print(f"\nIncome distribution:\nLess than $20,000: {income_20000} galaxy(s)")
    print(f"At least $20,000 but less than $40,000: {income_20000_40000} galaxy(s)")
    print(f"At least $40,000 but less than $60,000: {income_40000_60000} galaxy(s)")
    print(f"At least $60,000 but less than $80,000: {income_60000_80000} galaxy(s)")
    print(f"At least $80,000: {income_80000} galaxy(s)")

    # Need to ask the user to analyze more galaxies or not
    repeat = input("\nWould you like to analyze another quadrant (yes/no)? ")

    if repeat.lower().strip() == 'no':
        print("Thanks for using the Galaxy Analyzer progam! See you again.")
    else:
        # It is necessary to understand that clients could not answer the way I want
        print("ERROR! Your answer does not work, we will consider it as a NO.")
