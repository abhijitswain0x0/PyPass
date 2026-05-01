# Contributing to PyPass

Thank you for your interest in contributing!

## Ways to Contribute

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Development Setup

```shell
# Clone the repository
git clone https://github.com/abhijitswain0x0/PyPass.git
cd PyPass

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Unix

# Install dependencies
uv pip install -e .
uv pip install -e ".[dev]"
```

## Running the App

```shell
python main.py
```

## Building the .exe

```shell
.venv\Scripts\python -m PyInstaller --onefile --console --name PyPass main.py
```

Output: `dist/PyPass.exe`

## Code Style

- Use 4 spaces for indentation
- Add docstrings to functions
- Keep modules focused (one responsibility per file)

## Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run tests (if any)
5. Commit and push
6. Open a pull request

## License

By contributing, you agree that your contributions will be licensed under MIT.