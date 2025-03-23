MAX_FIB = 10_000  # Max Fibonacci value (readability with underscores)

def main():
    """
    Generates and prints Fibonacci numbers up to MAX_FIB.
    """
    a, b = 0, 1  # Start of Fibonacci sequence
    fib_numbers = []  # Store values for better output formatting

    while a <= MAX_FIB:
        fib_numbers.append(str(a))  # Store Fibonacci number as string
        a, b = b, a + b  # Update values

    print("\n".join(fib_numbers))  # Print all Fibonacci numbers, one per line

if __name__ == '__main__':
    main()
