'''

PROGRAM: caesarCipher.py
AUTHOR: Danielle Lamb
DATE: March 3, 2020
PURPOSE: Encrypt or decrypt a plaint text string shifting by
         the string indexes based on a key length input by user.

'''

import string # Import string library to generate character list(s)

while True:

# Stores message from user
    message = input("Enter message to be encrypted or decrypted: ")

    # Stores key size from user
    # If entry is not integer, throws error and forces user to try again
    while True:
        try:
            key = int(input("Enter the symmetric key size: "))
            break
        except ValueError as error:
            print(error)
            print("Key must be an int type, please try again.")

    # Stores choice of mode from user
    mode = input("Enter the mode - [encrypt or decrypt]: ")

    # Stores custom charset (ASCII letters, digits, special chars, and whitespace)
    SYMBOLS = string.ascii_letters + string.digits + string.punctuation + " "

    # Stores output of translated message
    translated = ""

    for symbol in message: # Loops through every character in message
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol) # Checks index of symbol in charset

            # If mode is encrypt, index is added by key
            if mode in ['encrypt','Encrypt','e','E']:
                translatedIndex = symbolIndex + key
            # If mode is decrypt, index is subtracted by key
            elif mode in ['decrypt','Decrypt','d','D']:
                translatedIndex = symbolIndex - key

            # Handle wrap around if needed
            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            # Handle when message starts with 'a' in decrypting
            elif translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        # If symbol is outside of charset, print symbol within translated message
        else:
            translated += symbol

    print(translated)
        


