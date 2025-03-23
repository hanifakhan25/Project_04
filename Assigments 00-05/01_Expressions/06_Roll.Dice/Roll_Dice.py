import random
import time  # For animation effect

def roll_dice(sides=6):
    """Simulates rolling two dice and returns their values and total."""
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    total = die1 + die2

    return die1, die2, total

def dice_animation():
    """Simulates a rolling dice animation."""
    print("Rolling dice", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def main():
    print(" Welcome to the Dice Roller! \n")

    while True:
        try:
            sides = int(input("Enter the number of sides per die (default is 6): ") or 6)
            if sides < 2:
                print("Dice must have at least 2 sides! Try again.\n")
                continue
            
            dice_animation()  # Fun rolling effect
            die1, die2, total = roll_dice(sides)

            # Display results
            print(f" Dice have {sides} sides each.")
            print(f" First die: {die1}")
            print(f"Second die: {die2}")
            print(f"Total of two dice: {total}\n")

            # Special cases
            if die1 == die2:
                print(" You rolled a double! \n")
            if die1 == 6 and die2 == 6:
                print("Boxcars! Two sixes! \n")

            # Ask to roll again
            again = input("Roll again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thanks for playing! 🎲 Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.\n")

# Runs the program
if __name__ == '__main__':
    main()
