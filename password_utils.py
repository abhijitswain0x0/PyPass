import random
import character_map

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


def get_generated_password():
    
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
                    exit()

                else:
                    print("Invalid input. Please enter Y or N.")
            except KeyboardInterrupt:
                print("\nExiting...")
                exit()
   
