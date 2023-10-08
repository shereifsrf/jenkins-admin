"""This module to work with arg parser"""

import argparse
import logging


class Parser(type):
    """
    meta class for argparser to help easily add arguments and
    standard of definition
    """

    _parser = argparse.ArgumentParser()
    _subparsers = _parser.add_subparsers(dest="command", required=True)

    # add version argument
    _parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0",
        help="show program's version number and exit",
    )


    def __new__(cls, name, bases, attrs):
        """set up parser"""
        logging.debug("Setting up parser")

    @staticmethod
    def parser():
        """argument parser"""
        args = Parser._parser.parse_args()
        logging.debug("Parsing args")
