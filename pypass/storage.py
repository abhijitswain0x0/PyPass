"""
Storage module for PyPass.

Handles reading and writing password data to JSON files.
All passwords are hashed using Argon2 before storage.
"""

import json
from pathlib import Path
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHash


ph = PasswordHasher()


def get_passwords_path():
    return Path("Passwords/passwords.json")


def get_master_password_path():
    return Path("Passwords/master_password.json")


def ensure_data_dir():
    Path("Passwords").mkdir(parents=True, exist_ok=True)


def hash_password(password: str) -> str:
    """
    Hash a password using Argon2.

    Uses default parameters:
    - time=3 (number of iterations)
    - memory=65536 (memory in KB)
    - parallelism=4 (parallel threads)

    Args:
        password: Plaintext password to hash.

    Returns:
        Argon2 hash string.
    """
    return ph.hash(password)


def verify_password(password: str, hash: str) -> bool:
    """
    Verify a password against an Argon2 hash.

    Args:
        password: Plaintext password to verify.
        hash: Argon2 hash to verify against.

    Returns:
        True if password matches hash, False otherwise.
    """
    try:
        ph.verify(hash, password)
        return True
    except (VerifyMismatchError, VerificationError, InvalidHash):
        return False


def load_passwords():
    path = get_passwords_path()
    if not path.is_file():
        return {}
    return json.loads(path.read_text())


def save_passwords(data):
    ensure_data_dir()
    get_passwords_path().write_text(json.dumps(data, indent=4))


def store_password(username: str, password: str):
    """
    Hash and store a username-password pair.

    Args:
        username: The username to associate with the password.
        password: The plaintext password to hash and store.
    """
    data = load_passwords()
    data[username] = hash_password(password)
    save_passwords(data)


def get_password(username: str) -> str | None:
    """
    Retrieve the hashed password for a username.

    Args:
        username: The username to look up.

    Returns:
        Hashed password string, or None if not found.
    """
    data = load_passwords()
    return data.get(username)


def load_master_password():
    path = get_master_password_path()
    if not path.is_file():
        return None
    return json.loads(path.read_text()).get("master_password")


def save_master_password(master_password: str):
    """
    Hash and save the master password.

    Args:
        master_password: Plaintext master password to hash and store.
    """
    ensure_data_dir()
    path = get_master_password_path()
    hashed = hash_password(master_password)
    path.write_text(json.dumps({"master_password": hashed}, indent=4))