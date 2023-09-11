import json
from pprint import pprint


def read_json():
    with open('./data/test.json', "r") as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    res = read_json()
    pprint(res)