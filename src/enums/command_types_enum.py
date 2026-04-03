from enum import Enum


class CommandType(Enum):
    """
    Type of a received command
    """

    PLACE = 1
    MOVE = 2
    LEFT = 3
    RIGHT = 4
    REPORT = 5
