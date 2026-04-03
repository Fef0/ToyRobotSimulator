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

    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    @staticmethod
    def from_str(raw_param: str):
        """
        Enable the enum to translate a raw string to an element of the Enum itself
        e.g. DirectionEnum["NORTH"] -> DirectionEnum.NORTH

        :param raw_param: Raw string to convert to an element of the Enum

        """
        return DirectionEnum[raw_param]
