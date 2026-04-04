from src.simulator.robot import Robot
from src.simulator.map import Map
from src.simulator.simulator import RobotSimulator
from src.enums import DirectionEnum
import os

if __name__ == "__main__":
    # Check if logs and data directories exist, if not create them
    if not os.path.exists("logs"):
        os.makedirs("logs")
    if not os.path.exists("data"):
        os.makedirs("data")


    # Instantiate simulator and run simulation
    robot = Robot("ToyRobot", 0, 0, DirectionEnum.NORTH)
    map = Map(5, 5)
    robot_simulator = RobotSimulator(robot=robot, map=map, log_file="logs/log.log")
    robot_simulator.run_simulation(sim_commands_file="data/input.txt", out_file="data/output.txt")