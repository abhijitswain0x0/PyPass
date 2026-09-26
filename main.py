import sys

import pypass.auth as auth
import pypass.cli as cli
import pypass.storage as storage


def main():
    print("PyPass")
    master_password = None
    while master_password is None:
        master_password = auth.authenticate_user()

    dropped = storage.migrate_legacy_vault()
    if dropped:
        print(
            f"NOTE: previously hashed entries for {', '.join(dropped)} cannot be "
            "recovered from their hashes. They were moved to "
            "Passwords/passwords.json.legacy and a fresh encrypted vault was started."
        )

    while True:
        action = input("\nStore a password (s) / Retrieve a password (r) / Exit (q): ").strip().lower()
        if action in ("s", "store"):
            password = cli.prompt_generate_password()
            username = cli.prompt_username()
            cli.store_password(username, password, master_password)
            print(f"Stored {username}.")
        elif action in ("r", "retrieve"):
            username = cli.prompt_username()
            found = cli.retrieve_password(username, master_password)
            if found is None:
                print(f"No password stored for {username}.")
            else:
                print(f"{username}: {found}")
        elif action in ("q", "quit", "exit"):
            print("Exiting...")
            return
        else:
            print("Invalid input. Please enter s, r, or q.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        sys.exit(0)
