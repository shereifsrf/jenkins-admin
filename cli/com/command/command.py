"""Command module for command parser"""

from typing import Callable
from cli.com.dto.result import Result
from com.command.arg import Arg


class Command:
    """Command class for command parser"""

    def __init__(self, dest: str, args: list[Arg], fn: Callable[[], Result]):
        self.dest = dest
        self.args = args
        self.fn = fn