def main():
    """
    Asks the user for a number, then doubles it repeatedly until it reaches or exceeds 100.
    """
    while True:
        try:
            curr_value = int(input("Enter a positive number: ").strip())

            if curr_value <= 0:
                print("⚠️ Please enter a positive number greater than 0.")
                continue  # Ask again

            break  # Valid input, exit loop

        except ValueError:
            print("⚠️ Invalid input. Please enter a valid integer.")

    while curr_value < 100:
        curr_value *= 2
        print(curr_value)  # Print the doubled value

if __name__ == '__main__':
    main()
