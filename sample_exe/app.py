#
# Manipulator App
# Create, modify, delete, send file

# modules
import os
import argparse
from pathlib import Path, PurePath


def init_argparse() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTION] [PATH]',
    description='Create, manipulate, send, and delete file',
  )
  parser.add_argument('path', help='specify the path where you want the file', type=str)

  return parser

def main():
  # Initialize parser
  parser = init_argparse()
  args = parser.parse_args()

  # Retrieve path from arguments
  path = Path(args.path)

  # Create file
  file_path = create(path)

  # Manipulate file
  new_file_path = manipulate(path, file_path)

  # Send data

  # Delete file
  new_file_path.unlink()

def create(path):
    # Create new file
  try:
    # Check if path exists
    if path.exists() is False:
      raise Exception(f'Path: {path} does not exist')

    # Create
    file = PurePath.joinpath(path, 'endpoint_activity.txt')
    print(f'Original File: {file}')

    # Write
    with open(file, 'x') as f:
      f.write('01001000 01100101 01101100 01101100 01101111\n')  # Hello
      f.write('01010111 01101111 01110010 01101100 01100100\n')  # World

    return file

  except (FileNotFoundError, AssertionError) as error:
    print(error)
    raise

def manipulate(path, file_path):
  # Modify file
  try:
    ##Adjust file contents
    with open(file_path, 'a') as f:
      f.write('\n01100100 01101100 01110010 01101111 01010111')  # dlroW
      f.write('\n01101111 01101100 01101100 01100101 01001000')  # olleH

    # Rename file
    new_path_str = f'{path}\\activity_endpoint.txt'
    new_path = file_path.rename(new_path_str)
    print(f'New path: {new_path}')

    # Change file extension
    final_path = new_path.rename(new_path.with_suffix('.text'))
    print(f'Final path: {final_path}')

    return final_path

  except (FileNotFoundError, AssertionError) as error:
    print(error)


if __name__ == "__main__":
  main()
