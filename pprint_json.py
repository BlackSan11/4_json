import json
import sys


def load_data(filepath):
    with open(filepath, "r") as file_with_json:
        loaded_json = file_with_json.json.loads
        return loaded_json


def reformat_json(json_for_handling):
    return json.dumps(json_for_handling, sort_keys=True, indent=4)


if __name__ == '__main__':
    print(reformat_json(load_data(sys.argv[1])))
