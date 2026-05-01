from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password):
    """Generates a secure hash to store in your JSON."""
    return ph.hash(password)

def verify_password(stored_hash, provided_password):
    """Checks if the provided password matches the stored hash."""
    try:
        return ph.verify(stored_hash, provided_password)
    except VerifyMismatchError:
        return False
