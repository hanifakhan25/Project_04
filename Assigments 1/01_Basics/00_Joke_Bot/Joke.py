import random

PROMPT = "What do you want? "
SORRY = "Sorry, I only tell jokes. 🤷‍♂️"

JOKES = [
    "Here is a joke for you! 🤖 Sophia is heading out to the grocery store. "
    "A programmer tells her: get a liter of milk, and if they have eggs, get 12. "
    "Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: "
    "'because they had eggs' 😆",

    "Why do programmers prefer dark mode? 🖥️ Because the light attracts bugs! 🐞😂",

    "A SQL query walks into a bar, walks up to two tables, and asks: 'Can I join you?' 🍻🤣",

    "Why did the Python developer break up with their partner? 💔 Because they kept mutating their arguments! 🐍😂",

    "Why don’t programmers like nature? 🌳 It has too many bugs! 🐛",

    "How do you comfort a JavaScript bug? 🐞 You console it! 😆"
]

def main():
    """
    A simple joke bot that tells a random joke when the user types 'joke'.
    """
    user_input = input(PROMPT).strip().lower()  # Get input, remove spaces, and make lowercase

    if user_input == "joke":  # Only responds if exactly "joke" is entered
        print(random.choice(JOKES))  # Selects and prints a random joke
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
