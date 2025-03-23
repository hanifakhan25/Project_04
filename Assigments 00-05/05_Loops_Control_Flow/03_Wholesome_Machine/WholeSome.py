AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    """
    Continuously prompts the user to type a specific affirmation until they do so correctly.
    """
    print(f"Please type the following affirmation: \n{AFFIRMATION}")

    while True:
        user_input = input().strip()  # Get input and remove unnecessary spaces

        if user_input == AFFIRMATION:
            print(" That's right! Keep believing in yourself! ")
            break
        else:
            print("❌ That was not the affirmation. Try again!")
            print(f"\nPlease type the following affirmation: \n{AFFIRMATION}")

if __name__ == '__main__':
    main()
