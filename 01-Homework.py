# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR Assignment 01   #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

def caesar_cipher_encrypt(message, shift):
    """
    Encrypts the input message using a Caesar cipher with a given shift and 
    returns the result.
    """
    result = ""

    for i in range(len(message)):
        char = message[i]

        if char == " ":
            result += char
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    
    return result

first_msg = "Zaklady kryptografie"
shift = 2

print(f"Original message: {first_msg}")
print(f"Shift pattern: {shift}")
print(f"Cipher: {caesar_cipher_encrypt(first_msg, shift)}")