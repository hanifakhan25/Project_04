def main():
    #taking input
    print()
num = float(input("Type a Number To See Its Square: "))
#Square of the inputted number
Square = num **2
#check if its even or odd (Additional )
 # Check if the number and its square are even or odd
num_type = "even" if num % 2 == 0 else "odd"
square_type = "even" if Square % 2 == 0 else "odd"
# print output
print(f"{num} Squared is {Square}")
print(f"The number {num} is {num_type}.")
print(f"The square {Square} is {square_type}.")

if __name__ == '__main__':
        main()