import authentification
import password_utils


def init():
    """
    Initializes and runs the PyPass application.
    
    Displays the app title and prompts for user authentication.
    Once authenticated, generates a password and stores it with
    the associated username.
    """
    print("PyPass")

    verification_state = False

    while not verification_state:
        verification_state = authentification.authentificate_user()

    password = password_utils.get_generated_password()
    username = password_utils.get_username()

    print(f"{username}: {password}")
    password_utils.store_generated_password(username, password)


if __name__ == "__main__":
    init()
