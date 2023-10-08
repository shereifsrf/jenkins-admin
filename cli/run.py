"""Entry point for the CLI."""

from com.log import log
from com.command.parser import parser
import bus.status


if __name__ == "__main__":
    log.info("Starting CLI")
    parser()
