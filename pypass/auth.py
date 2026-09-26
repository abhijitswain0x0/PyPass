"""
Authentication module for PyPass.

Handles master password verification using Argon2 hashes.
"""

from getpass import getpass

import pypass.storage as storage


def check_user_exists():
    return storage.get_master_password_path().is_file()


def authenticate_user() -> str | None:
    """
    Prompt for and verify the master password.

    Returns:
        The master password on success (it is needed to derive the vault
        key), or None on a wrong password.
    """
    stored_hash = storage.load_master_password()
    if stored_hash is not None:
        password = getpass("Enter Master Password: ")
        if storage.verify_password(password, stored_hash):
            print("Password verified!")
            return password
        print("Wrong Password!")
        return None
    return create_user()


def create_user() -> str:
    print("No user has been identified!\nCreating new user...")
    master_password = getpass("Set a master password: ")
    storage.save_master_password(master_password)
    return master_password
