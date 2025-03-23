from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Checks if the provided password (hashed) matches the stored hash for the given email.
    
    email: The email to authenticate.
    stored_logins: Dictionary mapping emails to hashed passwords.
    password_to_check: Plain-text password to be verified.
    
    Returns:
        True if login is successful, False otherwise.
    """
    hashed_password = hash_password(password_to_check)

    # Use .get() to avoid KeyError if email does not exist
    return stored_logins.get(email) == hashed_password


def hash_password(password):
    """
    Hashes a password using SHA-256.
    
    password: The input password (plain text).
    
    Returns:
        The SHA-256 hashed version of the password.
    """
    return sha256(password.encode()).hexdigest()


def main():
    """
    Simulates a login system using hashed passwords.
    """
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # 'password'
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # 'Karel'
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # '123!456?789'
    }

    test_cases = [
        ("example@gmail.com", "word"),         # ❌ Incorrect password
        ("example@gmail.com", "password"),     # ✅ Correct password
        ("code_in_placer@cip.org", "Karel"),   # ✅ Correct password
        ("code_in_placer@cip.org", "karel"),   # ❌ Incorrect (case-sensitive)
        ("student@stanford.edu", "password"),  # ❌ Incorrect password
        ("student@stanford.edu", "123!456?789"),  # ✅ Correct password
        ("unknown_user@test.com", "anypass")   # ❌ Email not in system
    ]

    print("\n **Login Test Cases** \n")
    for email, password in test_cases:
        result = login(email, stored_logins, password)
        print(f"🟢 Login success: {result}" if result else f"🔴 Login failed for '{email}'")


if __name__ == '__main__':
    main()
