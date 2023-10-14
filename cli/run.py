"""Entry point for the """

from com.log import log
from com.command.parser import parser
import bus.status  # pylint: disable=unused-import


if __name__ == "__main__":
    parser()
