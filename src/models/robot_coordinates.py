from dataclasses import dataclass


@dataclass
class RobotCoordinates:
    """
    Coordinates in a 2D space

    :param x: Position on X axis
    :param y: Position on Y axis
    """
    x: int
    y: int
 
