"""Arg class for storing the structure of the command line arguments"""


class Arg:  # pylint: disable=too-few-public-methods
    """Class for args to store the structure"""

    def __init__(self, arg_type: type, arg_help: str, required: bool):
        self.arg_type = arg_type
        self.arg_help = arg_help
        self.required = required
        self.arg = None
        self.dest = None

    def update(self, dest: str):
        """update arg with dest after parsing via metaclass"""
        self.dest = dest
        self.arg = f"--{dest}"