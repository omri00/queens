"""
This module has the logic to find all solutions to the queens problem
"""
from copy import deepcopy

from solution_builder import SolutionBuilder


def find_solutions(board_size: int) -> list:
    """
    Find all of the solution to the queens problem to a board with a given size
    :param board_size: The size of the board
    :return: All of the solution
    """
    builder = SolutionBuilder(board_size)
    return build_solution(builder)


def build_solution(builder: SolutionBuilder) -> list:
    """
    Build solutions recursively with a SolutionBuilder one row at a time
    :param builder: the solution builder
    :return: A list of all solutions possible with the prev steps
    """
    if builder.is_solution_completed():
        return [builder.get_solution()]
    free_spaces = builder.get_free_places_in_next_row()
    solutions = []
    for next_space in free_spaces:
        new_builder = deepcopy(builder)
        new_builder.place_queen(next_space)
        solutions = union_solutions(solutions, build_solution(new_builder))
    return solutions


def union_solutions(solutions_list1: list, solutions_list2: list) -> list:
    """
    Union 2 lists of solutions.
    Note that this function doesn't check for duplicates in the lists beforehand.
    :param solutions_list1: A first list of solutions
    :param solutions_list2:A second list of solutions
    :return: A union of the 2 lists
    """
    union = solutions_list1[:]
    for solution in solutions_list2:
        if solution not in solutions_list1:
            union.append(solution)
    return union
