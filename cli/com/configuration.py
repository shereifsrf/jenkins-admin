"""Module to help with configuration"""

import json
import os

from com.util.base_enum import BaseEnum
from com.logger import log

_CONFIGURATION_FILE = (
    f"{os.path.dirname(os.path.dirname(__file__))}/config/configuration.json"
)


class Property(BaseEnum):
    """properties from configuration"""

    NAME = "name"
    VERSION = "version"


class _Configuration:
    """Class for configuration"""

    def __init__(self, fullpath: str):
        try:
            with open(fullpath, "r", encoding="utf-8") as file:
                self._config = json.load(file)
        except FileNotFoundError as e:
            log.error("File not found: %s", e)
            raise e
        except json.JSONDecodeError as e:
            log.error("Error parsing JSON: %s", e)
            raise e
        except Exception as e:  # pylint: disable=broad-except
            log.error("Error: %s", e)
            raise e

    def get(self, prop: Property):
        """get property from configuration"""
        return self._config.get(prop())


_configuration = _Configuration(_CONFIGURATION_FILE)


def get(prop: Property):
    """get property from configuration"""
    return _configuration.get(prop)
