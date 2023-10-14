"""Helper module for logging
This module can be used in any modules in the repo
This will set the logging with configuration and can be used anywhere
"""

import logging
import os
import colorama


__all__ = ["log"]


class _NoColorFormatter(logging.Formatter):
    """Formatter to remove color from log"""

    def __init__(self, fmt):
        super().__init__(fmt)

    def format(self, record):
        """remove color from log"""
        msg = super().format(record)
        return (
            msg.replace(colorama.Fore.BLUE, "")
            .replace(colorama.Fore.GREEN, "")
            .replace(colorama.Fore.RESET, "")
        )


class _Logger:
    """Logger class"""

    _logger = None

    @classmethod
    def get_logger(cls):
        """get logger"""
        if cls._logger:
            return cls._logger

        if not os.path.exists("cli/bin/logs"):
            os.makedirs("cli/bin/logs")

        cls._logger = logging.getLogger(__name__)
        cls._logger.setLevel(logging.DEBUG)
        # add format
        _formatter = "%(asctime)s :%(levelname)s:%(filename)s:%(lineno)d: %(message)s"

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(_formatter))
        cls._logger.addHandler(stream_handler)

        file_handler = logging.FileHandler("cli/bin/logs/debug.log")
        file_handler.setFormatter(_NoColorFormatter(_formatter))
        cls._logger.addHandler(file_handler)

        logging.addLevelName(
            logging.DEBUG,
            colorama.Fore.BLUE
            + logging.getLevelName(logging.DEBUG)
            + colorama.Fore.RESET,
        )
        logging.addLevelName(
            logging.INFO,
            colorama.Fore.GREEN
            + logging.getLevelName(logging.INFO)
            + colorama.Fore.RESET,
        )

        return cls._logger


log = _Logger.get_logger()  # pylint: disable=invalid-name
