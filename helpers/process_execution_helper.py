#
# Process Execution Helper
# Call executable

import getpass
import os
from datetime import datetime

import click
import psutil

from helpers.logger_helper import logger


@click.command()
@click.option(
    "--path",
    required=True,
    prompt="Enter the path to the executable",
    help="Location of executable",
)
@click.option(
    "--exe",
    required=True,
    prompt="Enter the name of the executable",
    help="Executable"
)
@click.option(
    "--args",
    prompt="Enter any optional arguments",
    help="Arguments of executable"
)
def exe(path, exe, args):
    # Call file given path and arguments
    executable = f"{path}/{exe} {args}"
    os.system(executable)

    # Gather logging details
    p = psutil.Process(os.getpid())

    # Define dataset
    log = {
        "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "process_name": p.name(),
        "process_id": os.getpid(),
        "process_command_line": " ".join(p.cmdline()),
        "username": getpass.getuser(),
        "activity": "run executable",
        "file_path": "",
        "destination": "",
        "source": "",
        "protocol": "",
        "data_size": "",
    }

    # Log details
    logger(process_data=log)
