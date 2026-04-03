from dataclasses import dataclass
from enums.command_types_enum import CommandType
from typing import Dict, Any


@dataclass
class Command:
    command_type: CommandType
    parameters: Dict[str, Any]
    cmd_id: str
