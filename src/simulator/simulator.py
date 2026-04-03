import logging
from simulator.robot import Robot
from simulator.map import Map


class RobotSimulator():
    def __init__(self, robot: Robot, map: Map, log_file: str) -> None:
        """
        Initialize a simulator that controls a Robot in a 2D Map

        :param robot: The Robot to control
        :param map: The Map in which the robot moves
        :param log_file: The log file to which write logs into
        """

        self.robot = robot
        self.map = map
        self.log_file = log_file
        
        # Set logging policies
        logging.basicConfig(
            filename=log_file,
            encoding="utf-8",
            filemode="a",
            format="{asctime} - {levelname} - {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M",
        )
        self.logger = logging.getLogger("robot_sim")
