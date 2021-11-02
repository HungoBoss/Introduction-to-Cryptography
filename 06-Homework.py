# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 05  #
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


def main():
    # First task
    print("1) ")
    print(f"GCD(10547, 1651) = {basic_euclidean_algorithm(10547, 1651)}")


if __name__ == "__main__":
    main()