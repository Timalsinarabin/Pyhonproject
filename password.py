import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num='0123456789'
    special='!@#$%^&*()_+-=[]{}|;:,.<>?'
    password=''
    for i in range(length):
        password += random.choice(characters)+random.choice(cap)+random.choice(num)+random.choice(special)
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

password = generate_password(4)
print("Generated Password:", password)
