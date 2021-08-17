#
# Data Transmission Helper
# Transmit data

import getpass
import json
import os
import socket
import sys
from datetime import datetime

import click
import psutil
import requests
from requests.auth import HTTPBasicAuth

from helpers.logger_helper import logger


@click.command()
@click.option(
    "--api",
    required=True,
    prompt="Enter the api endpoint",
    help="API endpoint"
)
@click.option(
    "--key",
    prompt="Enter the api key",
    help="API key"
)
@click.option(
    "--data",
    required=True,
    prompt="Enter the json data",
    help="Data to send"
)
def api(api, key, data):
    try:
        request_headers = {"Content-Type": "application/json"}

        if not key:
            request_auth = HTTPBasicAuth("apikey", key)
            response = requests.post(
                api,
                data=json.dumps(data),
                headers=request_headers,
                auth=request_auth
            )
        else:
            response = requests.post(
                api,
                data=json.dumps(data),
                headers=request_headers
            )

        log("transmit data", api, "api", sys.getsizeof(data))

        print(f"Response: {repr(response)}")

    except requests.exceptions.RequestException as error:
        log("transmission error", api, "api", sys.getsizeof(data))
        print(error)
        raise


@click.command()
@click.option(
    "--host",
    required=True,
    prompt="Enter the host address or ip",
    help="API endpoint"
)
@click.option(
    "--port",
    required=True,
    type=int,
    prompt="Enter the port",
    help="API key"
)
@click.option(
    "--data",
    required=True,
    prompt="Enter the json data",
    help="Data to send"
)
def tcp(host, port, data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(json.dumps(data))
            response = s.recv(1024)

        log("transmit data", f"{host}:{port}", "tcp", sys.getsizeof(data))

        print(f"Response: {repr(response)}")

    except socket.error as error:
        log("transmission error", f"{host}:{port}", "tcp", sys.getsizeof(data))
        print(error)
        raise


def log(activity, destination="", protocol="", size=""):
    # Gather logging details
    p = psutil.Process(os.getpid())
    hostname = socket.gethostname()
    log = {
        "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "process_name": p.name(),
        "process_id": os.getpid(),
        "process_command_line": " ".join(p.cmdline()),
        "username": getpass.getuser(),
        "activity": activity,
        "file_path": "",
        "destination": destination,
        "source": f"{hostname}|{socket.gethostbyname(hostname)}",
        "protocol": protocol,
        "data_size": size,
    }

    # Log
    logger(process_data=log)
