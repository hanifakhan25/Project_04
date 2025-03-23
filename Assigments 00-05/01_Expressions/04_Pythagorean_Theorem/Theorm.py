import math  # Import math library to use sqrt()

def calculate_hypotenuse():
    """Prompts user for two perpendicular sides and calculates the hypotenuse."""
    while True:
        try:
            # Get valid positive side lengths
            ab = float(input("Enter the length of AB: "))
            ac = float(input("Enter the length of AC: "))

            if ab <= 0 or ac <= 0:
                print("Side lengths must be positive numbers! Try again.\n")
                continue

            # Calculate the hypotenuse using the Pythagorean theorem
            bc = math.sqrt(ab**2 + ac**2)

            # Print the result with proper formatting
            print(f"The length of BC (the hypotenuse) is: {bc:.2f}\n")

        except ValueError:
            print("Invalid input! Please enter numerical values.\n")

def main():
    while True:
        calculate_hypotenuse()
        again = input("Do you want to calculate another hypotenuse? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

# Ensures the script runs when executed
if __name__ == '__main__':
    main()
