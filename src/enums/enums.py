from enum import Enum


class CommandTypeEnum(Enum):
    """
    Type of a received command
    """

    PLACE = 1
    MOVE = 2
    LEFT = 3
    RIGHT = 4
    REPORT = 5


class DirectionEnum(Enum):
    """
    Direction name
    """

    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
