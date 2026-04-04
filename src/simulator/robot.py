from src.models.map_position import MapPosition
from src.enums import DirectionEnum


class Robot:
    """
    A Robot in a 2D space
    """
    def __init__(self, name: str, init_pos_x: int, init_pos_y: int, init_direction: DirectionEnum) -> None:
        """
        Initialize robot position and direction in a 2D space

        :param name: Robot name
        :param init_pos_x: Initial position on X axis
        :param init_pos_y: Initial position on Y axis
        :param init_direction: Initial direction
        """
        self.name = name
        self.pos = MapPosition(
            x=init_pos_x,
            y=init_pos_y,
        )

        self.direction = init_direction

    def get_name(self) -> str:
        """
        Returns robot name

        :return: The Rsobot name
        """
        return self.name

    def get_current_pos(self) -> MapPosition:
        """
        Returns current Robot position in space

        :return: The Robot position in space
        """
        return self.pos
    
    def get_current_direction(self) -> DirectionEnum:
        """
        Returns current Robot direction

        :return: The Robot direction in space
        """
        return self.direction

    def update_current_pos(self, position: MapPosition) -> None:
        """
        Updates current Robot position in space

        :param pos_x: The new Robot position on X axis
        :param pos_y: The new Robot position on Y axis
        """

        self.pos = position

    def update_current_direction(self, direction: DirectionEnum) -> None:
        """
        Updates current Robot facing direction
        
        :param direction: The new Robot direction
        """

        self.direction = direction
