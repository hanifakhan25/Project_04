from collections import Counter

def get_user_numbers():
    """
    Collect numbers from the user and store them in a list.
    Stops when the user enters a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":  # Stop if the input is blank
            break

        try:
            num = int(user_input)  # Convert input to integer
            user_numbers.append(num)
        except ValueError:
            print(" Invalid input. Please enter a valid integer.")

    return user_numbers

def count_nums(num_lst):
    """
    Uses the Counter class to count occurrences of numbers in the list.
    """
    return Counter(num_lst)

def print_counts(num_dict):
    """
    Prints the count of each unique number in a readable format.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} time(s).")

def main():
    """
    Main function that collects user input, counts occurrences, and prints results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Python boilerplate.
if __name__ == '__main__':
    main()
