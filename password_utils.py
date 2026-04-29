import random
from pathlib import Path
import json

import character_map


def get_username():
    """
    Prompts the user to enter a username to pair with a generated password.

    Returns:
        str: The username entered by the user.
    """
    username = input("Enter a username to pair with password: ")
    return username


def generate_password(length=16):
    """
    Generates a random password of specified length using a mix of character types.

    The password is constructed by randomly selecting characters from four categories:
    uppercase letters, lowercase letters, numbers, and symbols.

    Args:
        length (int): Desired password length. Defaults to 16.

    Returns:
        str: The generated password string.
    """
    password_chars = []

    for _ in range(length):
        choice_type = random.randrange(0, 4)

        if choice_type == 0:
            password_chars.append(random.choice(character_map.characters_uppercase))
        elif choice_type == 1:
            password_chars.append(random.choice(character_map.characters_lowercase))
        elif choice_type == 2:
            password_chars.append(random.choice(character_map.numbers))
        elif choice_type == 3:
            password_chars.append(random.choice(character_map.symbols))

    return "".join(password_chars)


def get_generated_password():
    """
    Prompts the user to confirm password generation and optionally specify length.

    If confirmed, generates a password with user-specified length or default.
    Handles invalid input gracefully by falling back to default length.

    Returns:
        str: The generated password.
    """
    while True:
        try:
            user_input = input("Generate Password? (Y/N): ").strip().lower()

            if user_input in ["y", "yes"]:
                try:
                    password_length = input("Enter password length [Default = 16]: ")
                    password = generate_password(length=int(password_length))
                    return password
                except ValueError:
                    password = generate_password()
                    return password

            elif user_input in ["n", "no"]:
                print("Exiting...")
                exit()
            else:
                print("Invalid input. Please enter Y or N.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()


def store_generated_password(username, password):
    """
    Saves a username-password pair to a JSON file.

    Creates the Passwords directory if it doesn't exist, then writes the
    username and password as a JSON object.

    Args:
        username (str): The username associated with the password.
        password (str): The password to store.
    """
    passwords_file_path = Path("Passwords/passwords.json")
    password_json = {username: password}

    passwords_file_path.parent.mkdir(parents=True, exist_ok=True)
    passwords_file_path.write_text(json.dumps(password_json, indent=4))
