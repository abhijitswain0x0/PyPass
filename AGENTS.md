# PyPass v1.0.0

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
- `AGENTS.md` - Agent instructions
- `CONTRIBUTING.md` - Contribution guide

## Dependencies

- `argon2-cffi` - Argon2 hashing

Dev: `pyinstaller` - Build .exe

## Security

All passwords (master + stored) are hashed with Argon2 before storage.

## Reset Master Password

Delete `Passwords/master_password.json` and run again to create a new one.

## Build

```shell
uv pip install pyinstaller
.venv\Scripts\python -m PyInstaller --onefile --console --name PyPass main.py
```

Output: `dist/PyPass.exe`