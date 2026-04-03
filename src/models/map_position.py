from dataclasses import dataclass


@dataclass
class MapPosition:
    """
    Position of an object in a 2D map

    :param x: Position on X axis
    :param y: Position on Y axis
    """
    x: int
    y: int
