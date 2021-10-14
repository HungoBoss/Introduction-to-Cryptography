# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR Assignment 03   #
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


def calculateGCD(x, y):
    """
    Calculates and returns the GCD value of X and Y.
    """
    if x > y:
        smaller = y
    else:
        smaller = x
    
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    
    return gcd


def calculateLCM(x, y):
    """
    Calculates and returns the LCM value of X and Y.
    LCM can be calculated by the multiplication of X and Y devided by the GCD of those two numbers.
    """
    return (x * y / calculateGCD(x, y))


def euler(n):
    """
    Calculates and returns the result of the Euler Totient Function.
    """
    result = 1

    for i in range(2, n):
        if calculateGCD(i, n) == 1:
            result += 1
    
    return result


def main():
    """
    Main function containing all finished tasks.
    """

    # First task
    print(f"Euler (21): {euler(21)}")
    print(f"Euler (56): {euler(56)}")
    print(f"Euler (91): {euler(91)}")
    print(f"Euler (243): {euler(243)}")


if __name__ == "__main__":
    main()