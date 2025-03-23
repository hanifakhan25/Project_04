def get_fruit_quantities(fruits):
    """
    Asks the user how many of each fruit they want to buy.
    Ensures valid numeric input (non-negative integers).
    Returns a dictionary of fruit quantities.
    """
    quantities = {}

    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ").strip()

                # Ensure input is numeric and non-negative
                if not amount_bought.isdigit():
                    print(" Please enter a valid non-negative integer.")
                    continue

                amount_bought = int(amount_bought)
                quantities[fruit_name] = amount_bought
                break  # Valid input, exit loop

            except ValueError:
                print("⚠️ Invalid input. Please enter a whole number.")

    return quantities


def calculate_total_cost(fruits, quantities):
    """
    Calculates the total cost based on fruit prices and user-selected quantities.
    Returns the total cost as a float.
    """
    total_cost = sum(fruits[fruit] * quantities[fruit] for fruit in fruits)
    return total_cost


def main():
    """
    Main function that handles user input, calculates total cost, and prints the result.
    """
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    quantities = get_fruit_quantities(fruits)
    total_cost = calculate_total_cost(fruits, quantities)

    print(f"\n Your total is **${total_cost:.2f}**")  # Formats to two decimal places


# Python boilerplate
if __name__ == '__main__':
    main()
