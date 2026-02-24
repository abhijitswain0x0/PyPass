def enable():
    master_password = "thisisthemasterpassword"
    
    auth = False
         
    try:

        master_password_by_user = input("Enter Master Password: ")

        if master_password_by_user == master_password:

            auth = True

            return True

        else:
            return False

    except KeyboardInterrupt:

        print("Exiting...")

        exit
