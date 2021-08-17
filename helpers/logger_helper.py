#
# Logger Helper
# Logs processes

import csv
from pathlib import Path, PurePath


def logger(process_data):
    try:
        # Get current working directory
        path = Path.cwd()

        # Establish full file path
        file = PurePath.joinpath(path, "endpoint_generator_logs.csv")

        file_exists = file.exists()

        with open(file, "a+", newline="") as f:
            w = csv.DictWriter(f, process_data.keys())

            if not file_exists:
                w.writeheader()

            w.writerow(process_data)

    except (FileNotFoundError, AssertionError) as error:
        print(error)
        raise
