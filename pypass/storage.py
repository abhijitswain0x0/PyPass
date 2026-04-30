import json
from pathlib import Path


def get_passwords_path():
    return Path("Passwords/passwords.json")


def get_master_password_path():
    return Path("Passwords/master_password.json")


def ensure_data_dir():
    Path("Passwords").mkdir(parents=True, exist_ok=True)


def load_passwords():
    path = get_passwords_path()
    if not path.is_file():
        return {}
    return json.loads(path.read_text())


def save_passwords(data):
    ensure_data_dir()
    get_passwords_path().write_text(json.dumps(data, indent=4))


def store_password(username, password):
    data = load_passwords()
    data[username] = password
    save_passwords(data)


def load_master_password():
    path = get_master_password_path()
    if not path.is_file():
        return None
    return json.loads(path.read_text()).get("master_password")


def save_master_password(master_password):
    ensure_data_dir()
    path = get_master_password_path()
    path.write_text(json.dumps({"master_password": master_password}, indent=4))