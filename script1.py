######## encruption program

import random
import string


chars = " "+string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"Chars:{chars}")
#fprint(f"Key  :{key}")

# Encryption
plain_text = input("Text to encrypt: :")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Cipher text: {cipher_text}")

# Decryption
cipher_text = input("Text to decrypt: :")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]


print(f"original text: {plain_text}")