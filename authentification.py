def auth():
    master_password = "master_password"

    provided_master_password = input("Enter Master Password: ")

    if provided_master_password == master_password:
        print("Confirmed")

    elif provided_master_password != master_password:
        print("Error")

auth()
