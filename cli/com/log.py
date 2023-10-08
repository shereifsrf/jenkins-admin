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

    def format(self, record):
        """remove color from log"""
        msg = super().format(record)
        return colorama.Style.RESET_ALL + msg

_logger = None
def _get_logger():
    """get logger"""
    global _logger

    if _logger:
        return _logger

    if not os.path.exists("cli/bin/logs"):
        os.makedirs("cli/bin/logs")

    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG)
    # add format
    _formatter = logging.Formatter(
        "%(asctime)s :%(levelname)s: %(message)s"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(_formatter)
    _logger.addHandler(stream_handler)

    file_handler = logging.FileHandler("cli/bin/logs/debug.log")
    file_handler.setFormatter(_NoColorFormatter(_formatter))
    _logger.addHandler(file_handler)

    logging.addLevelName(logging.DEBUG, colorama.Fore.BLUE + logging.getLevelName(logging.DEBUG) + colorama.Fore.RESET)
    logging.addLevelName(logging.INFO, colorama.Fore.GREEN + logging.getLevelName(logging.INFO) + colorama.Fore.RESET)

    return _logger


log = _get_logger()