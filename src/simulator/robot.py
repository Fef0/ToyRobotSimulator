from models.robot_position import RobotPosition


class Robot:
    """
    A Robot in a 2D space
    """
    def __init__(self, name: str, init_pos_x: int, init_pos_y: int, init_direction: str) -> None:
        """
        Initialize robot position and direction in a 2D space

        :param name: Robot name
        :param init_pos_x: Initial position on X axis
        :param init_pos_y: Initial position on Y axis
        :param init_direction: Initial direction
        """
        self.name = name
        self.pos = RobotPosition(
            x=init_pos_x,
            y=init_pos_y,
        )

        self.direction = init_direction

    def get_name(self) -> str:
        """
        Returns robot name
        """
        return self.name

    def get_current_pos(self) -> RobotPosition:
        """
        Returns current Robot position in space
        """
        
        return self.pos

    def update_current_pos(self, pos_x: int, pos_y: int) -> None:
        """
        Updates current Robot position in space

        :param pos_x: The new Robot position on X axis
        :param pos_y: The new Robot position on Y axis
        """

        self.pos = RobotPosition(
            x=pos_x,
            y=pos_y
        )

    def update_current_direction(self, direction: str) -> None:
        """
        Updates current Robot facing direction
        
        :param direction: The new Robot direction
        """

        self.direction = direction
