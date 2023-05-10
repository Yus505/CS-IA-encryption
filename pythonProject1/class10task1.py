encryption_dict = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}

def encrypt(message, encryption_dict):
    encrypted_message = ''
    for letter in message:
        if letter in encryption_dict:
            encrypted_message += encryption_dict[letter]
        else:
            encrypted_message += letter
    return encrypted_message

def decrypt(message, encryption_dict):
    decryption_dict = {v: k for k, v in encryption_dict.items()}
    decrypted_message = ''
    for letter in message:
        if letter in decryption_dict:
            decrypted_message += decryption_dict[letter]
        else:
            decrypted_message += letter
    return decrypted_message

message = ''
encrypted_message = encrypt(message, encryption_dict)
decrypted_message = decrypt(encrypted_message, encryption_dict)
print('Original message:', message)
print('Encrypted message:', encrypted_message)
print('Decrypted message:', decrypted_message)
