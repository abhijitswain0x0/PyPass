# PyPass
A Python CLI password manager. No build/test tooling.
## Run
```
python main.py
```
## Project Structure
- `main.py` - Entry point
- `pypass/` - Package
  - `auth.py` - Master password auth
  - `storage.py` - File I/O (passwords.json, master_password.json)
  - `generator.py` - Password generation
  - `cli.py` - User prompts (username, password length)
  - `characters.py` - Character sets
  - `__init__.py` - DATA_DIR constant
- `Passwords/` - Data directory, gitignored
## Reset Master Password
Delete `Passwords/master_password.json` and run again to create a new one.