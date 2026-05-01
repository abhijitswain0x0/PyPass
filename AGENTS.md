# PyPass
A Python CLI password manager with Argon2 hashing.
## Run
```shell
python main.py
```
(Or activate .venv: `source .venv/Scripts/activate` then `python main.py`)
## Project Structure
- `main.py` - Entry point
- `pyproject.toml` - UV package config
- `pypass/` - Package
  - `auth.py` - Master password auth
  - `storage.py` - File I/O + Argon2 hashing
  - `generator.py` - Password generation
  - `cli.py` - User prompts
  - `characters.py` - Character sets
  - `__init__.py` - DATA_DIR constant
- `Passwords/` - Data directory (gitignored)
- `.venv/` - Virtual environment (gitignored)
## Security
All passwords (master + stored) are hashed with Argon2 before storage.
## Reset Master Password
Delete `Passwords/master_password.json` and run again to create a new one.