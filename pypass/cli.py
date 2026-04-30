import pypass.storage as storage
import pypass.generator as generator


def prompt_username():
    return input("Enter a username to pair with password: ")


def prompt_generate_password():
    while True:
        try:
            choice = input("Generate Password? (Y/N): ").strip().lower()
            if choice in ("y", "yes"):
                try:
                    length = int(input("Enter password length [Default = 16]: "))
                    return generator.generate(length)
                except ValueError:
                    return generator.generate()
            elif choice in ("n", "no"):
                print("Exiting...")
                exit()
            else:
                print("Invalid input. Please enter Y or N.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()


def store_password(username, password):
    storage.store_password(username, password)
