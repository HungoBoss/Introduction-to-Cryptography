# # # # # # # # # # # # # # #
#                           #
#   BPC-ZKR  Assignment 05  #
#   Author: Hung Ngo Quang  #
#                           #
# # # # # # # # # # # # # # #

def main():
    # First task
    print("1) ")
    print("Budeme vycházet z Malé Fermatovy věty:\n\tx^(p-1) ≡ 1 (mod p)")
    print("Obě dvě strany můžeme vynásobit x^(-1), čímž dostaneme:\n\tx^(p-2) ≡ x^(-1) mod p")
    print("Převedením (mod p) na levou stranu (komutativní operace), pak získáme vztah:\n\tx^(p-2) mod p ≡ x^(-1)")

if __name__ == "__main__":
    main()