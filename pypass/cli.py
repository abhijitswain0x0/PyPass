import sys

import pypass.generator as generator
import pypass.storage as storage


def prompt_username():
    return input("Enter a username to pair with password: ")


def prompt_generate_password():
    while True:
        choice = input("Generate Password? (Y/N): ").strip().lower()
        if choice in ("y", "yes"):
            try:
                length = int(input("Enter password length [Default = 16]: "))
                return generator.generate(length)
            except ValueError:
                return generator.generate()
        elif choice in ("n", "no"):
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid input. Please enter Y or N.")


def store_password(username, password, master_password):
    storage.store_password(username, password, master_password)


def retrieve_password(username, master_password):
    return storage.get_password(username, master_password)
