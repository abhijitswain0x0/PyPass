import authentification  # imports authentification.py file for user verification
import password_utils  # imports password_utils.py file to get generated passwords


def init():  # function to initialize/starts the app
    print("PyPass")

    # checks if user has the master password

    verification_state = False  # stores current state of verification

    while not verification_state:  # loops indefinetly until verification state == true
        verification_state = authentification.auth()  # calls the authentification.auth() function and stores its return value in the verfication_state variable

    password_utils.get_generated_password()  # calls the get_generated_password function funtion from password_utils


if __name__ == "__main__":  # calls the init function to start the app
    init()
