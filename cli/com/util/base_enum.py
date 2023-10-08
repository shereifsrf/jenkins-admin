"""Helper class for base enum"""

import enum

class BaseEnum(enum.Enum):
    """Base Enum class"""
    
    def __call__(self):
        return self.value