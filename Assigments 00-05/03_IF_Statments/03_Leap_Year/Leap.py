def is_leap_year(year):
    """
    Determines whether a given year is a leap year based on the Gregorian calendar rules.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    """
    Prompts the user to enter a year and prints whether it's a leap year or not.
    """
    try:
        year = int(input("Please input a year: "))
        
        if is_leap_year(year):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    
    except ValueError:
        print("Invalid input! Please enter a valid year.")

if __name__ == '__main__':
    main()
