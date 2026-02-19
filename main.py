import random # imports the standard random library
import character_map # imports all the arrays of charecters from the charecter_map.py file


# How this works:
# genrate_password fuction genrates a password of a given length (defalt = 16 charecters)
#   it works by creating a array named password_chars
#   then does a for loop for in range of lenght (default = 16)
#   creates a choice_type variable that randomly chooses a number between 0 to 4
#   The numbers correspond to arrays of charecters: 1: Uppercase Letters, 2: Lowercase Letters, 3: Numbers and 4: Symbols
#   it then loops over it as many times the lenght is
#   upon loop end it then return a string by joining all the chars stored in the password variable


# main function takes user input if they want to genrate a password
#   for error protection it uses a try-except block:
#       in the try block it:
#           if 'y' or 'yes' then it calls the generate_password function and prints the password 
#           if 'n' or 'no' then it prints "exiting" and then breaks
#           else it prints "Invalid input. Please enter Y or N."
#       in the except block:
#           if user terminates the program forcefully (KeyboardInterrupt) it prints exiting and breaks


def generate_password(length=16):
    password_chars = []

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

def main():
    print("PyPass")
    
    while True:
        try:
            user_input = input("Generate Password? (Y/N): ").strip().lower()
            
            if user_input in ['y', 'yes']:
               
                try:

                    lenght_of_password = input("Enter password length [Desfault = 16]: ")

                    password = generate_password(length = int(lenght_of_password))

                    print(f'Generated Password: {password}')
                
                except ValueError:

                    password = generate_password()

                    print(f'Generated Password: {password}')
                    
            elif user_input in ['n', 'no']:
                print("Exiting...")
                break

            else:
                print("Invalid input. Please enter Y or N.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
