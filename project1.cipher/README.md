# Vigenère Cipher in Python

This project demonstrates how to use the **Vigenère Cipher** for string
manipulation by encrypting and decrypting messages with a custom key.

## How It Works

The Vigenère cipher is a method of encrypting alphabetic text using a
series of interwoven Caesar ciphers based on the letters of a keyword.

-   **Encryption** shifts letters forward by the key's offsets.
-   **Decryption** shifts them backward using the same key.

## Code Overview

The main function is `vigenere(message, key, direction)`: -
`direction=1` → Encrypt the message - `direction=-1` → Decrypt the
message

Helper functions: - `encrypt(message, key)` → Encrypts a given
message. - `decrypt(message, key)` → Decrypts a given message.

## Example Usage

``` python
# Encrypted text to be decrypted
text = 'mrttaqrhknsw ih puggrur'

# Custom key for the Vigenère cipher
custom_key = 'happycoding'

# Decrypt the text
decrypted = decrypt(text, custom_key)
print("Decrypted text:", decrypted)
# Output: programming is awesome

# Encrypt back to confirm
encrypted = encrypt("programming is awesome", custom_key)
print("Encrypted text:", encrypted)
# Output: mrttaqrhknsw ih puggrur
```

## How to Run

1.  Copy the code into a file, e.g. `cipher.py`
2.  Run it with Python:

``` bash
python cipher.py
```

You can modify the `text` and `custom_key` variables to experiment with
your own messages and keys.

------------------------------------------------------------------------

Happy coding! 🎉
