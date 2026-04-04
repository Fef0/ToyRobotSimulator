from src.simulator.map import Map
from src.models.map_position import MapPosition


def test_map_is_position_valid():
    m = Map(5, 5)
    # Test map limits
    assert m.is_position_valid(MapPosition(x=0, y=0)) is True
    assert m.is_position_valid(MapPosition(x=4, y=4)) is True
    # Test invalid positions
    assert m.is_position_valid(MapPosition(x=5, y=4)) is False
    assert m.is_position_valid(MapPosition(x=4, y=5)) is False
    assert m.is_position_valid(MapPosition(x=-1, y=0)) is False
    assert m.is_position_valid(MapPosition(x=0, y=-1)) is False
