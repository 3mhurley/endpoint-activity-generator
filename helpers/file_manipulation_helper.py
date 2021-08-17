#
# File Manipulator Helper
# Create, modify, delete file

import getpass
import os
from datetime import datetime
from pathlib import Path, PurePath

import click
import psutil

from helpers.logger_helper import logger


@click.command()
@click.option(
    "--path",
    required=True,
    prompt="Enter a path location for the file",
    help="Destination of the file",
)
@click.option(
    "--name",
    default="endpoint_activity",
    prompt="Enter a name for the file",
    help="Name of the file",
)
@click.option(
    "--exe",
    default="txt",
    prompt="Enter an extension type for the file",
    help="Extension of the file",
)
def file(path, name, exe):
    # Retrieve values from arguments
    original_path = Path(path)
    file = f"{name}.{exe}"

    # Create file
    file_path = create(original_path, file)

    # Manipulate file
    new_file_path = manipulate(file_path, original_path, file)

    # Delete file
    delete(new_file_path)


def create(path, name):
    # Create new file
    try:
        # Check if path exists
        if path.exists() is False:
            raise Exception(f"Error: {path} does not exist")

        # Check if file exists
        file = PurePath.joinpath(path, name)
        if file.exists() is True:
            raise Exception(f"Error: {file} already exists")

        # Create and write file
        with open(file, "x") as f:
            f.write("01001000 01100101 01101100 01101100 01101111\n")
            f.write("01010111 01101111 01110010 01101100 01100100\n")

        # Log details
        log("file created", file)

        return file

    except (FileNotFoundError, AssertionError) as error:
        print(error)
        raise


def manipulate(file_path, path, file):
    # Modify file
    try:
        # Check if file exists
        if file_path.exists() is False:
            raise Exception(f"Error: {file_path} does not exist")

        # Adjust file contents
        with open(file_path, "a") as f:
            f.write("\n01100100 01101100 01110010 01101111 01010111")
            f.write("\n01101111 01101100 01101100 01100101 01001000")

        # Rename file with reversed file name
        file_name, file_exe = file.split(".")
        new_path_str = f"{path}\\{file_name[::-1]}.{file_exe}"
        new_path = file_path.rename(new_path_str)

        # Change file extension
        final_path = new_path.rename(new_path.with_suffix(".text"))

        # Log details
        log("file modified", final_path)

        return final_path

    except (FileNotFoundError, AssertionError) as error:
        print(error)


def delete(file_path):
    # Delete file
    try:
        # Check if file exists
        if file_path.exists() is False:
            raise Exception(f"Error: {file_path} does not exist")

        # Delete file
        file_path.unlink()

        # Log details
        log("file deleted", file_path)

    except (FileNotFoundError, AssertionError) as error:
        print(error)
        raise


def log(activity, file_path):
    # Gather logging details
    p = psutil.Process(os.getpid())
    log = {
        "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "process_name": p.name(),
        "process_id": os.getpid(),
        "process_command_line": " ".join(p.cmdline()),
        "username": getpass.getuser(),
        "activity": activity,
        "file_path": file_path,
        "destination": "",
        "source": "",
        "protocol": "",
        "data_size": "",
    }

    # Log
    logger(process_data=log)
