PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    """
    Asks the user for their age and determines if they can vote in the fictional countries
    Peturksbouipo, Stanlau, and Mayengua based on their voting ages.
    """
    try:
        user_age = int(input("How old are you? "))
        
        countries = {
            "Peturksbouipo": PETURKSBOUIPO_AGE,
            "Stanlau": STANLAU_AGE,
            "Mayengua": MAYENGUA_AGE
        }
        
        for country, age in countries.items():
            if user_age >= age:
                print(f"You can vote in {country} where the voting age is {age}.")
            else:
                print(f"You cannot vote in {country} where the voting age is {age}.")
    
    except ValueError:
        print("Invalid input! Please enter a valid age.")

if __name__ == '__main__':
    main()
