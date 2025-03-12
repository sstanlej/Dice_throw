import os
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_sides():
    print("Input number of sides: ")
    sides = input(">> ")
    try:
        sides = int(sides)
        assert sides > 0
        return sides
    except Exception:
        print('Wrong number of sides, must be positive intiger\n')


def input_operation():
    print("Input number 0-2:")
    try:
        n = int(input(">> "))
        if n in [0, 1, 2]:
            return n
    except Exception:
        print("Wrong operation")


def throw(sides):
    cls()
    print(f'Throwing {sides}-sided die...\n')
    x = random.randint(1, sides)
    size = len(str(x))
    print('Result:')
    print('='*(4+size))
    print(f'= {x} =')
    print('='*(4+size))


def menu(sides):
    print(f'Number of sides: {sides}\n')
    print('What do you want to do?')
    print('0. Exit')
    print('1. Throw')
    print('2. Input number of sides\n')

    operation = input_operation()
    while operation is None:
        operation = input_operation()
    if operation == 0:
        print('Goodbye\n')
        return 0
    elif operation == 1:
        throw(sides)
        menu(sides)
    elif operation == 2:
        main()


def main():
    cls()
    sides = input_sides()
    while sides is None:
        sides = input_sides()
    menu(sides)


if __name__ == "__main__":
    main()
