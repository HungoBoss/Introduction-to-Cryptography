# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR Assignment 02   #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

from math import sqrt

def is_prime(n):
    """
    Determines whether a given number is a prime or not. Prints the result into the console.
    """
    prime = False

    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime = True
                break
        
        if prime:
            print(f"{n} is NOT a prime number!")
        else:
            print(f"{n} is prime number!")
    else:
        print(f"{n} is NOT a prime number!")


def main():
    """
    Main function containing all finished tasks.
    """

    # First task
    is_prime(73241)     # shouldn't be a prime number


if __name__ == "__main__":
    main()