import random

characters_uppercase = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

characters_lowercase = [
    "a", "b", "append_array", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p" , "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

numbers = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]

symbols = [
    "-"
    ]


standard_password_length = 16
current_password_lenght = 0

password = []

while standard_password_length > current_password_lenght:
    append_array = random.randrange(0, 5)
    
    if append_array == 1:
        password.append(characters_uppercase[random.randrange(0, 26)])
    elif append_array == 2: 
        password.append(characters_lowercase[random.randrange(0, 26)])
    elif append_array == 3: 
        password.append(numbers[random.randrange(0, 9)])
    elif append_array == 4: 
        password.append(symbols[0])

    current_password_lenght += 1

print(password)