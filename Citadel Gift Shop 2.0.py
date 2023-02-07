from typing import List, Tuple

def handle_answer(answer: str) -> bool:
    """
    Check if answer is 'yes' or 'y' and return a boolean value.
    """
    return answer.lower() in ['yes', 'y']

def calculate_cost(unit: float, price_list: List[Tuple[float, float]]) -> float:
    """
    Calculate the cost of the product based on the given unit and price list.
    """
    for lower_bound, price in price_list:
        if unit < lower_bound:
            return unit * price
    return unit * price_list[-1][1]

def main():
    """
    Main function that implements the gift shop program.
    """
    money = 0
    print("Welcome to The Citadel's Gift Shop! Let's work on your order.")

    for product in [('Plumbuses', [(5, 20), (15, 17.5), (float('inf'), 15.25)]),
                   ('Meeseeks Boxes', [(10, 1.75), (18, 1.5), (float('inf'), 1.25)]),
                   ('Portal Fluid', [(3, 8), (7, 7), (float('inf'), 6)])]:
        question = input(f"\nWould you like to buy any {product[0]} (yes/no)? ")
        if handle_answer(question):
            unit = float(input(f"How many gallons of {product[0]} would you like to buy? "))
            money += calculate_cost(unit, product[1])
        elif question.lower() not in ['no', 'n']:
            raise ValueError(f"Invalid answer: {question}")

    print(f"\nYour final total is {money} dollars.")
    print("\nThanks for visiting Citadel's Gift Shop! We hope to see you again.")

if __name__ == '__main__':
    main()