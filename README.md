# PyPass

A Python CLI application for generating and managing secure passwords with master password authentication.

## Features

- **Custom-length password generation**: Generate passwords from 1 to any length (default: 16 characters)
- **Mixed character sets**: Passwords include uppercase, lowercase, numbers, and symbols
- **Master password protection**: Access is protected by a master/sudo password
- **Persistent storage**: Generated passwords are saved locally as JSON

## Requirements

- Python 3.11+

## Installation

```shell
git clone https://github.com/abhijitswain0x0/PyPass.git
cd PyPass
```

## Usage

```shell
python main.py
```

On first run, you'll be prompted to create a master password. Subsequent runs require the master password to proceed.

## Project Structure

```
PyPass/
├── main.py                # Application entry point
├── authentification.py    # Master password authentication
├── password_utils.py      # Password generation and storage
├── character_map.py      # Character sets for password generation
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

## How It Works

1. **Authentication**: On startup, the app checks for a master password file. If none exists, it prompts you to create one. Otherwise, it verifies your input.
2. **Password Generation**: After authentication, you can generate a password of any length (default 16). Characters are randomly selected from:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Symbols (!, @, #, $, %, ^, &, *, (, ), -, _, =, +)
3. **Storage**: Username-password pairs are stored in `Passwords/passwords.json`.

## License

MIT License