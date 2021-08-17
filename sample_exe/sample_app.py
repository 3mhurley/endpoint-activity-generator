#
# Manipulator App
# Create, modify, delete, send file

# modules
from pathlib import Path, PurePath

import click


@click.command()
@click.argument("path")
@click.option("--name", default="endpoint_activity", help="Name of the file")
@click.option("--exe", default="txt", help="Extension of the file")
def main(path, name, exe):
    # Retrieve values from arguments
    original_path = Path(path)
    file = f"{name}.{exe}"

    # Create file
    file_path = create(original_path, file)

    # Manipulate file
    new_file_path = manipulate(file_path, original_path, file)

    # Send data

    # Delete file
    new_file_path.unlink()
    print("File deleted")


def create(path, name):
    # Create new file
    try:
        # Check if path exists
        if path.exists() is False:
            raise Exception(f"Path: {path} does not exist")

        # Create
        file = PurePath.joinpath(path, name)
        print(f"File created: {file}")

        # Write
        with open(file, "x") as f:
            f.write("01001000 01100101 01101100 01101100 01101111\n")  # Hello
            f.write("01010111 01101111 01110010 01101100 01100100\n")  # World

        return file

    except (FileNotFoundError, AssertionError) as error:
        print(error)
        raise


def manipulate(file_path, path, file):
    # Modify file
    try:
        # Adjust file contents
        with open(file_path, "a") as f:
            f.write("\n01100100 01101100 01110010 01101111 01010111")  # dlroW
            f.write("\n01101111 01101100 01101100 01100101 01001000")  # olleH

        # Rename file with reversed name
        file_name, file_exe = file.split(".")
        new_path_str = f"{path}\\{file_name[::-1]}.{file_exe}"
        new_path = file_path.rename(new_path_str)
        print(f"File renamed: {new_path}")

        # Change file extension
        final_path = new_path.rename(new_path.with_suffix(".text"))
        print(f"Extension changed: {final_path}")

        return final_path

    except (FileNotFoundError, AssertionError) as error:
        print(error)


if __name__ == "__main__":
    main()
