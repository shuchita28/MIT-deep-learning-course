def encrypt(text, key):
  
    encrypted_text = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        encrypted_text = encrypted_text + alphabet[idx]

    return encrypted_text

def decrypt(text, key):
  
    decrypted_text = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) - key) % len(alphabet)
        decrypted_text = decrypted_text + alphabet[idx]

    return decrypted_text
  
# Check the encryption function with the shift equals to 10
print(encrypt("datacamp", 10))

# Check the decryption function with the shift equals to 10
print(decrypt("datacamp", 10))

