import random
import charecter_map

standard_password_length = 16
current_password_lenght = 0
password = []

def create_password(standard_password_length = standard_password_length, current_password_lenght = current_password_lenght):
    while standard_password_length > current_password_lenght:
        append_array = random.randrange(0, 5)

        if append_array == 1:
            password.append(charecter_map.characters_uppercase[random.randrange(0, 26)])
        elif append_array == 2: 
            password.append(charecter_map.characters_lowercase[random.randrange(0, 26)])
        elif append_array == 3: 
            password.append(charecter_map.numbers[random.randrange(0, 9)])
        elif append_array == 4: 
            password.append(charecter_map.symbols[0])

        current_password_lenght += 1


def main() :
    print("Password Genrator")
    
    choice = input("Genrate Password [Y/N]: ")

    avalaible_inputs = ["y", "Y", "Yes", "YES", "yes"]

    if choice == avalaible_inputs[0]:
        create_password()
        return(password)
    elif choice == avalaible_inputs[1]:
        create_password()
        return(password)
    elif choice == avalaible_inputs[2]:
        create_password()
        return(password)
    elif choice == avalaible_inputs[3]:
        create_password()
        return(password)
    elif choice == avalaible_inputs[4]:
        create_password()
        return(password)
    else:
        return("The program has been terminated by user")

print(main())