"""
This module tests the class Solution
"""
from solution import Solution


def test_equal_solution_comparison():
    """
    Test to see that two equal solution are equal when compared
    """
    solution_1 = Solution([[0, 1], [1, 3], [2, 0], [3, 2]])
    solution_2 = Solution([[0, 2], [1, 0], [2, 3], [3, 1]])
    assert solution_1 == solution_2
    solution_1 = Solution([[0, 1], [1, 3], [2, 0], [3, 2], [4, 4]])
    solution_2 = Solution([[0, 2], [1, 0], [2, 3], [3, 1], [4, 4]])
    assert solution_1 == solution_2


def test_unequal_solution_comparison():
    """
    Test to see that two unequal solution are unequal when compared
    """
    solution_1 = Solution([[0, 1], [1, 3], [2, 0], [3, 2], [4, 4]])
    solution_2 = Solution([[0, 1], [1, 4], [2, 2], [3, 0], [4, 3]])
    assert solution_2 != solution_1
