from dataclasses import dataclass


@dataclass
class RobotPosition:
    """
    Position of the Robot in a 2D space

    :param x: Position on X axis
    :param y: Position on Y axis
    """
    x: int
    y: int
