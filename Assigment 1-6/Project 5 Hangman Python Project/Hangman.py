import os
import random
import pygame
import pyttsx3
import time

# Initialize AI Voice
tts_engine = pyttsx3.init()

# 🔊 Initialize Pygame for Sound Effects & Music
pygame.init()


# 📂 Define Sound Folder Paths
SOUND_FOLDER = r"C:\Users\umar\Desktop\Project04_ Assigments\Assigments 1- 6\Project 5 Hangman Python Project\Sounds"

# 🎵 List of Random Background Music Files
MUSIC_FILES = [
    "Company.mp3",
    "Payphone.mp3", 
    "Sugar-Crash.mp3" ,
    "Lauv-I-Like-Me-Better.mp3" ,
    "Sickick .mp3",
    "24kGoldn.mp3"
]

# 🎶 Choose a Random Music File
random_music = os.path.join(SOUND_FOLDER, random.choice(MUSIC_FILES))

# 🔊 Load & Play Music
if os.path.exists(random_music):
    pygame.mixer.music.load(random_music)
    pygame.mixer.music.set_volume(0.3)  # Lower background music volume
    pygame.mixer.music.play(-1)  # Loop the Music Forever
    print(f"🎵 Now Playing: {random_music}")
else:
    print("⚠️ Background music file not found! Skipping music playback.")

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# ASCII Hangman Stages
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    ========= GAME OVER
    """
]

# Word List
WORDS = ["python", "hangman", "developer", "gaming", "cyberpunk", "skateboard", "algorithm", "vibing", "streamer", "legend", "laptop"]

# Gen Z Roasts
ROASTS = [
    "Bro really thought they could win 💀.",
    "Nah fam, that was mad embarrassing 🤡.",
    "That was an L move, fr fr. 📉",
    "Bruh, even a goldfish has better memory than you. 🐠",
    "Skill issue detected. 🚨 Try again, goofy."
]

# Gen Z Praise
PRAISES = [
    "W move! You really built different 🏆.",
    "Certified GOAT behavior 🐐.",
    "Nah, you straight up cracked at this game. 🎯",
    "Lowkey that was impressive af. 🔥",
    "W gamer, W vibes, W everything. 🚀"
]

def get_random_word():
    return random.choice(WORDS)

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6
    hidden_word = ["_" for _ in word]

    print("🎮 Welcome to Gen Z Hangman!")
    speak("Welcome to Gen Z Hangman! Get ready!")
    time.sleep(1)

    while attempts > 0:
        print(HANGMAN_STAGES[6 - attempts])
        print("Word: ", " ".join(hidden_word))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("🚨 Invalid input. Enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
            print("🔥 Nice! You got a letter.")
        else:
            attempts -= 1
            print("❌ Wrong guess!")

        if "_" not in hidden_word:
            print("✅ YOU WON! Word was:", word)
            praise = random.choice(PRAISES)
            print(f"🏆 {praise}")
            speak(praise)
            return

    print(HANGMAN_STAGES[-1])
    print("☠️ YOU LOST! The word was:", word)
    roast = random.choice(ROASTS)
    print(f"💀 {roast}")
    speak(roast)

if __name__ == "__main__":
    play_hangman()
