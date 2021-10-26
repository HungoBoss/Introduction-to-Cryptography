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


def fermat_test(n, k):
    """
    Prints whether a given number N is a prime number or not using a Fermat Primality Test. The test is computed k-times (each time for a different result)
    """
    for i in range(k):
        a = randint(1, n-1)
        result = congruence(a ** (n-1), 1, n)
        print(f"{a}^{n-1} ≡ 1 mod {n} is {result}")
        if result == False:
            print(f"\t{n} is NOT a prime number!")
            return
    print(f"\t{n} is a prime number!")


def miller_rabin_test(n, k):
    """
    Prints whether a given number N is a prime number or not using a Miller-Rabin Primality Test. The test is computed k-times (each time for a different result)
    """
    s = 0
    r = n - 1

    # Determining r and s
    while r % 2 == 0:
        r >>= 1         # Binary shift acts the same way as division by 2
        s += 1
    assert(2 ** s * r == n - 1)

    def is_composite(a):
        """
        Utility function that determines whether a given A is a composite number or not. Returns True in case it is and False in case it is not.
        """
        if pow(a, r, n) == 1:       # Equals to (a ** d) % n
            return False
        for i in range(s):
            if pow(a, 2**i * r, n) == n-1:
                return False
        return True

    for i in range(k):
        a = randint(2, n)
        if is_composite(a):
            return False

    return True


def lucas_lehmer_test():
    """
    Generates a Marsenne number and finds out whether it is prime or not.
    """
    s = randint(7, 19)
    print(f"Generated s = {s}")
    n = (2**s) - 1
    print(f"Value of N: {n}")
    
    u = []              # List holding u numbers at each and every index
    u.append(4)

    for i in range(1, (s-2)+1):
        u_i = ((u[i-1]) ** 2 - 2) % n
        u.append(u_i)

    if u[s-2] == 0:
        print(f"{n} is a prime number!")
    else:
        print(f"{n} is NOT a prime number!")


def square_and_multiply(x, y):
    """
    Calculates and returns the value of X pow Y using a Square and multiply algorithm.
    """
    exp = bin(y)
    result = x

    for i in range(3, len(exp)):
        result *= result
        if(exp[i:i+1] == '1'):
            result = result * x
    
    return result


def main():
    """
    Main function containing all finished tasks.
    """
    # First task
    print("1) ")
    fermat_test(87, 4)
    print()
    fermat_test(631, 4)
    print()

    # Second task
    print("2) ")
    print(f"Is 313 a prime number: {miller_rabin_test(313, 2)}")
    print()
    print(f"Is 847 a prime number: {miller_rabin_test(847, 2)}")
    print()

    # Third task
    print("3) ")
    lucas_lehmer_test()
    print()
    lucas_lehmer_test()
    print()

    # Fourth task
    print("4) ")
    print("Každé složené číslo N je součin prvočísel p1 a p2, přičemž platí N = p1 * p2.\nV případě, že by obě čísla p byla stejná, tak bude n = p^2 a tudíž bude platit, že p = sqrt(n).\nPokud nebudou čísla p1 a p2 nabývat stejné hodnoty, pak bude vždy jedno z prvočísel menší, než sqrt(n).\n")


    # Fifth task
    print("5) ")
    print(f"5^39 mod 23 = {square_and_multiply(5, 39) % 23}")

if __name__ == "__main__":
    main()