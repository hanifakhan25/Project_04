def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])

# Function to get a list from user input
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    if lst:  # Ensuring the list is not empty (though guaranteed by the problem statement)
        get_first_element(lst)
    else:
        print("The list is empty!")

if __name__ == '__main__':
    main()
