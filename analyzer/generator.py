import secrets
import string
def generate_secure_password(length:int = 12)->str:
    if not length >= 8:
        raise ValueError("Password length should be at least 8 characters")
    """defining the pool of characters to choose from"""
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    all_characters = uppercase + lowercase + digits + punctuation
    """generating a secure password"""
    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]
    password_chars += [secrets.choice(all_characters) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password_chars)  # Shuffle the characters
    return ''.join(password_chars)
