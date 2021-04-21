import logging
import sys
import json


def load_json(path):
    with open(path) as _f:
        return json.load(_f)


def main(arguments):
    """
    Problem 1: Path doesn't exist
    Problem 2: Path is not JSON
    """
    # the last argument is the JSON file
    json_file = arguments[-1]
    print(f"The JSON file is: {json_file}")

    try:
        loaded_json = load_json(json_file)
    except FileNotFoundError:
        logging.exception("file doesn't exist")
        print(f"Couldn't use {json_file} as input, file doesn't exist")
        sys.exit(1)
    except json.decoder.JSONDecodeError as error:
        print(f"Couldn't load {json_file} as valid JSON. Error is: {error}")
        sys.exit(2)

    print(f"Name:  {loaded_json['name']}")
    print(f"Last Name: {loaded_json['last_name']}")

if __name__ == '__main__':
    main(sys.argv)
