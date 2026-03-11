def auth():
    master_password = "master_password"  # stores the master passwords

    # try except block for error handling
    try:
        provided_master_password = input(
            "Enter Master Password: "
        )  # asks the user to give the master password

        # checks if the provided_master_password = master_password
        #
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
