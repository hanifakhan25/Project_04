import random

N_NUMBERS = 10  # Number of random numbers to generate
MIN_VALUE = 1    # Minimum value for random numbers
MAX_VALUE = 100  # Maximum value for random numbers

def main():
    """
    Prints N_NUMBERS random integers between MIN_VALUE and MAX_VALUE.
    """
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))  # Generate and print a random number

if __name__ == '__main__':
    main()
