# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 07  #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

from Crypto.PublicKey import DSA
from math import sqrt


def discrete_logarithm(prime, base, arg):
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
    for i in range(1, p):
        if g ** i % p == 1:
            return i
    return -1


def DSA_parameters():
    key = DSA.generate(1024)
    p, q, g = key.domain()
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"g = {g}")


def print_recommendation_for_DSA():
    print("|p| >= 2048 bitů")
    print("|q| >= 224 bitů")


def main():
    # First task
    print("1)")
    print_recommendation_for_DSA()
    print()

    # Second task
    print("2)")
    DSA_parameters()
    print()

    # Third task
    print("3)")
    print(f"q = {find_q(29, 13)}")
    print()

    # Fourth task
    print("4)")
    print(f"x = {discrete_logarithm(34963, 1212, 11144)}")

if __name__ == "__main__":
    main()
