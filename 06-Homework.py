# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 06  #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

from math import gcd
from sympy import isprime

def pollard_algorithm(n):
    base = 2
    i = 2

    while True:
        base = (base ** i) % n
        d = gcd((base-1), n)

        if d > 1:
            return d
            
        i += 1


def find_prime_factors(n):
    num = n
    ans = []

    while True:
        d = pollard_algorithm(num)
        ans.append(d)
        r = int(num / d)

        if isprime(r):
            ans.append(r)
            break
        else:
            num = r

    return ans


def find_private_key(n, public_key):
    factors = find_prime_factors(n)
    print(f"Factors of 129621733357 are: {factors}")

    phi_n = (factors[0] - 1) * (factors[1] - 1)
    print(f"Φ(n) = {phi_n}")

    private_key = pow(public_key, -1, phi_n)
    
    return private_key


def decypher_rsa(cryptogram, n, private_key):
    message = square_and_multiply_always(cryptogram, private_key, n)
    str_message = str(message)
    letters = []

    for i in range(len(str_message) // 2):
        letter = str_message[2*i:(2*i)+2]
        letters.append(letter)

    decyphered_message = ""

    for i in range(len(letters)):
        decyphered_message += chr((int(letters[i]) + 65 - 1))

    print(letters)

    print(decyphered_message)


def square_and_multiply_always(base, exp, mod):
    R0=1
    R1 = base
    c = '{0:b}'.format(exp)
    i=len(c)-1
    t=0
    c=c[::-1]
    while(i>=0):
        if(t==0):
            Rt=R0
        elif(t==1):
            Rt=R1
        else:
            print("t != 0 or 1")
        R0=(R0*Rt)%mod
        d=int(c[i])
        t=(t^d)
        i=i-1+t
    return R0


def basic_euclidean_algorithm(a, b):
    """
    Recursive function that calculates the GCD of given numbers a and b using a basic version of Euclidean algorithm. Returns the value of GCD.
    """
    if a == 0:
        return b
    
    return basic_euclidean_algorithm(b % a, a)


def extended_euclidean_algorithm(a, b):
    """
    Calculate the inverse element using an Extended Euclidean algorithm.
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean_algorithm(b % a, a)
        return (g, x - (b // a) * y, y)


def main():
    # First task
    print("1)")
    print(f"GCD(10547, 1651) = {basic_euclidean_algorithm(10547, 1651)}\n")
    
    # Second task
    print("2)")
    _, x, _ = extended_euclidean_algorithm(345, 577)
    print(f"345^(-1) mod 577 = {x % 577}\n")

    # Third task
    print("3)")
    _, x, _ = extended_euclidean_algorithm(16, 357)
    print(f"16^(-1) mod 357 = {x % 357}\n")

    # Fourth task
    print("4)")
    print(f"Private key: {find_private_key(129621733357, 9)}")

    # Fifth task
    print("5)")
    decypher_rsa(605710893992533, 3324847060925479, 1813552871415011)


if __name__ == "__main__":
    main()