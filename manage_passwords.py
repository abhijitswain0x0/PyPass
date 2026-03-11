from pathlib import Path

passwords = Path("passwords/passwords.json")

if passwords.is_file():
    print("file_found")
else:
    print("fuh naw")
