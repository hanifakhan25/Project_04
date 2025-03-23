def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(f"The last element in the list is: {lst[-1]}")

def get_lst():
    """
    Prompts the user to enter elements for the list, one at a time, until they press enter.
    Returns the list with valid inputs.
    """
    lst = []
    print("Enter elements for the list (press Enter to stop):")
    
    while True:
        elem = input("> ").strip()
        if elem == "":
            break
        lst.append(elem)

    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()
