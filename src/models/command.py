from dataclasses import dataclass
from src.enums.enums import CommandTypeEnum
from typing import Dict, Any


@dataclass
class Command:
    command_type: CommandTypeEnum
    parameters: Dict[str, Any]
    cmd_id: str
