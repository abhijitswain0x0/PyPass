# PyPass

A Python CLI password manager. No build/test tooling.

## Run

```shell
python main.py
```

## Project Structure

- `main.py` - Entry point
- `authentification.py` - Master password auth (first run prompts to create; subsequent runs verify)
- `password_utils.py` - Password generation and storage
- `character_map.py` - Character sets (uppercase, lowercase, numbers, symbols)
- `Passwords/` - Data directory, gitignored

## Reset Master Password

Delete `Passwords/master_password.json` and run again to create a new one.