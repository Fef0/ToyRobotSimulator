from typing import Tuple
from src.models.map_position import MapPosition


class Map:
    """
    A 2D Map
    """
    def __init__(self, length: int, width: int) -> None:
        """
        Initialize Map size

        :param length: Length of the map
        :param width: Width of the map
        """

        self.length = length
        self.width = width
    
    def is_position_valid(self, position: MapPosition) -> bool:
        """
        Checks the validity of a given position

        :param position: Position to check
        :return: True if the provided position is valid, False otherwise
        """
        return 0 <= position.x < self.length and 0 <= position.y < self.width

    def get_size(self) -> Tuple[int, int]:
        """
        Get map size

        :return: The size of the map as an (length, width) tuple
        """

        return self.length, self.width
