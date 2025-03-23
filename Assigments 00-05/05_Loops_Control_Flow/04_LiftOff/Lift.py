COUNTDOWN_START = 10  # Constant for the countdown start value

def main():
    """
    Prints a countdown from COUNTDOWN_START to 1, followed by "Liftoff!".
    """
    for i in range(COUNTDOWN_START, 0, -1):  # Count down from 10 to 1
        print(i)

    print("🚀 Liftoff!")  # Final message

if __name__ == '__main__':
    main()
