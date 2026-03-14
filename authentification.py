from pathlib import Path
import json


def authentificate_user():

    user_exists = if_user_exists()

    if user_exists:

        path = Path("passwords/master_password.json")
        data = json.loads(path.read_text())

        master_password = data["sudo"]

        # try except block for error handling
        try:
            provided_master_password = input(
                "Enter Master Password: "
            )  # asks the user to give the master password

            # checks if the provided_master_password = master_password

            if provided_master_password == master_password:
                print("Password verified!")

                return True  # returns True as confirmation

            elif provided_master_password != master_password:
                print("Wrong Password!")

                return False

        except (
            KeyboardInterrupt
        ):  # listens for keyboard interrupt and handles it correctly by calling python's in-built exit() function
            print("\nExiting...")

            exit()

    else:
        create_user()


def if_user_exists():
    master_password = Path("passwords/master_password.json")

    if master_password.is_file():
        return True

    else:
        return False


def create_user():
    print("No user has been identified!" + "\nCreating new user...")

    master_password = input("Set a master password:")

    master_password_json = {"sudo": master_password}

    master_password_file_path = Path("Passwords/master_password.json")

    master_password_file_path.parent.mkdir(parents=True, exist_ok=True)
    master_password_file_path.write_text(json.dumps(master_password_json, indent=4))
