def divide_numbers():
    """Prompts the user for two numbers and performs integer division with error handling."""
    while True:
        try:
            dividend = int(input("Please enter an integer to be divided: "))
            divisor = int(input("Please enter an integer to divide by: "))

            if divisor == 0:
                print("Error: Division by zero is not allowed. Try again.\n")
                continue

            quotient = dividend // divisor  # Integer division
            remainder = dividend % divisor  # Remainder of division

            print(f"The result of this division is {quotient} with a remainder of {remainder}\n")

        except ValueError:
            print("Invalid input! Please enter whole numbers only.\n")

def main():
    while True:
        divide_numbers()
        again = input("Do you want to perform another division? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

# Ensures the script runs when executed
if __name__ == '__main__':
    main()
