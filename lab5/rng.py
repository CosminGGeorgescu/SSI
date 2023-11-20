import os
import random
import secrets
import string
import keyring
import getpass

def generate_password():
    password_list = [random.choice(string.ascii_lowercase), 
                     random.choice(string.ascii_uppercase), 
                     random.choice(['.', '!', '$', '@']), 
                     ''.join(random.choice(string.ascii_letters + string.digits + '.!$@') for _ in range(7))]
    random.shuffle(password_list)
    
    return ''.join(password_list)


def generate_url_safe_string(length):
    length = max(32, length)
    url_safe_characters = string.ascii_letters + string.digits + '-._~'
    url_safe_string = ''.join(secrets.choice(url_safe_characters) for _ in range(length))
    return url_safe_string


def generate_hex_token(length):
    length = max(32, length)
    token = secrets.token_hex(length // 2)  # Each byte in hexadecimal is represented by 2 characters
    while len(token) < length:
        token += secrets.token_hex((length - len(token)) // 2)
    return token[:length]

if __name__ == "__main__":
    os.system("clear")
    while True:
        print("generate\n1. password\n2. url-safe string\n3. hex token\n4. binary key\n5. compare strings\n6. add credentials\nyour choice: ", end='')
        match int(input()):
            case 1:
                print("Password: ", generate_password())
            case 2:
                print("URL: ", generate_url_safe_string(int(input("URL length: "))))
            case 3:
                print("Hex Token: ", generate_hex_token(int(input("Token length: "))))
            case 4:
                print("Binary key: ", os.urandom(16))
            case 5:
                print(secrets.compare_digest(input(), input()))
            case 6:
                keyring.set_password(input("Service: "), input("Username: "), getpass.getpass("Password: "))
        input("Press any key")
        os.system("clear")
