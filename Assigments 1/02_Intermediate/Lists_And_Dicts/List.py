def print_list(lst):
    """Prints the list in a clean format."""
    print(", ".join(lst))

def main():
    """
    Creates a list of fruits, prints its length, adds a new fruit, and displays the updated list.
    """
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    print(f"Initial list length: {len(fruit_list)}")

    # Add 'mango' to the end of the list
    fruit_list.append('mango')

    print("Updated list:")
    print_list(fruit_list)

if __name__ == '__main__':
    main()

