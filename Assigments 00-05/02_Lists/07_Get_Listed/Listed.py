def main():
    """
    Continuously asks the user to enter values which are added one by one into a list.
    When the user presses enter without typing anything, prints the list.
    """
    lst = []  # Initialize an empty list
    
    print("Enter values (press Enter to stop):")
    
    while True:
        val = input("-> ").strip()
        if val == "":  # Stop when input is empty
            break
        lst.append(val)  # Add input to list
    
    print("Here's the list:", lst)

if __name__ == '__main__':
    main()
