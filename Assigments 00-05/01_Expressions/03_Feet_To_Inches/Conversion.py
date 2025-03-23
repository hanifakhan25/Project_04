# conversion 1 foot = 12 inches 
INCHES_IN_FOOT = 12
def main():
    while True :
     try:
            feet = float(input("Enter Number Of Feet : "))
            inches = feet * INCHES_IN_FOOT
        # Correct pluraliz ation: "foot" for 1, "feet" for others
            unit = "foot" if feet == 1 else "feet"
        # print the result
            print(f"{feet} {unit} is {inches} inches!\n")
     except ValueError:
            print("Invalid input! Please enter a number.")
# run program
if __name__ == '__main__':
     main()

          