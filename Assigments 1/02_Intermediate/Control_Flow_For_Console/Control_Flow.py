import random

NUM_ROUNDS = 5  # Number of rounds in the game

def get_valid_input():
    """
    Ensures the user enters either 'higher' or 'lower'.
    """
    while True:
        user_input = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if user_input in ["higher", "lower"]:
            return user_input
        print("⚠️ Please enter either 'higher' or 'lower'.")

def play_round(round_num):
    """
    Plays a single round of the High-Low game.
    Returns 1 if the player wins, 0 otherwise.
    """
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"\nRound {round_num}")
    print(f"Your number is {user_number}")

    guess = get_valid_input()

    if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"✅ You were right! The computer's number was {computer_number}")
        return 1  # Player earns a point
    else:
        print(f"❌ Aww, that's incorrect. The computer's number was {computer_number}")
        return 0  # No point earned

def main():
    """
    Runs the full High-Low game for NUM_ROUNDS rounds.
    """
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # Player's score

    for round_num in range(1, NUM_ROUNDS + 1):
        score += play_round(round_num)
        print(f"Your score is now {score}\n")

    # Ending messages based on score
    print("Thanks for playing! ")

    if score == NUM_ROUNDS:
        print(" Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print(" Good job, you played really well!")
    else:
        print("🔄 Better luck next time!")

if __name__ == '__main__':
    main()
