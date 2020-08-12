# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
message = "guv6Jv6Jz!J6rp5r7Jzr66ntrM"

# The encryption/decryption key:
key = 13

# Whether the program encrypts or decrypts:
mode = "decrypt" # Set to either 'encrypt' or 'decrypt'.
SYMBOLS = ""
# Every possible symbol that can be encrypted:
#A to Z
i = 65
while i <= 90:
    SYMBOLS = SYMBOLS + chr(i)
    i=i+1

#a to z
i = 97
while i <= 122:
    SYMBOLS = SYMBOLS + chr(i)
    i=i+1

#1 - 0
i = 49
while i <= 57:
    SYMBOLS = SYMBOLS + chr(i)
    i=i+1

SYMBOLS = SYMBOLS + "0 !?."

#SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123457890 !?."

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        
        #Handle wraparound, if needed:
        if translatedIndex >=  len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        
        translated = translated + SYMBOLS[translatedIndex]
    else:
        #Append the symbol without encrypting/decrypting:
        translated = translated + symbol

#Output the translated string
print(translated)
pyperclip.copy(translated)