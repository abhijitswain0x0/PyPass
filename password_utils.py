import random  # imports the random library
from pathlib import Path 
import json


import character_map  # imports charecter_mpa.py to get all charcters to use in a password

def get_username():
    username = input("Enter a username to pair with password: ")

    return username

def generate_password(
    length=16,
):  # function to generate passwords with any given lenght with 16 as the default
    password_chars = []  # array to store the password temporarily

    # generates passwords by creating a for loop which loops as many times specified
    # gets a random chareter map and then picks a random charecter out of it and appends to the password_chars array
    # it then return a string by joining all the charecters in the array at every index

    for _ in range(length):
        choice_type = random.randrange(0, 4)

        if choice_type == 0:
            password_chars.append(random.choice(character_map.characters_uppercase))
        elif choice_type == 1:
            password_chars.append(random.choice(character_map.characters_lowercase))
        elif choice_type == 2:
            password_chars.append(random.choice(character_map.numbers))
        elif choice_type == 3:
            password_chars.append(random.choice(character_map.symbols))

    return "".join(password_chars)


# function to get a generated_password and return it with error handling and user input
def get_generated_password():
    while True:
        try:
            user_input = (
                input("Generate Password? (Y/N): ").strip().lower()
            )  # gets user input if the user wants to generate a password

            if user_input in ["y", "yes"]:
                try:
                    lenght_of_password = input(
                        "Enter password length [Desfault = 16]: "
                    )

                    password = generate_password(length=int(lenght_of_password)) 

                    return password
                except ValueError:
                    password = generate_password()

                    return password

            elif user_input in ["n", "no"]:
                print("Exiting...")
                exit()

            else:
                print("Invalid input. Please enter Y or N.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()


def store_generated_password(username, password):
   
    passwords_file_path = Path("Passwords/passwords.json")
    
    password_json = {username: password}

    passwords_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    passwords_file_path.write_text(
            json.dumps(
                password_json, indent=4
                )
            )
