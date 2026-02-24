def auth():
    master_password = "master_password"
    
    try:
        provided_master_password = input("Enter Master Password: ")

        if provided_master_password == master_password:
            print("Password verified!")
        
            return True

        elif provided_master_password != master_password:
            print("Wrong Password!")
        
            return False

    except KeyboardInterrupt:
        print("\nExiting...")

        exit()
