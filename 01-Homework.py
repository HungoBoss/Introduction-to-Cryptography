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


def caesar_cipher_decrypt(message):
    """
    Decrypts the input message using a brute-force approach and prints all the
    possible variants.
    """
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(alphabet)):
        print(f"Key #{i}: {caesar_cipher_encrypt(message, i)}")


def vernam_cipher(message, key):
    """
    Decrypts the message using Vernam's cipher with a given binary key.
    """
    result = ""

    for i in range(len(message)):
        if message[i] == " ":
            result += " "
        elif message[i] != key[i]:
            result += "1"
        else:
            result += "0"

    return result


def main():
    # First task
    first_msg = "Zaklady kryptografie"
    shift = 2

    print("1) ")
    print(f"Original message: {first_msg}")
    print(f"Shift pattern: {shift}")
    print(f"Cipher: {caesar_cipher_encrypt(first_msg, shift)}\n")


    # Second task
    second_msg = "01100010 01101100 01101111 01101011"
    key = "01110100 01101001 01110011 01101011"

    print("2) ")
    print(f"Encrypted message: {vernam_cipher(second_msg, key)}\n")


    # Third task
    third_msg = "vmwxqacrq lwuikq cswtg dgxzikwdidiu rm aiuwabibv"
    print("3) ")
    caesar_cipher_decrypt(third_msg)
    print("note: Correct key is #18\n")


    # Fourth task
    answer = "Na každou pozici lze vložit číslice od 0 do 9 (tj. 10 číslic). Celkový počet variant je proto 10^4. Pravděpodobnost na správné zvolení PINu na první pokus je 1/10^4, což je 0,01%."
    print("4) ")
    print(answer + "\n")

if __name__ == "__main__":
    main()