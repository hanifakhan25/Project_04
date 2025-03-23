def main():
    # Ask user for input
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print(f"Temperature: {fahrenheit:.1f}F = {celsius:.6f}C")


# This calls the main function when the program runs
if __name__ == '__main__':
    main()
