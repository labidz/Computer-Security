import random
import string

def encrypt(key_lower, message):
    alphabet = string.ascii_lowercase
    table_lower = str.maketrans(alphabet, key_lower)
    
    encrypted_message = ""

    for char in message:
        if char >='a' and char <='z':
            encrypted_char = char.translate(table_lower)
            encrypted_message += encrypted_char
        else:
            char = char.lower()
            encrypted_char = char.translate(table_lower)
            encrypted_char = encrypted_char.upper()
            encrypted_message += encrypted_char

    return encrypted_message

def decrypt(key, encrypted_message):
    alphabet = string.ascii_lowercase
    table = str.maketrans(key, alphabet)
    decrypted_message = ""

    for char in encrypted_message:
        if char.islower():
            decrypted_char = char.translate(table)
            decrypted_message += decrypted_char
        elif char.isupper():
            char = char.lower()
            decrypted_char = char.translate(table)
            decrypted_message += decrypted_char.upper()
        else:
            decrypted_message += char

    return decrypted_message

def shuffle_key(key):
    key_list = list(key)
    random.shuffle(key_list)
    return ''.join(key_list)

if __name__ == "__main__":
    key_lower = "abcdefghijklmnopqrstuvwxyz"
    print(key_lower)

    key_lower = shuffle_key(key_lower)
    print(key_lower)

    message = input()
    enms = encrypt(key_lower, message)
    print(enms)
    
    print(decrypt(key_lower, enms))
