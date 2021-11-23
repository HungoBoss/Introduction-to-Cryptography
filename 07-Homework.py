# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 07  #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

from Crypto.PublicKey import DSA
from math import sqrt


def diffie_hellman(p, g, A, B):
    """
    Base algorithm for Diffie-Hellman.
    """
    b = discrete_logarithm(p, g, B)
    a = discrete_logarithm(p, g, A)
    
    K = A ** b % p
    K_2 = B ** a % p

    print(f"a = {a}, b = {b}")
    
    if K == K_2:
        return K

    
def discrete_logarithm(prime, base, arg):
    """
    Discrete algorithm using a baby-step giant-step approach to get the value of a discrete logarithm.
    """
    result = 0
    current = 1
    while result < prime - 1:
        if (current-arg) % prime == 0:
            return(result)
        else:
            current *= base
            result += 1
    return -1


def find_q(p, g):
    """
    Function that uses brute-force approach to find parameter Q in DSA.
    """
    for i in range(1, p):
        if g ** i % p == 1:
            return i
    return -1


def DSA_parameters():
    """
    Function for generating DSA parameters with the prime number of the length at least 1024 bits. Using a nasty trick to display the domain of characters.
    """
    key = DSA.generate(1024)
    p, q, g = key.domain()
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"g = {g}")


def print_recommendation_for_DSA():
    """
    Function for printing recommended p and q for DSA.
    """
    print("|p| >= 2048 bitů")
    print("|q| >= 224 bitů")

    
def is_generator(x, n):
    """
    Utility function that determines whether X is generator of a cyclic group or not.
    """
    arr = [j for j in range(1, n)]

    for i in range(n):
        subresult = x ** i % n
        if subresult in arr:
            arr.remove(subresult)

    if len(arr) == 0:
        return True
    else:
        return False


def cyclic_group(n):
    """
    Return the amount of generators of a cyclic group.
    """
    generators = 0

    for i in range(1, n):
        if is_generator(i, n):
            generators += 1
            print(f"Generator found: {i}")
    
    return generators
    

def main():
    # First task
    print("1)")
    print_recommendation_for_DSA()

    # Second task
    print("\n2)")
    DSA_parameters()

    # Third task
    print("\n3)")
    print(f"q = {find_q(29, 13)}")

    # Fourth task
    print("\n4)")
    print(f"x = {discrete_logarithm(34963, 1212, 11144)}")

    # Fifth task
    print("\n5)")
    cyclic_group(17)

    # Sixth task
    print("\n6)")
    print(f"K' = K = {diffie_helman(105541, 26, 84035, 22250)}")

if __name__ == "__main__":
    main()
