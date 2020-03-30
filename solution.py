X_COORD_INDEX = 0
Y_COORD_INDEX = 1
LEFT = 0
RIGHT = 1
NUMBER_SIDES_IN_SQUARE = 4


class Solution:
    """
    A class that represent a finished solution. The
    Note that this class doesn't check if the solution is correct and
    """
    QUEEN_CHAR = 'Q'
    EMPTY_SPACE_CHAR = "*"

    def __init__(self, queens_coords):
        self.__queens_coords = queens_coords
        self.__size = len(queens_coords)
        self._sort_queens()

    def __str__(self):
        str_representation = ""
        for i in range(self.__size):
            for j in range(self.__size):
                str_representation += self.QUEEN_CHAR if [i, j] in self.__queens_coords else self.EMPTY_SPACE_CHAR
            str_representation += '\n'
        return str_representation

    def __eq__(self, other):
        for i in range(NUMBER_SIDES_IN_SQUARE):
            if self.__queens_coords == other.__queens_coords:
                return True
            self._mirror()
            if self.__queens_coords == other.__queens_coords:
                return True
            self._rotate(LEFT) if i % 2 == 0 else self._rotate(RIGHT)

    def _mirror(self) -> None:
        """
        Mirror the solution
        """
        for queen_coords in self.__queens_coords:
            queen_coords[Y_COORD_INDEX] = self.__size - queen_coords[Y_COORD_INDEX] - 1

    def _rotate(self, direction) -> None:
        """
        Rotate the solution 90 degree to a given direction
        :param direction: The direction
        """
        for queen_coords in self.__queens_coords:
            first_coord = X_COORD_INDEX if direction == LEFT else Y_COORD_INDEX
            second_coord = Y_COORD_INDEX if direction == LEFT else X_COORD_INDEX
            place_holder = queen_coords[first_coord]
            queen_coords[first_coord] = queen_coords[second_coord]
            queen_coords[second_coord] = self.__size - place_holder - 1
        self._sort_queens()

    def _sort_queens(self) -> None:
        """
        Sort the queens by their x coord
        """
        self.__queens_coords = sorted(self.__queens_coords, key=lambda coord: coord[X_COORD_INDEX])
