# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 05  #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #


def eulers_theorem(a, e, n):
    """
    Returns the result of a given a^e mod n using Euler's theorem.
    """
    if n < 2:
        print("N has to be higher than 2!")
        return
    
    if calculateGCD(a, n) != 1:
        print("GCD(a, n) has to be equal to 1!")
        return
    
    base = a % n
    exp = e % euler(n)

    print(f"Rewritten as {base}^{exp} mod {n}")

    return base ** exp % n


def chinese_remainder_theorem(a, m):
    M = 1
    for i in range(len(m)):
        M *= m[i]
    
    N = []
    for i in range(len(m)):
        Ni = M // m[i]
        N.append(Ni)

    L = []
    for i in range(len(m)):
        Li = pow(N[i], -1, m[i])
        L.append(Li)
    
    result = 0
    for i in range(len(m)):
        result += a[i] * N[i] * L[i]
    
    print(f"M = {M}")
    print(f"N = {N}")
    print(f"L = {L}")

    return result % M

def main():
    # First task
    print("1) ")
    print("Budeme vycházet z Malé Fermatovy věty:\n\tx^(p-1) ≡ 1 (mod p)")
    print("Obě dvě strany můžeme vynásobit x^(-1), čímž dostaneme:\n\tx^(p-2) ≡ x^(-1) mod p")
    print("Převedením (mod p) na levou stranu (komutativní operace), pak získáme vztah:\n\tx^(p-2) mod p ≡ x^(-1)")

    # Second task
    print("2) ")
    print(f"497^(10701) mod 27")
    print(f"\tResult: {eulers_theorem(479, 10701, 27)}")

    # Third task
    print("3) ")
    print("x ≡ 11 (mod 15)")
    print("x ≡ 5 (mod 22)")
    print(f"\tResult: {chinese_remainder_theorem([11, 5], [5, 22])}")

    # Fourth task
    print("4) ")
    print("x ≡ -4 (mod 35)")
    print("x ≡ 15 (mod 43)")
    print(f"\tResult: {chinese_remainder_theorem([-4, 15], [35, 43])}")

    # Fifth task
    print("5) ")
    print("x ≡ 11 (mod 17)")
    print("x ≡ -8 (mod 67)")
    print("x ≡ 10 (mod 47)")
    print(f"\tResult: {chinese_remainder_theorem([11, -8, 10], [17, 67, 47])}")


# Utility functions
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

if __name__ == "__main__":
    main()