import random

# List of different sentence starters for variety
SENTENCE_TEMPLATES = [
    "Panaversity is fun. I learned to program and used Python to make my {adj} {noun} {verb}!",
    "One day, a {adj} {noun} decided to {verb} in the middle of the night!",
    "Have you ever seen a {adj} {noun} that can {verb}? Now you have!",
    "The {adj} {noun} loves to {verb} whenever nobody is watching!",
    "In a world where {adj} {noun}s rule, everyone must {verb} to survive!",
    "A {adj} {noun} once tried to {verb}, but it didn’t go as planned...",
    "They say a {adj} {noun} can {verb} better than anyone else!",
    "Why did the {adj} {noun} decide to {verb}? Nobody knows!",
    "Every morning, the {adj} {noun} wakes up and starts to {verb} immediately.",
    "If you ever meet a {adj} {noun}, be sure to {verb} as quickly as possible!",
    "The {adj} {noun} went on an adventure to {verb} across the lands!",
    "Never underestimate a {adj} {noun} who knows how to {verb}!"
]

def get_valid_input(prompt):
    """Ensures the user enters a valid non-empty alphabetical word."""
    while True:
        word = input(prompt).strip()
        if word.isalpha():
            return word
        print("Invalid input! Please enter a single word with only letters.")

def play_mad_libs():
    """Prompts the user for words and generates a fun sentence."""
    print("\n Welcome to Mad Libs! \n")

    while True:
        # Get user input
        adjective = get_valid_input("Please type an adjective and press enter: ")
        noun = get_valid_input("Please type a noun and press enter: ")
        verb = get_valid_input("Please type a verb and press enter: ")

        # Choose a random sentence template and insert user words
        sentence = random.choice(SENTENCE_TEMPLATES).format(adj=adjective, noun=noun, verb=verb)
        
        # Print the result
        print("\n Your Mad Libs story: ")
        print(sentence + "\n")

        # Ask if the user wants to play again
        again = input("Do you want to create another Mad Lib? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye! Thanks for playing! ")
            break

# Runs the program
if __name__ == '__main__':
    play_mad_libs()
