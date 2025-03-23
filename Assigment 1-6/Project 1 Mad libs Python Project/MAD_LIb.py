import random
import os
import pyttsx3  # Text-to-Speechadvanture
import pygame   # For Sound Effects & Background Music

# 🔊 Initialize Pygame for Background Music & Sound Effects
pygame.init()

# 📂 Define Sound Folder Paths
SOUND_FOLDER = r"C:\Users\umar\Desktop\Project04_ Assigments\Assigments 1- 6\Project 1 Mad libs Python Project\Sounds"

# 🎵 List of Random Background Music Files
MUSIC_FILES = [
    "Company.mp3",
    "Payphone.mp3", 
    "Sugar-Crash.mp3" ,
    "Lauv-I-Like-Me-Better.mp3" ,
    #"mystery_theme.mp3"
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

# Load Sound Effects
correct_sound_path = os.path.join(SOUND_FOLDER, "correct_sound.wav")
wrong_sound_path = os.path.join(SOUND_FOLDER, "wrong_sound.wav")

if os.path.exists(correct_sound_path):
    sound_correct = pygame.mixer.Sound(correct_sound_path)
else:
    print("⚠️ correct_sound.wav not found! Sound effect will be skipped.")
    sound_correct = None

if os.path.exists(wrong_sound_path):
    sound_wrong = pygame.mixer.Sound(wrong_sound_path)
else:
    print("⚠️ wrong_sound.wav not found! Sound effect will be skipped.")
    sound_wrong = None

# Story Templates with Many Themes 🎭
STORY_TEMPLATES = {
    "Adventure": [
        "One day, a {adjective} {noun} was {verb} {adverb} in the jungle when a {animal} appeared!",
        "In the middle of the {place}, a {adjective} explorer found a {noun} that could {verb}!"
    ],
    "Sci-Fi": [
        "A {adjective} {noun} from Mars landed on Earth and started to {verb} {adverb}.",
        "The {adjective} spaceship encountered a {animal} that knew how to {verb}!"
    ],
    "Rom-Com": [
        "At a {place}, a {adjective} {noun} accidentally bumped into a {adjective} {noun}, and they both {verb} {adverb}.",
        "The {adjective} date turned into a disaster when a {animal} decided to {verb} at the restaurant."
    ],
    "Dark Romance": [
        "Under the {adjective} moonlight, a {noun} whispered, 'I will {verb} you forever, no matter how {adjective} it gets.'.",
        "In the {place}, a {adjective} {noun} confessed their love, knowing it would lead to {adjective} consequences."
    ],
    "Tragic Endings": [
        "The {adjective} hero tried to {verb}, but in the end, fate had other plans and {adverb} took it all away.",
        "The {noun} they loved most was lost forever, leaving them to {verb} in {adjective} solitude."
    ],
    "Violence": [
        "With a {adjective} roar, the {noun} swung their {noun} and {verb} the enemy {adverb}.",
        "The battlefield was {adjective} as warriors {verb} through the chaos with {adjective} determination."
    ]
}

# Random Word Bank for Auto-Fill
WORD_BANK = {
    "noun": ["robot", "wizard", "treasure", "unicorn", "superpower", "warrior", "villain", "lover", "betrayer"],
    "verb": ["jump", "dance", "sing", "fly", "punch", "whisper", "attack", "embrace", "sacrifice"],
    "adjective": ["shiny", "brave", "magical", "gigantic", "invisible", "doomed", "mysterious", "dangerous"],
    "adverb": ["quickly", "happily", "loudly", "silently", "gracefully", "tragically", "violently", "softly"],
    "place": ["forest", "space", "village", "desert", "ocean", "battlefield", "castle", "dark alley"],
    "animal": ["tiger", "dragon", "alien", "phoenix", "dinosaur", "raven", "serpent", "wolf"],
    "exclamation": ["Wow!", "Oh no!", "Hooray!", "Yikes!", "Oops!", "Damn!", "Alas!", "For honor!"]
}

# Initialize Text-to-Speech Engine 🎙️
tts_engine = pyttsx3.init()

def speak(text):
    """
    Speaks the given text using Text-to-Speech.
    """
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_user_input(prompt, category):
    """
    AI asks for user input, and user types their answer.
    If left blank, it picks a random word.
    """
    speak(prompt)
    user_input = input(prompt + " ").strip()

    if not user_input:
        user_input = random.choice(WORD_BANK[category])
        print(f"💡 Auto-suggested: {user_input}")

    return user_input

def generate_story(theme):
    """
    Generates a Mad Libs story based on user input.
    """
    template = random.choice(STORY_TEMPLATES[theme])

    words = {key: get_user_input(f"Enter a {key}:", key) for key in WORD_BANK}
    
    return template.format(**words)

def main():
    """
    Runs the ultimate Mad Libs game with themes, sound effects, and music.
    """
    print("\n🎭 Welcome to Mad Libs! Choose a theme: Adventure, Sci-Fi, Rom-Com, Dark Romance, Tragic Endings, Violence 🎭")
    speak("Choose a theme.")
    theme = input("Select a theme: ").strip().capitalize()
    if theme not in STORY_TEMPLATES:
        theme = "Adventure"

    print("\n📝 Fill in the blanks below!")
    speak("Fill in the blanks below!")

    story = generate_story(theme)

    print("\n📖 Here's your Mad Libs story:\n")
    print(story)

    speak("Here is your story!")
    speak(story)

    print("\n📂 Story saved to mad_libs_story.txt!")

if __name__ == '__main__':
    main()
