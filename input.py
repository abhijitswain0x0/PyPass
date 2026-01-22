import main

def get_input():
    user_choice = input("Genrate Password[(Y)es/(N)o]: ")

    available_inputs = ["Y", "N", "Yes", "No", "yes", "no", "y", "n"]

    if user_choice == available_inputs[0]:
        main.create_password()
    elif user_choice == available_inputs[1]:
        exit()
    elif user_choice == available_inputs[2]:
        main.create_password()
    elif user_choice == available_inputs[3]:
        exit()
    elif user_choice == available_inputs[4]:
        main.create_password()
    elif user_choice == available_inputs[5]:
        exit()
    elif user_choice == available_inputs[6]:
        main.create_password()
    elif user_choice == available_inputs[7]:
        exit()