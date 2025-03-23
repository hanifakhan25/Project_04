import random
import string
import pyperclip  # To copy password to clipboard
import json  # To save passwords to a file
import hashlib  # To hash passwords for security
import qrcode  # To generate QR codes
import time

# Weak password list
COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "welcome", "123123", "admin", "iloveyou", "abc123", "monkey"}

# 🔐 Generate Secure Password
def generate_password(length=12, use_digits=True, use_special=True, avoid_similar=True, must_include=[]):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if avoid_similar:
        characters = characters.replace("O", "").replace("0", "").replace("l", "").replace("1", "")
    
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if all(any(c in password for c in group) for group in must_include) and password not in COMMON_PASSWORDS:
            return password

# 📊 Strength Meter
def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    
    return ["Weak", "Moderate", "Strong", "Very Strong"][score]

# 🔒 Hash Password for Secure Storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 📂 Save Passwords Securely
def save_passwords(passwords):
    encrypted_passwords = [{"label": p["label"], "password": hash_password(p["password"])} for p in passwords]
    with open("generated_passwords.json", "w") as file:
        json.dump(encrypted_passwords, file, indent=4)
    print("📂 Passwords saved securely in generated_passwords.json!")

# 🔗 Generate QR Code for Password
def generate_qr(password, label):
    """Generate and save a QR code for the password with a unique filename."""
    qr = qrcode.make(password)
    filename = f"{label}_password_qr.png".replace(" ", "_")  # Replace spaces in label
    qr.save(filename)
    print(f"📱 QR code generated! Check {filename}")

# 📝 Generate Passphrase
def generate_passphrase(words=4):
    word_list = ["cloud", "tiger", "banana", "rocket", "panda", "guitar", "ocean", "shadow", "volcano", "glitch", "matrix", "cyber", "dragon", "phantom", "ninja"]
    return '-'.join(random.sample(word_list, words))

# 🚀 Main Function
def main():
    print("🔐 Welcome to the Ultimate Password Generator!")
    num_passwords = int(input("How many passwords do you need? "))
    length = int(input("Enter password length: "))
    include_digits = input("Include numbers? (yes/no): ").lower() == "yes"
    include_specials = input("Include special characters? (yes/no): ").lower() == "yes"
    avoid_similar = input("Avoid similar characters (O/0, l/1)? (yes/no): ").lower() == "yes"
    
    must_include = []
    if include_digits:
        must_include.append(string.digits)
    if include_specials:
        must_include.append(string.punctuation)
    must_include.append(string.ascii_uppercase)
    must_include.append(string.ascii_lowercase)
    
    passwords = []
    print("\n🎯 Your Generated Passwords:")
    for _ in range(num_passwords):
        label = input("Enter a label for this password (e.g., Email, Bank): ")
        password = generate_password(length, include_digits, include_specials, avoid_similar, must_include)
        strength = check_strength(password)
        passwords.append({"label": label, "password": password, "strength": strength})
        print(f"{label}: {password}  |  Strength: {strength}")
    
    # 🔗 Copy First Password to Clipboard
    pyperclip.copy(passwords[0]["password"])
    print("📋 First password copied to clipboard!")
    
    # 💾 Save Passwords Securely
    save_passwords(passwords)
    
    # 📱 Generate QR Code Option
    if input("Generate QR code for first password? (yes/no): ").lower() == "yes":
        generate_qr(passwords[0]["password"], passwords[0]["label"])
    
    # 📝 Generate Passphrase Option
    if input("Do you want a passphrase instead? (yes/no): ").lower() == "yes":
        passphrase = generate_passphrase()
        print(f"📝 Passphrase: {passphrase}")
        pyperclip.copy(passphrase)
        print("📋 Passphrase copied to clipboard!")
    
    print("\n✅ Stay secure and keep your passwords safe!")

if __name__ == "__main__":
    main()
