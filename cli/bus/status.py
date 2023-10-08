"""Module to check jenkins job status."""

from com.dto.result import Result
from com.log import log

from com.command.parser import CommandParser


class Status(CommandParser):
    """Class to check jenkins job status."""

    def __init__(self, job_name: str):
        self.job_name = job_name

    def run(self) -> Result:
        log.info(f"Checking status of job {self.job_name}")