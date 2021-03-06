from solution import Solution


class SolutionBuilder:
    """
    A class that helps build a solution to the queens' problem
    """

    def __init__(self, size: int):
        self.__size = size
        self.__queens_coords = []
        self.__free_spaces = [[i for i in range(size)] for _ in range(size)]

    def get_solution(self):
        """
        :return: The solution if it's complete and None if not
        """
        return Solution(self.__queens_coords)

    def get_free_places_in_next_row(self) -> list:
        """
        :return: The free places in the next row
        """
        if not self.__free_spaces:
            return []
        return self.__free_spaces[0]

    def is_solution_completed(self) -> bool:
        """
        :return: True if the solution is completed and all of the queens were space
        """
        return len(self.__queens_coords) == self.__size

    def place_queen(self, queen_space_column: int) -> None:
        """
        Place a queen in the next row in a given column and update the free space
        :param queen_space_column: the queens column
        """
        if queen_space_column not in self.__free_spaces[0]:
            raise ValueError("A queen was placed in a taken space")
        queen_space_row = len(self.__queens_coords)
        self.__queens_coords.append([queen_space_row, queen_space_column])  # Saves the space of the new queen
        self._update_free_spaces(queen_space_column)

    def _update_free_spaces(self, queen_space_column: int) -> None:
        """
        Update the free spaces after placing a queen in the first row and in the given column
        :param queen_space_column: The column of the new queen
        """
        for i, row in enumerate(self.__free_spaces):
            if queen_space_column in row:
                row.remove(queen_space_column)  # Update the column
            if queen_space_column + i in row:
                row.remove(queen_space_column + i)  # Update the right diagonal
            if queen_space_column - i in row:
                row.remove(queen_space_column - i)  # Update the left diagonal
        self.__free_spaces = self.__free_spaces[1:]  # Update the row
