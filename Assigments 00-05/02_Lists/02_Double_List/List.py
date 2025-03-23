def double_numbers(numbers: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns a new list with each number doubled.
    """
    return [num * 2 for num in numbers]  # More concise and efficient

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
    print("Welcome to the Number Doubler!\n")

    # Get numbers from the user
    numbers = get_numbers_from_user()
    
    # Double the numbers
    doubled_numbers = double_numbers(numbers)

    # Display the result
    print(f"\nOriginal list: {numbers}")
    print(f"Doubled list: {doubled_numbers} ")

if __name__ == '__main__':
    main()
