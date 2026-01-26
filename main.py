import random
import character_map

def generate_password(length=16):
    """Generates a random password of a given length."""
    password_chars = []
    
    # Ensure at least one of each type is included for strong passwords (optional but good practice)
    # For now, we will stick to the user's logic of random selection per character slot
    
    for _ in range(length):
        # 0: Uppercase, 1: Lowercase, 2: Numbers, 3: Symbols
        # We use random.choice for cleaner selection from lists
        
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
    while True:
        try:
            user_input = input("Generate Password? (Y/N): ").strip().lower()
            
            if user_input in ['y', 'yes']:
                password = generate_password()
                print(f"Generated Password: {password}")
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
