import json


def load_data(filepath):
    f = open(filepath, "r")
    filetext = f.read()
    return filetext

def pretty_print_json(data):
    print(data)
    res = json.loads(data)
    print(json.dumps(res, sort_keys=True, indent=4))

if __name__ == '__main__':
    pyth = input('Enter pyth: ')
    pretty_print_json(load_data(pyth))
