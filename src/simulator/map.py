from typing import Tuple
from models.robot_position import RobotPosition


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
        # Creates an empty map (0 means empty, 1 means occupied)
        self.map = [[0] * length] * width
    
    def update_map(self, old_robot_pos: RobotPosition, new_robot_pos: RobotPosition):
        """
        Updates occupancy in the Map

        :param old_robot_pos: The Robot position before command execution
        :param new_robot_pos: The Robot position after command execution
        """

        # Removes the robot from old position
        self.map[old_robot_pos.x][old_robot_pos.y] = 0
        # Put the robot into the new positiion
        self.map[new_robot_pos.x][new_robot_pos.y] = 1

    def get_size(self) -> Tuple[int, int]:
        """
        Get map size
        """

        return self.length, self.width
