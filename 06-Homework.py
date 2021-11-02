# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 06  #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

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
    print(f"GCD(10547, 1651) = {basic_euclidean_algorithm(10547, 1651)}")
    
    # Second task
    print("2)")
    _, x, _ = extended_euclidean_algorithm(345, 577)
    print(f"345^(-1) mod 577 = {x % 577}")


if __name__ == "__main__":
    main()