from icecream import ic
from tools.col import myzip
from tools.numbers.simp import add, subtract
from tools.numbers.comp import sumofdigits, ispal

import enum as enum
import os


class Actions(enum.Enum):
    ADD = 1
    SUBTRACT = 2
    SUM = 3
    PALINDROME = 4
    ZIP = 5
    EXIT = 6


def menu():  
    print("==Test Menu==")
    for x in Actions:
        print(f'{x.name} - {x.value}')
    return input("Enter your selection: ")

simp_called = False

# Checks if functions from the simp module have been called.
def check_simp_called():
    if not simp_called:
        raise Exception("Call at least one function in simp module first. (ADD or SUBTRACT)")


# two collections for the zip function
it1 = [1, 2, 3, 5]
it2 = ['a', 'b', 'c', 'd']


def main():
    global simp_called

    while True:
        user_selection = menu()

        if Actions(int(user_selection)) == Actions.ADD:
            os.system('cls')
            add(2, 2)
            simp_called = True
        elif Actions(int(user_selection)) == Actions.SUBTRACT:
            os.system('cls')
            check_simp_called()
            subtract(10, 2)
        elif Actions(int(user_selection)) == Actions.SUM:
            os.system('cls')
            check_simp_called()
            sumofdigits(12345)
        elif Actions(int(user_selection)) == Actions.PALINDROME:
            os.system('cls')
            check_simp_called()
            ispal(1221)
        elif Actions(int(user_selection)) == Actions.ZIP:
            os.system('cls')
            check_simp_called()
            myzip(it1, it2)
        elif Actions(int(user_selection)) == Actions.EXIT:
            break



if __name__ == "__main__":
    main()
