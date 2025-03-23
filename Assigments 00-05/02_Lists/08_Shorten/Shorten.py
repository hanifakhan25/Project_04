MAX_LENGTH = 3

def shorten(lst):
    """
    Removes elements from the end of lst until it is MAX_LENGTH items long.
    Prints each removed element. If lst is already shorter, it remains unchanged.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"Removed: {last_elem}")

def get_lst():
    """
    Prompts the user to enter elements for the list, one at a time, until they press enter.
    Returns the list with valid inputs.
    """
    lst = []
    print("Enter elements for the list (press Enter to stop):")
    
    while True:
        elem = input("-> ").strip()
        if elem == "":
            break
        lst.append(elem)
    
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("Final list:", lst)

if __name__ == '__main__':
    main()
