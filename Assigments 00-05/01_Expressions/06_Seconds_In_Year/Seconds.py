# Constants for time calculations
DAYS_IN_YEAR = 365
DAYS_IN_LEAP_YEAR = 366
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def calculate_seconds(days_per_year):
    """Calculates the number of seconds in a year (normal or leap year)."""
    return days_per_year * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE

def main():
    print(" Welcome to the Year Seconds Calculator! \n")

    while True:
        # Ask user if they want to calculate for a leap year or normal year
        year_type = input("Do you want to calculate for a leap year? (yes/no): ").strip().lower()
        
        if year_type == "yes":
            total_seconds = calculate_seconds(DAYS_IN_LEAP_YEAR)
            print(f"\nThere are {total_seconds:,} seconds in a leap year!\n")
        elif year_type == "no":
            total_seconds = calculate_seconds(DAYS_IN_YEAR)
            print(f"\nThere are {total_seconds:,} seconds in a normal year!\n")
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.\n")
            continue

        # Ask if they want to run again
        again = input("Would you like to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye! ")
            break

# Ensures the script runs when executed
if __name__ == '__main__':
    main()
