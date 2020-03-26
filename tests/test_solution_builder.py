"""
This module tests the class SolutionBuilder
"""
import pytest
from solution_builder import SolutionBuilder


def test_update_free_spaces_sanity():
    """
    Test that after placing a queen the free places update
    """
    builder = SolutionBuilder(4)
    assert builder.get_free_places_in_next_row() == [0, 1, 2, 3]
    builder.place_queen(2)
    assert builder.get_free_places_in_next_row() == [0]
    builder.place_queen(0)
    assert builder.get_free_places_in_next_row() == [3]
    builder.place_queen(3)
    assert builder.get_free_places_in_next_row() == [1]
    builder.place_queen(1)
    assert builder.get_free_places_in_next_row() == []


def test_place_in_taken_space():
    """
    Test to see that an exception is raised when trying to place a queen in a taken place
    """
    with pytest.raises(ValueError):
        builder = SolutionBuilder(2)
        builder.place_queen(0)
        builder.place_queen(1)
