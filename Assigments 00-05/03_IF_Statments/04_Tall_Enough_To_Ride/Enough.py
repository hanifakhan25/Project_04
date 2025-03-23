MINIMUM_HEIGHT = 50  # Minimum height requirement

def check_height():
    """
    Continuously asks the user for their height and determines if they can ride.
    Stops when the user enters an empty input.
    """
    while True:
        height = input("How tall are you? (Press Enter to exit): ")
        if height == "":
            print("Goodbye!")
            break
        
        try:
            height = float(height)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride! ")
            else:
                print("You're not tall enough to ride, but maybe next year! ")
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    check_height()

if __name__ == '__main__':
    main()
