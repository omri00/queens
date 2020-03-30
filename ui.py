"""
This module is ui to let the user see the solution to the queens problem
"""
from logic import find_solutions


def show_solutions() -> None:
    """
    Let's the user choose the size of the board and the number of solutions he wishes to see and prints them
    """
    size = receive_int("Choose the board size")
    solutions_num = receive_int("Choose the number of solutions to present")
    solutions = find_solutions(size)
    print_solutions(solutions, solutions_num)


def print_solutions(solutions: list, solutions_num: int) -> None:
    """
    Print a given number of solutions
    :param solutions: The solutions
    :param solutions_num: The number of solutions to print
    """
    for i in range(solutions_num):
        if i >= len(solutions):
            print("That's all of the solution")
            return
        print(f"{i + 1}:\n{solutions[i]}")


def receive_int(msg) -> int:
    """
    Receive an int form the user
    :param msg: A msg to show when asking for the int
    :return: The int from the user
    """
    truly_a_number = False
    while not truly_a_number:
        num = input(f"{msg}\n")
        try:
            num = int(num)
            truly_a_number = True
        except ValueError:
            print(f"{num} isn't an integer!")
    return num


if __name__ == '__main__':
    show_solutions()
