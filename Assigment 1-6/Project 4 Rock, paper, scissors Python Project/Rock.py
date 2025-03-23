import random
import pyttsx3  # Text-to-Speech
import speech_recognition as sr  # Voice Recognition
import tkinter as tk  # GUI
import pygame  # Sound Effects
import time

# 🎙️ Initialize Text-to-Speech Engine
tts_engine = pyttsx3.init()

def speak(text):
    """Text-to-Speech Output"""
    tts_engine.say(text)
    tts_engine.runAndWait()

# 🎤 Speech Recognition Function
def get_user_choice_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Rock, Paper, or Scissors:")
        speak("Say Rock, Paper, or Scissors.")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return "invalid"
        except sr.RequestError:
            return "error"

# 🔊 Initialize Sound Effects
#def play_sound(sound):
    #pygame.mixer.init()
    #pygame.mixer.music.load(sound)
    #pygame.mixer.music.play()

# 🤖 AI Chooses Based on Player History
user_choices = []

def get_computer_choice():
    """AI learns & counters most common player choice"""
    if len(user_choices) < 3:
        return random.choice(["rock", "paper", "scissors"])
    
    most_common = max(set(user_choices), key=user_choices.count)
    counter_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter_moves[most_common]

# 💀 Savage AI Roasts
roasts = [
    "Wow, you actually thought that would work? 😂",
    "Bruh, my grandma plays better than you. 💀",
    "That was the worst choice since the Titanic. 🚢💥",
    "If losing was a sport, you'd be the GOAT. 🐐😂",
]

def determine_winner(user, computer):
    """Decides winner based on choices."""
    if user == computer:
        return "It's a tie! 🤝"
    
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning_combinations[user] == computer:
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

# 🏆 Best of X Tournament Mode
def play_game(best_of=3):
    """Main function for Rock, Paper, Scissors."""
    print(f"🎮 Best of {best_of} Mode! First to {best_of // 2 + 1} wins!")

    choices = ["rock", "paper", "scissors"]
    user_score, computer_score = 0, 0
    rounds_to_win = best_of // 2 + 1  # First to win X rounds

    while user_score < rounds_to_win and computer_score < rounds_to_win:
        user_choice = input("\nEnter Rock, Paper, or Scissors (or 'voice' to speak): ").lower()
        
        if user_choice == "voice":
            user_choice = get_user_choice_voice()
        
        if user_choice not in choices:
            print("⚠️ Invalid choice! Choose Rock, Paper, or Scissors.")
            speak("Invalid choice. Try again.")
            continue
        
        user_choices.append(user_choice)
        computer_choice = get_computer_choice()
        
        print(f"\nComputer chose: {computer_choice.capitalize()}")
        speak(f"I choose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        speak(result)

        if "You win" in result:
            user_score += 1
            #play_sound("sound/win.mp3")
        elif "Computer wins" in result:
            computer_score += 1
            roast = random.choice(roasts)  # Brutal AI roast
            print(f"\n💀 {roast}")
            speak(roast)
            #play_sound("sound/roast.mp3")
            time.sleep(1)

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

    # 🏆 Announce Winner
    if user_score > computer_score:
        print("\n🎉 YOU WIN THE TOURNAMENT!")
        speak("Congratulations! You win the tournament!")
    else:
        print("\n😈 COMPUTER WINS! Bow to your AI overlord!")
        speak("I am your AI overlord! You lose!")

# 🎨 GUI Mode
def play_gui():
    """Tkinter GUI for Rock, Paper, Scissors"""
    def on_click(choice):
        user_choices.append(choice)
        computer = get_computer_choice()
        result = determine_winner(choice, computer)
        result_label.config(text=f"Computer: {computer.capitalize()}\n{result}")
        speak(result)
    
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    
    tk.Label(root, text="Choose your move!", font=("Arial", 14)).pack()
    tk.Button(root, text="Rock", command=lambda: on_click("rock")).pack()
    tk.Button(root, text="Paper", command=lambda: on_click("paper")).pack()
    tk.Button(root, text="Scissors", command=lambda: on_click("scissors")).pack()
    
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack()
    
    root.mainloop()

# 🎮 Main Menu
def main():
    print("🎮 Ultimate Rock, Paper, Scissors")
    print("1️⃣ Play Best of 3 (Text Mode)")
    print("2️⃣ Play Best of 5 (Text Mode)")
    print("3️⃣ Play in GUI Mode")
    print("4️⃣ Quit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        play_game(best_of=3)
    elif choice == '2':
        play_game(best_of=5)
    elif choice == '3':
        play_gui()
    else:
        print("Goodbye!")
        speak("Goodbye!")

# Run the Game
if __name__ == '__main__':
    main()
