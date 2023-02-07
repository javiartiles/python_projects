def main():
    incomes_planets = []
    incomes_galaxies = []
    total_income = 0
    total_planets = 0

    print("Welcome to the Galaxy analyzer!\n")

    repeat = 'yes'
    while repeat.lower().strip() == 'yes':
        number_of_galaxies = int(input("How many galaxies would you like to analyze? "))
        for i in range(1, number_of_galaxies + 1):
            planets_in_galaxy = int(input(f"\nHow many planets are in galaxy {i}: "))
            income_g = 0
            for j in range(1, planets_in_galaxy + 1):
                income_p = int(input(f"What was planet {j}'s income last year? "))
                income_g += income_p
                total_planets += 1
                incomes_planets.append(income_p)

            total_income += income_g
            incomes_galaxies.append(income_g/planets_in_galaxy)

        income_distribution = [0] * 5
        for income in incomes_galaxies:
            if income < 20000:
                income_distribution[0] += 1
            elif 20000 <= income < 40000:
                income_distribution[1] += 1
            elif 40000 <= income < 60000:
                income_distribution[2] += 1
            elif 60000 <= income < 80000:
                income_distribution[3] += 1
            else:
                income_distribution[4] += 1

        print("\nNumber of planets:", total_planets)
        print("Planets per galaxy:", total_planets/number_of_galaxies)
        print("\nAverage planetary income:", total_income/total_planets)
        print("Average galactic income:", total_income/number_of_galaxies)

        print("\nIncome distribution:")
        print("Less than $20,000:", income_distribution[0], "galaxy(s)")
        print("At least $20,000 but less than $40,000:", income_distribution[1], "galaxy(s)")
        print("At least $40,000 but less than $60,000:", income_distribution[2], "galaxy(s)")
        print("At least $60,000 but less than $80,000:", income_distribution[3], "galaxy(s)")
        print("At least $80,000:", income_distribution[4], "galaxy(s)")

        repeat = input("\nWould you like to analyze another quadrant (yes/no)? ")
        if repeat.lower().strip() == 'no':
            print("Thanks for using the Galaxy Analyzer progam! See you again.")
        else:
            print("ERROR! Your answer does not work, we will consider it as a NO.")

if __name__ == '__main__':
    main()
