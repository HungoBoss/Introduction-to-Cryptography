# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 07  #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

from Crypto.PublicKey import DSA

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

    # Second task
    print("2)")
    DSA_parameters()


if __name__ == "__main__":
    main()