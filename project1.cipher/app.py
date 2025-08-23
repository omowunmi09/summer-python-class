#Learn string manipulation by building a cipher
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')




# Learn string manipulation by building a cipher

# Encrypted text to be decrypted
text = 'mrttaqrhknsw ih puggrur'

# Custom key for the Vigenère cipher
custom_key = 'happycoding'

# Function to handle both encryption and decryption using the Vigenère cipher
def vigenere(message, key, direction=1):  # direction=1 for encryption, -1 for decryption
    key_index = 0  # Index to keep track of which key character to use
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # The alphabet for reference
    final_message = ''  # Initialize the final output message

    # Loop through each character in the message
    for char in message.lower():  # Convert the message to lowercase for consistency

        # If the character is not a letter (e.g., space or punctuation), keep it unchanged
        if not char.isalpha():
            final_message += char  # Append non-letter character directly
        else:        
            # Get the corresponding character from the key
            key_char = key[key_index % len(key)]  # Wrap around if key is shorter than the message
            key_index += 1  # Move to the next key character for the next letter

            # Calculate the offset using the key character's position in the alphabet
            offset = alphabet.index(key_char)

            # Find the index of the current message character
            index = alphabet.find(char)

            # Calculate new index using direction (1 for encryption, -1 for decryption)
            new_index = (index + offset * direction) % len(alphabet)

            # Append the new encrypted/decrypted character
            final_message += alphabet[new_index]
    
    # Return the final encrypted or decrypted message
    return final_message

# Wrapper function to encrypt using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)

# Wrapper function to decrypt using the Vigenère cipher
def decrypt(message, key):
    return vigenere(message, key, -1)  # Use direction = -1 for decryption

# Print the original encrypted text
print(f'\nEncrypted text: {text}')

# Print the key used for decryption
print(f'Key: {custom_key}')

# Decrypt the text using the custom key
decryption = decrypt(text, custom_key)

# Print the decrypted message
print(f'\nDecrypted text: {decryption}\n')
