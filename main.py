from src.simulator.robot import Robot
from src.simulator.map import Map
from src.simulator.simulator import RobotSimulator
from src.enums import DirectionEnum

if __name__ == "__main__":
    robot = Robot("ToyRobot", 0, 0, DirectionEnum.NORTH)
    map = Map(5, 5)

    robot_simulator = RobotSimulator(robot=robot, map=map, log_file="logs/log.log")

    robot_simulator.run_simulation(sim_commands_file="data/input.txt", out_file="data/output.txt")