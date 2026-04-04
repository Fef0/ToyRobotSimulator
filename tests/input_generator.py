import os
import sys

# Add the parent directory to sys.path to allow running directly from the tests folder
# which is ugly but works for rapid testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.enums import CommandTypeEnum, DirectionEnum
from src.models.map_position import MapPosition
import random

map_size_l = 5
map_size_w = 5

# Max coordinates at which we place a robot
place_max_coord_x = map_size_l - 1
place_max_coord_y = map_size_w - 1

output_size = 10

# A fast half-hacked way to generate new inputs for testing
output_file_path = os.path.join(os.path.dirname(__file__), '..', 'input.txt')
with open(output_file_path, "w") as out:
    for i in range(output_size):
        # Choose a random command and direction
        command = random.choice(list(CommandTypeEnum))
        direction = random.choice(list(DirectionEnum))

        match command:
            case CommandTypeEnum.PLACE:
                # Generate random coordinates to place a Robot
                coordinates = MapPosition(random.randint(0, place_max_coord_x), random.randint(0, place_max_coord_y))
                cmd = f"PLACE {coordinates.x},{coordinates.y},{direction.value}\n"
                out.write(cmd)
            case CommandTypeEnum.MOVE:
                cmd = f"MOVE\n"
                out.write(cmd)
            case CommandTypeEnum.LEFT:
                cmd = f"LEFT\n"
                out.write(cmd)
            case CommandTypeEnum.RIGHT:
                cmd = f"RIGHT\n"
                out.write(cmd)
            case CommandTypeEnum.REPORT:
                cmd = f"REPORT\n"
                out.write(cmd)