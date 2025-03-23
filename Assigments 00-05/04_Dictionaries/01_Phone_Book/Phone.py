def read_phone_numbers():
    """
    Collects names and numbers from the user and stores them in a dictionary (phonebook).
    Ensures that phone numbers are valid and names are not empty.
    Returns the phonebook dictionary.
    """
    phonebook = {}

    while True:
        name = input("Enter name (or press Enter to finish): ").strip()
        if name == "":
            break

        number = input(f"Enter number for {name}: ").strip()
        
        # Validate number input (should contain only digits)
        if not number.isdigit():
            print(" Invalid number! Please enter a valid numeric phone number.")
            continue
        
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Displays all names and numbers stored in the phonebook.
    """
    if not phonebook:
        print(" Phonebook is empty!")
        return

    print("\n📞 Phonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allows the user to search for a number by entering a name.
    The lookup is case-insensitive.
    """
    while True:
        name = input(" Enter name to lookup (or press Enter to exit): ").strip()
        if name == "":
            break

        # Case insensitive lookup
        matching_name = next((key for key in phonebook if key.lower() == name.lower()), None)

        if matching_name:
            print(f" {matching_name}'s number: {phonebook[matching_name]}")
        else:
            print(f" {name} is not in the phonebook.")


def main():
    """
    Main function that provides an interactive menu for the phonebook.
    """
    phonebook = read_phone_numbers()
    
    while True:
        print("\n📱 Phonebook Menu:")
        print("1. View all contacts")
        print("2. Lookup a number")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ").strip()

        if choice == "1":
            print_phonebook(phonebook)
        elif choice == "2":
            lookup_numbers(phonebook)
        elif choice == "3":
            print(" Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")


# Python boilerplate.
if __name__ == '__main__':
    main()
