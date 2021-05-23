import json
import re

TEST = '[-1,{"a":1}]'

with open('input.json', 'r') as f:
    raw_data = f.read()

with open('input.json', 'r') as f:
    json_data = json.load(f)


def find_numbers_re(document: str):
    numbers = re.findall('-?[0-9]+', document)
    return sum([int(i) for i in numbers])


def sum_numbers(obj):
    if isinstance(obj, int):
        return obj

    if isinstance(obj, list):
        return sum([sum_numbers(i) for i in obj])

    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0

        return sum([sum_numbers(i) for i in obj.values()])

    else:
        return 0


if __name__ == '__main__':
    result_1 = find_numbers_re(raw_data)
    result_2 = sum_numbers(json_data)
    print(result_1, result_2)
