"""
Storage module for PyPass.

Handles reading and writing password data to JSON files.

The master password stays one-way hashed with Argon2 (verification only).
Stored credentials are encrypted with Fernet, using a key derived from the
master password via Argon2id and a per-vault random salt, so they can be
retrieved after authentication but are unreadable at rest.
"""

import base64
import json
import os
from pathlib import Path

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHash
from argon2.low_level import Type, hash_secret_raw
from cryptography.fernet import Fernet, InvalidToken

ph = PasswordHasher()

KDF_TIME_COST = 3
KDF_MEMORY_COST = 65536  # KiB
KDF_PARALLELISM = 4
KDF_HASH_LEN = 32


class VaultDecryptError(Exception):
    """Raised when the vault cannot be decrypted with the given master password."""


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


def _derive_key(master_password: str, salt: bytes) -> bytes:
    """
    Derive a 32-byte vault key from the master password with Argon2id.

    Args:
        master_password: Plaintext master password.
        salt: Random salt (16 bytes) stored alongside the vault.

    Returns:
        Raw key bytes suitable for Fernet.
    """
    return hash_secret_raw(
        master_password.encode("utf-8"),
        salt,
        time_cost=KDF_TIME_COST,
        memory_cost=KDF_MEMORY_COST,
        parallelism=KDF_PARALLELISM,
        hash_len=KDF_HASH_LEN,
        type=Type.ID,
    )


def _load_vault_file():
    path = get_passwords_path()
    if not path.is_file():
        return None
    data = json.loads(path.read_text())
    if data.get("version") != 1:
        return None
    return data


def migrate_legacy_vault() -> list[str]:
    """
    Move a legacy vault (Argon2-hashed entries) out of the way.

    Old versions hashed every stored password, so those entries cannot be
    recovered from their hashes. They are preserved untouched in
    Passwords/passwords.json.legacy and a fresh vault is started.

    Returns:
        Usernames that could not be recovered, so the caller can inform
        the user. Empty list when nothing needed migrating.
    """
    path = get_passwords_path()
    if not path.is_file():
        return []
    data = json.loads(path.read_text())
    if data.get("version") == 1:
        return []
    legacy = [u for u, v in data.items() if isinstance(v, str) and v.startswith("$argon2")]
    if not legacy:
        return []
    legacy_path = path.with_name("passwords.json.legacy")
    if legacy_path.is_file():
        path.unlink()
    else:
        path.rename(legacy_path)
    return legacy


def load_vault(master_password: str) -> dict:
    """
    Decrypt and return the stored credential entries.

    Args:
        master_password: Authenticated master password (used as the KDF input).

    Returns:
        Dict of username -> plaintext password. Empty dict if no vault exists.

    Raises:
        VaultDecryptError: If the vault exists but cannot be decrypted.
    """
    data = _load_vault_file()
    if data is None:
        return {}
    kdf = data["kdf"]
    salt = bytes.fromhex(kdf["salt"])
    key = _derive_key(master_password, salt)
    try:
        plain = Fernet(base64.urlsafe_b64encode(key)).decrypt(data["vault"].encode())
    except InvalidToken:
        raise VaultDecryptError(
            "Could not decrypt the vault with this master password."
        ) from None
    return json.loads(plain)


def save_vault(entries: dict, master_password: str):
    """
    Encrypt the full credential set and write it to disk.

    Args:
        entries: Dict of username -> plaintext password.
        master_password: Authenticated master password (used as the KDF input).
    """
    ensure_data_dir()
    salt = os.urandom(16)
    key = _derive_key(master_password, salt)
    token = Fernet(base64.urlsafe_b64encode(key)).encrypt(json.dumps(entries).encode())
    payload = {
        "version": 1,
        "kdf": {
            "salt": salt.hex(),
            "time_cost": KDF_TIME_COST,
            "memory_cost": KDF_MEMORY_COST,
            "parallelism": KDF_PARALLELISM,
            "hash_len": KDF_HASH_LEN,
        },
        "vault": token.decode(),
    }
    get_passwords_path().write_text(json.dumps(payload, indent=4))


def store_password(username: str, password: str, master_password: str):
    """
    Encrypt and store a username-password pair.

    Args:
        username: The username to associate with the password.
        password: The plaintext password to encrypt and store.
        master_password: Authenticated master password (used as the KDF input).
    """
    entries = load_vault(master_password)
    entries[username] = password
    save_vault(entries, master_password)


def get_password(username: str, master_password: str) -> str | None:
    """
    Retrieve and decrypt the password for a username.

    Args:
        username: The username to look up.
        master_password: Authenticated master password (used as the KDF input).

    Returns:
        Plaintext password string, or None if not found.
    """
    return load_vault(master_password).get(username)
