"""Entry point for the CLI."""

import logging

from com.command.parser import Parser


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s %(filename)s %(funcName)s %(message)s",
        handlers=[logging.FileHandler("cli/bin/logs/debug.log"), logging.StreamHandler()],
    )

    logging.info("Starting CLI")
    Parser.parser()
