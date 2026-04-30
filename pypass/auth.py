import pypass.storage as storage


def check_user_exists():
    return storage.get_master_password_path().is_file()


def authenticate_user():
    master_password = storage.load_master_password()
    if master_password is not None:
        try:
            provided = input("Enter Master Password: ")
            if provided == master_password:
                print("Password verified!")
                return True
            else:
                print("Wrong Password!")
                return False
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()
    else:
        create_user()


def create_user():
    print("No user has been identified!\nCreating new user...")
    master_password = input("Set a master password: ")
    storage.save_master_password(master_password)