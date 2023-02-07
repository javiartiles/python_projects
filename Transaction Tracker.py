# ------------------------------------ #
# Javier Artiles Manrique de Lara
# MSBA 503 - Analytics Programming II
# Homework 4: Transaction Ledger
# ------------------------------------ #

# ----------------------- #
# Part 0: Import packages #
# ----------------------- #

import os
import csv

# ------------------------------------------------- #
# Part 1: Create functions to IMPORT and STATISTICS #
# ------------------------------------------------- #

def import_function(file):

    try:
        with open(file, 'r') as ledger:

            read_ledger = csv.reader(ledger)
            ledger_data = list(read_ledger)

        if os.path.exists("transaction_ledger.csv"):
            ledger_exist = "yes"

        else:
            ledger_exist = "no"

        # If the ledger file does not exist we need to create it
        with open("transaction_ledger.csv", "a") as new_ledger:

            write_ledger = csv.writer(new_ledger)

            # This function will add the title for the columns and the data in the new ledger file
            if ledger_exist == "no":

                columns_name = ["ID", "COMPANY NAME", "DATE", "AMOUNT", "STATUS"]
                write_ledger.writerow(columns_name)
                new_ledger_data = ledger_data

            # This function will do the same as the last one but with the existing ledger file
            else:
                with open("transaction_ledger.csv", 'r') as old_ledger:

                    new_ledger_data = []
                    old_ledger_reader = csv.reader(old_ledger)
                    old_ledger_data = list(old_ledger_reader)

                    # This loop will add new data when it is not duplicates
                    for i in range(len(ledger_data)):

                        count = 0
                        add_ledger = True

                        # This loop will check for duplicate IDs and add it if is not a duplicate
                        for j in range(len(old_ledger_data)):

                            if ledger_data[i][0] == old_ledger_data[j][0]:
                                add_ledger = False

                        if add_ledger == True:
                            new_ledger_data.append(ledger_data[i])
                            count += 1

                        else:
                            print(f"Data for ID {ledger_data[i][0]} is already in transaction records.")

            # This loop will add new records into the ledger file
            transaction_records = 0

            for k in range(len(new_ledger_data)):
                write_ledger.writerow(new_ledger_data[k])
                transaction_records += 1

            print(f"{transaction_records} transaction records successfully loaded.")

    except:
        print("Sorry, that file could not be found. Please try again.")

def statistics_function():

    try:
        with open("transaction_ledger.csv", 'r') as old_ledger:
            old_ledger_data = csv.reader(old_ledger)
            existing_data = list(old_ledger_data)
            pending = 0
            pending = float(pending)

            for i in range(1, len(existing_data), 1):
                existing_data_int = int(existing_data[i][3])
                pending += existing_data_int

            print(f"\nNumber of current transactions: {len(existing_data)-1}")
            print(f"Total amount pending: ${pending:,}")

    except:
        print("Sorry, no transaction data was loaded yet. Please try again.")

# -------------------- #
# Part 2: User prompts #
# -------------------- #

print("Welcome to the Adrek Robotics transaction tracker!\n")

repeat = "yes"

while repeat.lower().strip() == "yes":

    performance = input("What would you like to perform (import/statistics)? ").lower().strip()

    if performance == "import":
        what_file = input("Which file would you like to import? ")
        import_file = import_function(what_file)

    elif performance == "statistics":
        statistics_function()

    else:
        print("ERROR! No performance found. Please try again.")

    repeat = input("\nWould you like to run any further analyses (yes/no)? ")

else:
    print("\nERROR! That is not a correct answer")