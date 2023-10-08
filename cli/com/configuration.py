"""Module to help with configuration"""

import json
import os

from com.util.base_enum import BaseEnum
from com.log import log

_CONFIGURATION_FILE = f"{os.path.dirname(__file__)}/../config/configuration.json"

class Property(BaseEnum):
    """properties from configuration"""
    NAME = "name"
    VERSION = "version"


class _Configuration:
    """Class for configuration"""

    def __init__(self, fullpath: str):
        try:
            with open(fullpath, "r") as file:
                self._config = json.load(file)
        except FileNotFoundError as e:
            log.error(f"File not found: {e}")
            raise e
        except json.JSONDecodeError as e:
            log.error(f"Error parsing JSON: {e}")
            raise e
        except Exception as e: # pylint: disable=broad-except
            log.error(f"Error: {e}")
            raise e


    def get(self, property: Property):
        """get property from configuration"""
        return self._config.get(property())
    
_configuration = _Configuration(_CONFIGURATION_FILE)

def get(property: Property):
    """get property from configuration"""
    return _configuration.get(property)