"""
Authentication module for PyPass.

Handles master password verification using Argon2 hashes.
"""

import pypass.storage as storage


def check_user_exists():
    return storage.get_master_password_path().is_file()


def authenticate_user():
    stored_hash = storage.load_master_password()
    if stored_hash is not None:
        try:
            password = input("Enter Master Password: ")
            if storage.verify_password(password, stored_hash):
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
    print("No user has been identified!\nCreating new user...")
    master_password = input("Set a master password: ")
    storage.save_master_password(master_password)