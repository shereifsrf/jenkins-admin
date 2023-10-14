"""Command module for command parser"""

from typing import Callable
from com.log import log
from com.dto.result import Result
from com.command.arg import Arg


class Command:
    """Command class for command parser"""

    _COMMANDS: dict[str, "Command"] = {}

    def __init__(self, class_type: type, args: list[Arg], run: Callable[[], Result]):
        self.class_type = class_type
        self.args = args
        self.run = run

    @classmethod
    def add(
        cls, class_type: type, dest: str, args: list[Arg], run: Callable[[], Result]
    ):
        """add command to list"""
        log.debug(f"Adding command {dest}")
        cls._COMMANDS[dest] = cls(class_type, args, run)

    @classmethod
    def get(cls, command: str) -> "Command":
        """get command from list"""
        log.debug(f"Getting command {command}")
        return cls._COMMANDS[command]

    @staticmethod
    def extract_command_name(command: str) -> str:
        """extract command name from class name"""
        command = command.replace("_", "-")
        # if its in PascalCase, convert to kebab-case
        for char in command:
            if char.isupper():
                command = command.replace(char, f"-{char.lower()}")

        return command.lstrip("-")
