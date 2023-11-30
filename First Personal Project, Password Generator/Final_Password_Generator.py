import secrets
import string

"""Password Generator

Author: William Jedrzejczak.

Version: 8/29/2023
"""


def generate_password(length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_punctuation=True):
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    secure_random = secrets.SystemRandom()

    # Ensure at least one character from each selected category
    password = [secure_random.choice(string.ascii_uppercase) if use_uppercase else '',
                secure_random.choice(string.ascii_lowercase) if use_lowercase else '',
                secure_random.choice(string.digits) if use_digits else '',
                secure_random.choice(string.punctuation) if use_punctuation else '']

    # Fill the rest of the password
    for _ in range(length - len(password)):
        password.append(secure_random.choice(characters))

    # Shuffle the password
    secure_random.shuffle(password)

    return ''.join(password)

# Example usage:
length = int(input("Enter the length of the password: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation)
print("Generated Password:", password)
