import json
from pathlib import Path


def check_user_exists():
    """
    Checks if a master password file already exists.

    Returns:
        bool: True if master password file exists, False otherwise.
    """
    master_password_path = Path("Passwords/master_password.json")
    return master_password_path.is_file()


def authenticate_user():
    """
    Authenticates the user by verifying their master password.

    If a master password file exists, prompts the user to enter their password
    and compares it against the stored value. If no user exists, creates a new one.

    Returns:
        bool: True if authentication successful, False otherwise.
    """
    if check_user_exists():
        path = Path("Passwords/master_password.json")
        data = json.loads(path.read_text())
        master_password = data["master_password"]

        try:
            provided_master_password = input("Enter Master Password: ")

            if provided_master_password == master_password:
                print("Password verified!")
                return True
            else:
                print("Wrong Password!")
                return False

        except KeyboardInterrupt:
            print("\nExiting...")
            exit()
    else:
        create_user()


def create_user():
    """
    Creates a new master password for first-time setup.

    Prompts the user to set a master password and saves it to a JSON file
    in the Passwords directory.
    """
    print("No user has been identified!\nCreating new user...")

    master_password = input("Set a master password: ")
    master_password_json = {"master_password": master_password}

    master_password_file_path = Path("Passwords/master_password.json")
    master_password_file_path.parent.mkdir(parents=True, exist_ok=True)
    master_password_file_path.write_text(json.dumps(master_password_json, indent=4))