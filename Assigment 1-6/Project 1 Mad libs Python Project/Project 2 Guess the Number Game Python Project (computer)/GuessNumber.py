import random
import pyttsx3  # Text-to-Speech
import pygame  # Sound Effects
import time

# 🎙️ Initialize Text-to-Speech Engine
tts_engine = pyttsx3.init()

def speak(text):
    """Text-to-Speech Output"""
    tts_engine.say(text)
    tts_engine.runAndWait()

def play_sound(filename):
    """Play funny sound effects."""
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def computer_guess(x):
    """User thinks of a number, and the computer tries to guess it."""
    print(f"\nThink of a number between 1 and {x}. The computer will guess it! 🤖🔢")
    speak(f"Think of a number between 1 and {x}. I will try to guess it!")

    low, high = 1, x
    feedback = ''
    attempts = 0

    dark_jokes = [
        "You thinking or buffering? 🤔🌀",
        "Bruh... even a rock would guess faster. 🪨💀",
        "Your brain has officially been put on airplane mode. ✈️🧠",
        "Nice, you just confused yourself. Proud of you. 👏😂",
        "Did you fall asleep or just forget how to read? 💤📖",
        "Are you waiting for divine intervention? Because it’s not coming. 🙏😆",
        "I’d roast you harder, but I see you’re already struggling enough. 🔥😂"
    ]

    while feedback != 'c':
        guess = (low + high) // 2  # Smart Binary Search
        attempts += 1

        # Computer asks in voice
        print(f"\nIs your number {guess}? 🤔")
        speak(f"Is your number {guess}?")

        feedback = input("\nToo high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("⚠️ Invalid input! Please enter H (high), L (low), or C (correct).")
            speak("Invalid input! Are you even trying?")
            play_sound("clown_horn.mp3")  # 🤡 Clown horn sound

        # 🎭 Dark humor moments
        if attempts == 5:  
            joke = random.choice(dark_jokes)
            print(f"\n💀 {joke}")
            speak(joke)
            play_sound("sad_trombone.mp3")  # 🎻 Sad trombone sound

        if attempts == 10:
            print("\n🎺 HONK HONK! Okay, are you even trying? 🤡")
            speak("Honk honk! Are you even trying?")
            play_sound("clown_horn.mp3")  # 🤡 Clown horn again

        if attempts == 15:
            print("\n💀 This is painful to watch. Need a tutorial? 📖")
            speak("This is painful to watch. Need a tutorial?")
            play_sound("facepalm.mp3")  # 🤦 Facepalm sound

        # 🚨 Contradiction check
        if low > high:
            print("\n⚠️ Oops! Your responses are contradictory. Restarting...")
            speak("Hmm, something seems wrong. Let's try again.")
            return  # Restart game if contradiction is detected

    # 🎉 Winning roast
    print(f"\n🎉 Yay! I guessed your number {guess} in {attempts} attempts! 🚀")
    speak(f"Haha! I guessed your number {guess} in {attempts} attempts!")
    play_sound("evil_laugh.mp3")  # 😈 Evil laugh when computer wins

    if attempts <= 3:
        print("😏 That was too easy. Try harder next time.")
        speak("That was too easy. Try harder next time.")

    elif attempts >= 15:
        print("💀 Wow. That was painful. Do you even know how numbers work?")
        speak("Wow. That was painful. Do you even know how numbers work?")

# Run the function
computer_guess(100)
