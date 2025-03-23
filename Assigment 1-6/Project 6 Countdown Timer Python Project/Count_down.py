import time
import pyttsx3  # AI Voice
import pygame   # Sound Effects
import random


# 🎙️ AI Voice Options
VOICE_MODES = {
    "default": "Normal Mode",
    "robot": "Robot Mode Activated.",
    "genz": "Yo fam, get ready!"  
}

def speak(text, mode="default"):
    """AI Voice Announcement with Modes"""
    engine = pyttsx3.init()
    if mode == "robot":
        engine.setProperty('rate', 100)
    elif mode == "genz":
        text = "Ayo! " + text
    engine.say(text)
    engine.runAndWait()


# 🔥 Random Motivational & Roast Messages
MOTIVATION = [
    "Keep pushing! You got this!", 
    "Hustle mode activated!", 
    "You're built different, keep going!"
]

ROASTS = [
    "Bruh, you really need a timer for this? 😂", 
    "Why you moving like a sloth? 🐌", 
    "Skill issue detected. Speed it up! 🚨"
]

FUN_FACTS = [
    "Did you know? A day on Venus is longer than a year on Venus!",
    "Fun fact: The Eiffel Tower can grow taller in summer!",
    "Random fact: Octopuses have three hearts!"
]

def countdown_timer(seconds, voice_mode="default", alarm_type="classic"):
    """Countdown Timer with AI Voice, Roasts, Motivation & Fun Facts"""
    speak(VOICE_MODES[voice_mode], voice_mode)
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02}:{secs:02}"
        print(timer_format, end='\r')
        
        if seconds == 10:
            speak(random.choice(MOTIVATION), voice_mode)
        elif seconds == 5:
            speak(random.choice(ROASTS), voice_mode)
        elif seconds == 3:
            speak("Final seconds, don’t fumble!", voice_mode)
        elif seconds % 20 == 0:
            print(random.choice(FUN_FACTS))
        
        time.sleep(1)
        seconds -= 1
    
    print("00:00 🚀 Time's up!")
    speak("Boom! Timer ended. You made it!", voice_mode)
   # play_sound(SOUND_OPTIONS[alarm_type])

if __name__ == "__main__":
    total_time = int(input("Enter countdown time in seconds: "))
    voice_choice = input("Choose voice mode (default/robot/genz): ").lower()
    #alarm_choice = input("Choose alarm type (hype/classic/meme): ").lower()
    countdown_timer(total_time, voice_choice,) #alarm_choice)
