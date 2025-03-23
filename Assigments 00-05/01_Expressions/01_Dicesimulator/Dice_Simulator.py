
import random  # Import random library for dice simulation

# Constant for number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their values and total.
    Demonstrates local variable scope.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled dice: {die1} and {die2} → Total: {total}")

def main():
    die1 = 10  # Local variable inside main()
    print(f"Before rolling, die1 in main() = {die1}")

    # Roll dice three times
    for _ in range(3):
        roll_dice()

    # `die1` inside main() remains unchanged
    print(f"After rolling, die1 in main() = {die1}")

# Ensures the script runs when executed
if __name__ == '__main__':
    main()
