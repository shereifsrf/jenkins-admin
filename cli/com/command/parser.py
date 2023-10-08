"""This module to work with arg parser"""

from abc import ABCMeta, abstractmethod
import argparse

from com.dto.result import Result
from com.log import log
import com.configuration as Config

__all__ = ["CommandParser", "parser"]

class _Parser(ABCMeta):
    """
    meta class for argparser to help easily add arguments and
    standard of definition
    """

    _parser = argparse.ArgumentParser(
        prog=Config.get(Config.Property.NAME),
        description="CLI for Jenkins admin",
        epilog="This is where you might put example usage",
    )
    _subparsers = _parser.add_subparsers(dest="command", required=True)

    # add version argument
    _parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=Config.get(Config.Property.VERSION)),
        help="show program's version number and exit",
    )

    def __init__(cls, name, bases, attrs):
        """set up parser"""
        log.debug("Setting up parser")

    @classmethod
    def parser(cls):
        """argument parser"""
        args = cls._parser.parse_args()
        log.debug(f"Parsing args, {args}")

def parser():
    _Parser.parser()

class CommandParser(metaclass=_Parser):
    """Parser helper to add commands"""

    @abstractmethod
    def __init__(self, **kwargs):
        pass
    
    @abstractmethod
    def run(self) -> Result:
        pass