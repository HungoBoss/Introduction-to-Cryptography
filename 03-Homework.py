# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR Assignment 03   #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

from math import sqrt

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


def euler(n):
    """
    Calculates and returns the result of the Euler Totient Function.
    """
    result = 1

    for i in range(2, n):
        if calculateGCD(i, n) == 1:
            result += 1
    
    return result


def modulo(x, y):
    """
    Returns x mod y. 
    """
    return x % y


def congruence(x, y, z):
    """
    Calculates x mod z and y mod z (congruence) and returns True if the results of both equations are the same. If not, returns False.
    """
    if x % z == y % z:
        return True
    else:
        return False


def modular_inversion(a, n):
    """
    Calculates and returns the modular inversion of a mod n. Returns -1 if the inversion doesn't exists.
    """
    for i in range(1, n):
        if (((a % n) * (i % n)) % n == 1):
            return i
    return -1


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
    """
    Main function containing all finished tasks.
    """

    # First task
    print("1)")
    print(f"Euler (21): {euler(21)}")
    print(f"Euler (56): {euler(56)}")
    print(f"Euler (91): {euler(91)}")
    print(f"Euler (243): {euler(243)}\n")

    # Second task
    print("2)")
    print("Pokud jsou A a N nesoudělná [tj. GCD(a, n) = 1], pak existuje inverzní prvek, kterým lze celou rovnici vynásobit a tudíž kongruence platí. V případě, že A a N nejsou soudělná, kongruence neplatí.\n")

    # Third task
    print("3)")
    print(f"17 mod 6 = {modulo(17, 6)}")
    print(f"-11 mod 7 = {modulo(-11, 7)}")
    print(f"115 mod 17 = {modulo(115, 17)}")
    print(f"-1 mod 9 = {modulo(-1, 9)}")
    print(f"44 mod 13 = {modulo(44, 13)}")
    print(f"56 mod 14 = {modulo(56, 14)}")
    print(f"421 mod 21 = {modulo(421, 21)}\n")

    # Fourth task
    print("4)")
    print(f"Congruence (-5 ≡ 12 mod 18): {congruence(-5, 12, 18)}")
    print(f"Congruence (-16 ≡ 54 mod 35): {congruence(-16, 54, 35)}")
    print(f"Congruence (-90 ≡ 26 mod 16): {congruence(-90, 26, 16)}\n")

    # Fifth task
    print("5)")
    print(f"Modular inversion (a = 5, n = 9): {modular_inversion(5, 9)}")
    print(f"Modular inversion (a = 4, n = 11): {modular_inversion(4, 11)}")
    print(f"Modular inversion (a = 8, n = 13): {modular_inversion(8, 13)}")
    print(f"Modular inversion (a = 17, n = 47): {modular_inversion(17, 47)}")
    print(f"Modular inversion (a = 85, n = 17): {modular_inversion(85, 17)}\n")

    # Sixth task
    print("6)")
    print(f"Generators: {cyclic_group(13)}")


if __name__ == "__main__":
    main()