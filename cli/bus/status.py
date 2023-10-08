"""Module to check jenkins job status."""

from com.command.arg import Arg
from com.dto.result import Result
from com.log import log

from com.command.parser import CommandParser


class Status(CommandParser):
    """Class to check jenkins job status."""

    def __init__(self):
        self.job_name = Arg(str, "Name of job to check", True)

    def run(self) -> Result:
        log.info("Checking status of job %s", self.job_name)
