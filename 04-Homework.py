# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR Assignment 04   #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

from random import randint

def congruence(x, y, z):
    """
    Calculates x mod z and y mod z (congruence) and returns True if the results of both equations are the same. If not, returns False.
    """
    if x % z == y % z:
        return True
    else:
        return False


def fermat_test(n):
    """
    Prints whether a given number N is a prime number or not using a Fermat Primality Test.
    """
    for i in range(4):
        a = randint(1, n-1)
        result = congruence(a ** (n-1), 1, n)
        print(f"{a}^{n-1} ≡ 1 mod {n} is {result}")
        if result == False:
            print(f"{n} is NOT a prime number!")
            return
    print(f"{n} is a prime number!")


def main():
    """
    Main function containing all finished tasks.
    """
    fermat_test(87)
    print()
    fermat_test(631)


if __name__ == "__main__":
    main()