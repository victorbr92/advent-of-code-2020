from __future__ import annotations
import re

test_molecule = 'HeOHeOHeO'
test_replacements = {'He': ['HeO', 'OHe'], 'O': ['HeHe']}


def camel_case_split(s):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', s)


def parse(data):
    r = {}
    for line in data.splitlines():
        if line:
            key, value = tuple(line.split(' => '))
            if key in r:
                r[key].append(value)
            else:
                r[key] = [value]
        else:
            break
    molecule = data.split('\n\n')[1]
    return r, molecule


def generate_new_molecules(original_molecule, replacement_dict):
    possible_cases = set()
    for replaceable in replacement_dict:
        for replacement in replacement_dict[replaceable]:
            for p in range(len(original_molecule)):
                if original_molecule[p:p + len(replaceable)] == replaceable:
                    new_molecule = original_molecule[:p] + replacement + original_molecule[p + len(replaceable):]
                    possible_cases.add(new_molecule)

    return possible_cases


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        raw_data = f.read()

    replacements, molecule = parse(raw_data)
    new_molecules = generate_new_molecules(molecule, replacements)
    print(len(new_molecules))
