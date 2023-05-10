import string
import random

alphabet = string.ascii_lowercase
key = ''.join(random.sample(alphabet, len(alphabet)))

def encrypt(message, key):
    encryption_dict = dict(zip(alphabet, key))
    encrypted_message = ''
    for letter in message:
        if letter in encryption_dict:
            encrypted_message += encryption_dict[letter]
        else:
            encrypted_message += letter
    return encrypted_message

def decrypt(message, key):
    decryption_dict = dict(zip(key, alphabet))
    decrypted_message = ''
    for letter in message:
        if letter in decryption_dict:
            decrypted_message += decryption_dict[letter]
        else:
            decrypted_message += letter
    return decrypted_message

message = 'IB Internal Assesment'
key = ''.join(random.sample(alphabet, len(alphabet)))
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print('Original message:', message)
print('Key:', key)
print('Encrypted message:', encrypted_message)
print('Decrypted message:', decrypted_message)
