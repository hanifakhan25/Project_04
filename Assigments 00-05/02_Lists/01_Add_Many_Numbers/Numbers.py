def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns their sum.
    """
    return sum(numbers)  # More efficient than manual looping

def get_numbers_from_user():
    """
    Prompts the user to enter numbers separated by spaces and returns them as a list.
    Handles invalid input gracefully.
    """
    while True:
        try:
            user_input = input("Enter numbers separated by spaces: ")
            numbers = list(map(int, user_input.split()))
            return numbers
        except ValueError:
            print("Invalid input! Please enter only numbers separated by spaces.")

def main():
    print(" Welcome to the Sum Calculator!\n")

    # Get numbers from the user
    numbers = get_numbers_from_user()
    
    # Calculate sum
    sum_of_numbers = add_many_numbers(numbers)

    # Display the result
    print(f"\nThe sum of {numbers} is: {sum_of_numbers} ")

if __name__ == '__main__':
    main()
