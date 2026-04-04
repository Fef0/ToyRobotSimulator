import os
import tempfile
import pytest
from src.simulator.simulator import RobotSimulator
from src.simulator.robot import Robot
from src.simulator.map import Map
from src.enums import DirectionEnum, CommandTypeEnum
from src.exceptions import InvalidCommandException, InvalidMovementException


@pytest.fixture
def simulator() -> RobotSimulator:
    # Create a temporary file to store logs
    fd, log_file_path = tempfile.mkstemp()
    os.close(fd)

    # Instantiate simulator
    robot = Robot("TestBot", 0, 0, DirectionEnum.NORTH)
    grid_map = Map(5, 5)
    
    sim = RobotSimulator(robot, grid_map, log_file_path)
    return sim


def test_parse_raw_command_place(simulator: RobotSimulator):
    cmd = simulator._parse_raw_command("PLACE 1,2,EAST")
    assert cmd.command_type == CommandTypeEnum.PLACE
    assert cmd.parameters == {"x": 1, "y": 2, "f": "EAST"}


def test_parse_raw_command_invalid(simulator: RobotSimulator):
    with pytest.raises(InvalidCommandException):
        simulator._parse_raw_command("INVALID_COMMAND")


def test_exec_place_command_invalid(simulator: RobotSimulator):
    cmd = simulator._parse_raw_command("PLACE 6,6,SOUTH")
    with pytest.raises(InvalidMovementException):
        simulator._exec_place_command(cmd)


def test_exec_move_command(simulator: RobotSimulator):
    # Place and move
    simulator._exec_place_command(simulator._parse_raw_command("PLACE 2,2,NORTH"))
    simulator._exec_move_command(simulator._parse_raw_command("MOVE"))
    pos = simulator.robot.get_current_pos()
    assert simulator.robot.get_current_direction() == DirectionEnum.NORTH
    assert pos.x == 2
    assert pos.y == 3

    # Place and move
    simulator._exec_place_command(simulator._parse_raw_command("PLACE 2,2,SOUTH"))
    simulator._exec_move_command(simulator._parse_raw_command("MOVE"))
    pos = simulator.robot.get_current_pos()
    assert simulator.robot.get_current_direction() == DirectionEnum.SOUTH
    assert pos.x == 2
    assert pos.y == 1

    # Place and move
    simulator._exec_place_command(simulator._parse_raw_command("PLACE 2,2,EAST"))
    simulator._exec_move_command(simulator._parse_raw_command("MOVE"))
    pos = simulator.robot.get_current_pos()
    assert simulator.robot.get_current_direction() == DirectionEnum.EAST
    assert pos.x == 3
    assert pos.y == 2

    # Place and move
    simulator._exec_place_command(simulator._parse_raw_command("PLACE 2,2,WEST"))
    simulator._exec_move_command(simulator._parse_raw_command("MOVE"))
    pos = simulator.robot.get_current_pos()
    assert simulator.robot.get_current_direction() == DirectionEnum.WEST
    assert pos.x == 1
    assert pos.y == 2


def test_exec_left_command(simulator: RobotSimulator):
    simulator._exec_place_command(simulator._parse_raw_command("PLACE 0,0,NORTH"))
    
    simulator._exec_left_command(simulator._parse_raw_command("LEFT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.WEST
    
    simulator._exec_left_command(simulator._parse_raw_command("LEFT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.SOUTH
    
    simulator._exec_left_command(simulator._parse_raw_command("LEFT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.EAST
    
    simulator._exec_left_command(simulator._parse_raw_command("LEFT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.NORTH


def test_exec_right_command(simulator: RobotSimulator):
    simulator._exec_place_command(simulator._parse_raw_command("PLACE 0,0,NORTH"))
    
    simulator._exec_right_command(simulator._parse_raw_command("RIGHT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.EAST
    
    simulator._exec_right_command(simulator._parse_raw_command("RIGHT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.SOUTH
    
    simulator._exec_right_command(simulator._parse_raw_command("RIGHT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.WEST
    
    simulator._exec_right_command(simulator._parse_raw_command("RIGHT"))
    assert simulator.robot.get_current_direction() == DirectionEnum.NORTH
