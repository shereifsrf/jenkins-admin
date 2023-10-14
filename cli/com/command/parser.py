"""This module to work with arg parser"""

from abc import ABCMeta, abstractmethod
import argparse
from com.command.command import Command
from com.command.arg import Arg

from com.dto.result import Result
from com.log import log
import com.configuration as Config

__all__ = ["parser", "CommandParser", "ArgParser"]


class _CustomArgumentParser(argparse.ArgumentParser):
    """Custom argument parser"""

    def error(self, message):
        """error message"""
        log.error(f"Argument parser error: {message}")
        super().error(message)
class _Parser(ABCMeta):
    """
    meta class for argparser to help easily add arguments and
    standard of definition
    """

    _parser = _CustomArgumentParser(
        prog=Config.get(Config.Property.NAME),
        description="CLI for Jenkins admin",
        epilog="This is where you might put example usage",
        exit_on_error=False,
    )
    _subparsers = _parser.add_subparsers(dest="command", required=True)

    # add version argument
    _parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {Config.get(Config.Property.VERSION)}",
        help="show program's version number and exit",
    )

    def __init__(cls, name, bases, attrs):
        """set up parser"""
        if name in ["CommandParser", "ArgParser"]:
            return

        obj: CommandParser = cls()
        # add command with arguments for cli
        command_dest = Command.extract_command_name(name)
        command_parser = _Parser._subparsers.add_parser(command_dest)
        args: list[Arg] = []
        for key, value in obj.__dict__.items():
            if not isinstance(value, Arg):
                raise KeyError(f"Invalid type {type(value)} for {key}")

            value.update(key)
            command_parser.add_argument(
                value.arg,
                dest=value.dest,
                type=value.arg_type,
                help=value.arg_help,
                required=value.required,
            )
            args.append(value)

        # check if the base class is ArgParser
        is_arg_parser = False
        for base in bases:
            log.debug(f"Checking base {base.__name__}")
            if base.__name__ == "ArgParser":
                is_arg_parser = True
                break
        cls.__init__ = _Parser.get_constructor(is_arg_parser, args)
        Command.add(cls, command_dest, args, obj.run)

    @classmethod
    def get_parser(mcs):
        """argument parser"""
        return mcs._parser

    @staticmethod
    def get_constructor(is_arg_parser: bool, args: list[Arg]):
        """get constructor"""

        def constructor(self, **kwargs):
            """constructor"""

            if is_arg_parser:
                return
            for arg in args:
                setattr(self, arg.dest, kwargs[arg.dest])

        return constructor


def parser():
    """parse arguments"""
    args = _Parser.get_parser().parse_args()
    
    log.debug(f"Parsing args, {args}")
    log.info(f"Running command '{args.command}'")
    cmd = Command.get(args.command)
    del args.command
    obj: CommandParser = cmd.class_type(**vars(args))
    obj.run()


class CommandParser(metaclass=_Parser):
    """Parser helper to add commands for cli"""

    @abstractmethod
    def run(self) -> Result:
        """run command"""


class ArgParser(metaclass=_Parser):
    """Some classes are needs to be inherited for command classes"""

    @abstractmethod
    def validate(self) -> Result:
        """validate command"""
