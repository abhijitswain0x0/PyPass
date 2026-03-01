import authentification
import password_utils


def init():
    print("PyPass")

    verification_state = False

    while not verification_state:
        if authentification.auth():
            verification_state = True
            break

        else:
            verification_state = False

    password_utils.get_generated_password()


if __name__ == "__main__":
    init()
