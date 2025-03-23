import random

def main():
    """
    A simple 'Guess My Number' game where the user guesses a randomly chosen number
    between 1 and 99, with feedback on whether their guess is too high or too low.
    """
    secret_number = random.randint(1, 99)
    attempts = 0  # Counter for number of attempts
    
    print("\n I am thinking of a number between 1 and 99...")
    
    while True:
        try:
            guess = int(input("Enter a guess: ").strip())
            
            # Ensure guess is within valid range
            if guess < 1 or guess > 99:
                print(" Please enter a number between 1 and 99.")
                continue

            attempts += 1  # Increment attempt count
            
            if guess < secret_number:
                print(" Your guess is too low.")
            elif guess > secret_number:
                print(" Your guess is too high.")
            else:
                print(f" Congrats! The number was: {secret_number}")
                print(f"You guessed it in {attempts} attempt(s)!")
                break  # Exit loop when correct number is guessed
        
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 99.")

if __name__ == '__main__':
    main()
