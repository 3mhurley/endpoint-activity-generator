#
# Endpoint Activity Generator
# CLI App to call services:
#  File manipulation, Executable running, Data transmission

import getpass
import os
from datetime import datetime

import click
import psutil

from helpers.data_transmission_helper import api, tcp
from helpers.file_manipulation_helper import file
from helpers.logger_helper import logger
from helpers.process_execution_helper import exe


@click.group()
def cli():
    # Log details
    log("process started")
    pass


@cli.group()
def data():
    pass


def log(activity):
    # Gather logging details
    p = psutil.Process(os.getpid())
    log = {
        "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "process_name": p.name(),
        "process_id": os.getpid(),
        "process_command_line": " ".join(p.cmdline()),
        "username": getpass.getuser(),
        "activity": activity,
        "file_path": "",
        "destination": "",
        "source": "",
        "protocol": "",
        "data_size": "",
    }

    # Log
    logger(process_data=log)


cli.add_command(file)
cli.add_command(exe)
cli.add_command(data)

data.add_command(api)
data.add_command(tcp)

if __name__ == "__main__":
    cli()
