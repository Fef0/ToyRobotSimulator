import logging
from typing import List
from src.simulator.robot import Robot
from src.models.map_position import MapPosition
from src.simulator.map import Map
from src.models.command import Command
from src.enums import CommandTypeEnum, DirectionEnum
from src.exceptions import InvalidCommandException, InvalidMovementException
from uuid import uuid4


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
            level=logging.INFO
        )
        self.logger = logging.getLogger("robot_sim")

    def _parse_raw_command(self, raw_command: str) -> Command:
        """
        Transform a raw command into a real command

        :param raw_command: The raw command
        :raises InvaldCommandException: If the command does not exist
        :return: A formatted command
        """

        # Clean the string
        raw_command = raw_command.strip()
        chunks = raw_command.split(" ")
        command_name = chunks[0]
        params = chunks[1].split(",") if len(chunks) > 1 else []

        # Create a new random id to use in commands
        cmd_id = str(uuid4())

        # Create a new command based on command name and validates it
        match command_name:
            case "PLACE":
                if (len(params) != 3):
                    msg = f"Raw Command {raw_command} is invalid"
                    self.logger.error(msg)
                    raise InvalidCommandException(msg)
                return Command(command_type=CommandTypeEnum.PLACE,
                               parameters={
                                   "x": int(params[0].strip()),
                                   "y": int(params[1].strip()),
                                   "f": params[2].strip()
                                },
                               cmd_id=cmd_id)
            case "MOVE":
                return Command(command_type=CommandTypeEnum.MOVE, parameters={}, cmd_id=cmd_id)
            case "LEFT":
                return Command(command_type=CommandTypeEnum.LEFT, parameters={}, cmd_id=cmd_id)
            case "RIGHT":
                return Command(command_type=CommandTypeEnum.RIGHT, parameters={}, cmd_id=cmd_id)
            case "REPORT":
                return Command(command_type=CommandTypeEnum.REPORT, parameters={}, cmd_id=cmd_id)
            case _:
                msg = f"Raw Command {raw_command} does not exist"
                self.logger.error(msg)
                raise InvalidCommandException(msg)

    def _parse_commands_file(self, sim_commands_file: str) -> List[Command]:
        """
        Parse the commands from a file and returns a list of formatted commands

        :param sim_commands_file: File with commands
        :return: A list of formatted commands
        """

        commands = []

        # Open file and populate commands
        with open(file=sim_commands_file) as sim_commands_f:
            lines = sim_commands_f.readlines()
            for raw_cmd in lines:
                command = self._parse_raw_command(raw_command=raw_cmd)

                commands.append(command)

        # Return the parsed result
        return commands

    def _exec_place_command(self, command: Command) -> None:
        """
        Run a PLACE command

        :param command: Command to execute
        :raises InvalidMovementException: If the place position is invalid
        """

        # Convert parameters into a valid position in map
        robot_pos = MapPosition(x=command.parameters["x"], y=command.parameters["y"])
        robot_direction = DirectionEnum.from_str(command.parameters["f"])

        # Verify if the coordinates are valid in our map
        if (not self.map.is_position_valid(robot_pos)):
            msg = f"Place Coordinates {robot_pos} are invalid"
            self.logger.error(msg)
            raise InvalidMovementException(msg)

        # Update robot position
        self.robot.update_current_pos(position=robot_pos)
        self.robot.update_current_direction(direction=robot_direction)

        self.logger.info(f"Robot placed in {self.robot.get_current_pos()}")

    def _exec_move_command(self, command: Command) -> None:
        """
        Run a MOVE command

        :param command: Command to execute
        """

        current_robot_pos = self.robot.get_current_pos()
        current_robot_direction = self.robot.get_current_direction()

        future_robot_pos = None
        # Precompute future position after movement
        match current_robot_direction:
            # If the robot is facing NORTH, we move 1 up in the Y axis
            case DirectionEnum.NORTH:
                future_robot_pos = MapPosition(x=current_robot_pos.x, y=current_robot_pos.y + 1)
                # If the robot is facing SOUTH, we move 1 down in the Y axis
            case DirectionEnum.SOUTH:
                future_robot_pos = MapPosition(x=current_robot_pos.x, y=current_robot_pos.y - 1)
                # If the robot is facing EAST, we move 1 right in the X axis
            case DirectionEnum.EAST:
                future_robot_pos = MapPosition(x=current_robot_pos.x+1, y=current_robot_pos.y)
                # If the robot is facing WEST, we move 1 left in the X axis
            case DirectionEnum.WEST:
                future_robot_pos = MapPosition(x=current_robot_pos.x-1, y=current_robot_pos.y)

        # If the position is not valid, we skip it
        if (not self.map.is_position_valid(position=future_robot_pos)):
            self.logger.warning(f"Robot Position {future_robot_pos} is not valid, skipping it")
            return

        self.robot.update_current_pos(position=future_robot_pos)

        self.logger.info(f"Robot moved to {future_robot_pos} - New Coordinates: {current_robot_pos}")

    def _exec_left_command(self, command: Command) -> None:
        """
        Run a LEFT command

        :param command: Command to execute
        """

        # NORTH -> WEST , SOUTH -> EAST , EAST -> NORTH , WEST -> SOUTH
        current_robot_direction = self.robot.get_current_direction()

        match current_robot_direction:
            case DirectionEnum.NORTH:
                self.robot.update_current_direction(DirectionEnum.WEST)
            case DirectionEnum.SOUTH:
                self.robot.update_current_direction(DirectionEnum.EAST)
            case DirectionEnum.EAST:
                self.robot.update_current_direction(DirectionEnum.NORTH)
            case DirectionEnum.WEST:
                self.robot.update_current_direction(DirectionEnum.SOUTH)
        
        self.logger.info(f"Robot rotated to the LEFT - New Direction: {self.robot.get_current_direction()}")

    def _exec_right_command(self, command: Command) -> None:
        """
        Run a RIGHT command

        :param command: Command to execute
        """

        # NORTH -> EAST , SOUTH -> WEST , EAST -> SOUTH , WEST -> NORTH
        current_robot_direction = self.robot.get_current_direction()

        match current_robot_direction:
            case DirectionEnum.NORTH:
                self.robot.update_current_direction(DirectionEnum.EAST)
            case DirectionEnum.SOUTH:
                self.robot.update_current_direction(DirectionEnum.WEST)
            case DirectionEnum.EAST:
                self.robot.update_current_direction(DirectionEnum.SOUTH)
            case DirectionEnum.WEST:
                self.robot.update_current_direction(DirectionEnum.NORTH)
        
        self.logger.info(f"Robot rotated to the RIGHT - New Direction: {self.robot.get_current_direction()}")

    def _exec_report_command(self, command: Command, out_file: str) -> None:
        """
        Run a REPORT command

        :param command: Command to execute
        :param out_file: File to which the simulator will write the output of the simulation
        """
        with open(file=out_file, mode="a+") as out_f:
            robot_current_pos = self.robot.get_current_pos()
            robot_current_direction = self.robot.get_current_direction()

            # build output msg
            out_msg = f"{robot_current_pos.x},{robot_current_pos.y},{robot_current_direction.value}"
            self.logger.info(f"Report: {out_msg}")
            out_f = out_f.write(f"{out_msg}\n")

    def _run_simulation_step(self, command: Command, out_file: str) -> None:
        """
        Run a single step of the simulation

        :param command: Command to execute
        :param out_file: File to which the simulator will write the output of the simulation
        :raises InvalidCommandException: If the command is not recognized 
        """
        match command.command_type:
            case CommandTypeEnum.PLACE:
                self._exec_place_command(command=command)
            case CommandTypeEnum.MOVE:
                self._exec_move_command(command=command)
            case CommandTypeEnum.LEFT:
                self._exec_left_command(command=command)
            case CommandTypeEnum.RIGHT:
                self._exec_right_command(command=command)
            case CommandTypeEnum.REPORT:
                self._exec_report_command(command=command, out_file=out_file)
            case _:
                msg = f"Command {command} not recognized"
                self.logger.error(msg)
                raise InvalidCommandException(msg)

    def run_simulation(self, sim_commands_file: str, out_file: str) -> None:
        """
        Run a simulation from a file and write the output to a file

        :param sim_commands_file: File with commands
        :param out_file: File to which the simulator will write the output of the simulation
        """
        # Load commands from file
        commands = self._parse_commands_file(sim_commands_file=sim_commands_file)

        # Constraint: The application should discard all commands in the sequence until a valid PLACE command has been
        # executed, so we must ensure that a place has occurred before adding a new command
        has_been_placed = False

        # Execute commands
        for command in commands:
            self.logger.info(f"Executing command {command}")
            # If the robot has not been placed we skip all commands that are not a PLACE one
            if (not has_been_placed and command.command_type != CommandTypeEnum.PLACE):
                continue
            # We flag the place once we receive the command
            elif (not has_been_placed and command.command_type == CommandTypeEnum.PLACE):
                has_been_placed = True

            # Now we can execute the command
            self._run_simulation_step(command=command, out_file=out_file)
