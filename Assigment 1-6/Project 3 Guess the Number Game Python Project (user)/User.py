import random
import time
import pyttsx3  # Text-to-Speech
import tkinter as tk
from tkinter import messagebox
import pygame  # For Sound Effects & Background Music
import speech_recognition as sr  # Voice Recognition
import os
import json

# 🔊 Initialize Pygame for Sound Effects & Music
pygame.init()


# 📂 Define Sound Folder Paths
SOUND_FOLDER = r"C:\Users\umar\Desktop\Project04_ Assigments\Assigments 1- 6\Project 3 Guess the Number Game Python Project (user)\Sounds"

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


# 🎙️ Initialize Text-to-Speech Engine
tts_engine = pyttsx3.init()
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_voice_input():
    """Capture voice input and return the text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

def save_score(player, score):
    """Save scores to a file."""
    scores = {}
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as file:
            scores = json.load(file)
    scores[player] = max(scores.get(player, 0), score)
    with open("scores.json", "w") as file:
        json.dump(scores, file)

def display_leaderboard():
    """Display top scores."""
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as file:
            scores = json.load(file)
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        print("🏆 Leaderboard:")
        for player, score in sorted_scores:
            print(f"{player}: {score}")
    else:
        print("No scores recorded yet.")

def guess(x, player):
    """Let the player guess a random number between 1 and x."""
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0
    start_time = time.time()
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        attempts += 1
        if guess < random_number:
            print('Too low! Try again.')
            speak('Too low! Try again.')
        elif guess > random_number:
            print('Too high! Try again.')
            speak('Too high! Try again.')
    end_time = time.time()
    score = max(100 - attempts * 5, 0) + max(100 - int(end_time - start_time), 0)
    print(f'Congrats {player}! You guessed {random_number} correctly in {attempts} tries! Score: {score}')
    speak(f'Congrats {player}! You guessed {random_number} correctly!')
    save_score(player, score)

def hardcore_mode(x, player):
    """Hardcore mode: limited attempts."""
    random_number = random.randint(1, x)
    attempts_left = 5
    while attempts_left > 0:
        guess = int(input(f'Guess a number (Attempts left: {attempts_left}): '))
        attempts_left -= 1
        if guess == random_number:
            print(f'You got it! The number was {random_number}. 🎉')
            speak('You got it!')
            return
        elif guess < random_number:
            print('Too low!')
        else:
            print('Too high!')
    print(f'Game Over! The number was {random_number}. 😢')
    speak(f'Game Over! The number was {random_number}.')

def gui_mode():
    """GUI version of the game using Tkinter."""
    def submit_guess():
        user_guess = int(entry.get())
        if user_guess < target_number:
            messagebox.showinfo("Result", "Too low! Try again.")
        elif user_guess > target_number:
            messagebox.showinfo("Result", "Too high! Try again.")
        else:
            messagebox.showinfo("Winner!", "Congratulations! You guessed correctly!")
            root.quit()
    target_number = random.randint(1, 100)
    root = tk.Tk()
    root.title("Guess the Number Game")
    tk.Label(root, text="Enter your guess (1-100):").pack()
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root, text="Submit", command=submit_guess).pack()
    root.mainloop()
def computer_guess(x):
    """Let the computer guess the player's number using binary search with AI-like behavior."""
    print(f"\nThink of a number between 1 and {x}. The computer will try to guess it! 🤖🔢")
    speak(f"Think of a number between 1 and {x}. I will try to guess it!")

    low, high = 1, x
    feedback = ''
    attempts = 0
    difficulty = input("\nChoose difficulty - Easy (E), Medium (M), Hard (H): ").lower()
    
    max_attempts = {'e': 15, 'm': 10, 'h': 7}.get(difficulty, 10)  # Default to Medium if invalid input
    
    while feedback != 'c' and attempts < max_attempts:
        guess = (low + high) // 2  # Binary Search (Smartest way)
        attempts += 1
        
        ai_responses = [
            f"Is it {guess}? 🤔",
            f"I'm feeling lucky... is it {guess}?",
            f"My guess is {guess}. Am I right?",
            f"Could it be {guess}? What do you think?"
        ]
        
        response = random.choice(ai_responses)
        print("\n" + response)
        speak(response)
        
        feedback = input("\nToo high (H), too low (L), or correct (C)? ").strip().lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("⚠️ Invalid input! Please enter H (high), L (low), or C (correct).")

        # 🚨 Contradiction check
        if low > high:
            print("\n⚠️ Oops! Your responses are contradictory. Restarting...")
            speak("Hmm, something seems wrong. Let's try again.")
            return  # Restart game if contradiction is detected

    if feedback == 'c':
        print(f"\n🎉 Yay! I guessed your number {guess} in {attempts} tries! 🚀")
        speak(f"Haha! I guessed your number {guess} in {attempts} tries!")
       # play_sound("win_sound.mp3")  # Play success sound
    else:
        print("\n😢 I ran out of attempts! You win!")
        speak("Oh no! I ran out of attempts. You win this time!")
       # play_sound("fail_sound.mp3")  # Play failure sound

    # 🔄 Auto Restart Option
    restart = input("\nDo you want to play again? (Y/N): ").lower()
    if restart == 'y':
        computer_guess(x)
    else:
        print("Thanks for playing! Goodbye!")
        speak("Thanks for playing! Goodbye!")
def main():
    """Main function to choose game mode."""
    print("Welcome to the Ultimate Guess the Number Game!")
    print("1. Player Guesses")
    print("2. Hardcore Mode")
    print("3. GUI Mode")
    print("4. Leaderboard")
    print("5.Computer guess")
    print("6. Voice Command Mode")
    mode = input("Enter your choice (1-6): ")
    
    max_value = int(input("Enter the max number for guessing range: "))
    if mode in ['1', '2']:
        player = input("Enter your name: ")
        max_value = int(input("Enter max number: "))
        if mode == '1':
            guess(max_value, player)
        elif mode == '2':
            hardcore_mode(max_value, player)
    elif mode == '3':
        gui_mode()
    elif mode == '4':
        display_leaderboard()
    elif mode == '5':
        computer_guess(max_value)
    elif mode == '6':
        print("Say 'start' to play!")
        command = get_voice_input()
        if "start" in command:
            player = "VoicePlayer"
            max_value = 100
            guess(max_value, player)
        else:
            print("Voice command not recognized.")
    else:
        print("Invalid choice! Restart and select 1-5.")

if __name__ == '__main__':
    main()

