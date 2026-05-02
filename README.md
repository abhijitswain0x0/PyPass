# PyPass

A Python CLI password manager with Argon2 hashing.

## Features

- **Custom-length password generation**: Generate passwords from 1 to any length (default: 16 characters)
- **Mixed character sets**: Passwords include uppercase, lowercase, numbers, and symbols
- **Master password protection**: Access is protected by a master password (hashed with Argon2)
- **Secure storage**: All passwords are hashed with Argon2 before storage


## Installation Video:

<video src="https://github.com/abhijitswain0x0/PyPass/blob/main/Pypass-Demo_v1.mp4" controls width="100%"></video>

## Project Structure

```
PyPass/
├── main.py              # Application entry point
├── pyproject.toml       # UV package configuration
├── pypass/              # Package
│   ├── __init__.py      # Constants
│   ├── auth.py          # Master password authentication
│   ├── storage.py       # File I/O + Argon2 hashing
│   ├── generator.py     # Password generation
│   ├── cli.py           # User prompts
│   └── characters.py    # Character sets
├── Passwords/           # Data directory (gitignored)
├── .venv/               # Virtual environment (gitignored)
├── README.md            # Project documentation
├── CONTRIBUTING.md      # Contribution guide
├── AGENTS.md            # Agent instructions
└── LICENSE              # MIT License
```

## How It Works

1. **Authentication**: On startup, the app checks for a master password file. If none exists, it prompts you to create one. Otherwise, it verifies your input against an Argon2 hash.
2. **Password Generation**: After authentication, you can generate a password of any length (default 16). Characters are randomly selected from:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Symbols (!, @, #, $, %, ^, &, *, (, ), -, _, =, +)
3. **Storage**: Username-password pairs are hashed with Argon2 and stored in `Passwords/passwords.json`.

## Security

All passwords (master and stored) are hashed using Argon2:
- Time cost: 3
- Memory cost: 64 MB
- Parallelism: 4

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License
