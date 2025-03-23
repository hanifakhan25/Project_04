NUM_EVEN_NUMBERS = 20  # Constant for the number of even numbers to print

def main():
    """
    Prints the first NUM_EVEN_NUMBERS even numbers.
    """
    even_numbers = range(0, NUM_EVEN_NUMBERS * 2, 2)  # Generate even numbers
    print("\n".join(map(str, even_numbers)))  # Print them neatly

if __name__ == "__main__":
    main()
