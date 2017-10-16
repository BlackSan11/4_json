import json
import sys
def load_data(filepath):
    file_with_json = open(filepath, "r")
    json_from_file = file_with_json.read()
    return json_from_file
def pretty_print_json(json_for_handling):
    loaded_json = json.loads(json_for_handling)
    return json.dumps(loaded_json, sort_keys=True, indent=4)
if __name__ == '__main__':
    path = sys.argv[1]
    print(pretty_print_json(load_data(path)))