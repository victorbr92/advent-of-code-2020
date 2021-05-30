from __future__ import annotations
import pandas as pd
import re

test_data = """Sue 475: vizslas: 7, perfumes: 1, trees: 6
Sue 476: vizslas: 3, samoyeds: 1, perfumes: 10
""".splitlines()

conditions_str = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
'''

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def parse_conditions(data):
    properties_values = re.findall('(\w+): (\d+)', data)
    cond = {}
    for prop in properties_values:
        cond[prop[0]] = int(prop[1])
    return cond


def parse(data):
    aunts = {}
    for line in data:
        number = re.findall('Sue (\d+):', line)[0]
        properties_values = re.findall('(\w+): (\d+)', line)

        properties = {}
        for prop in properties_values:
            properties[prop[0]] = int(prop[1])

        aunts[int(number)] = properties

    return aunts


if __name__ == '__main__':
    aunts = parse(raw_data)
    conditions = parse_conditions(data=conditions_str)
    aunts_df = pd.DataFrame.from_dict(aunts, orient='index')
    for c in conditions:
        aunts_df = aunts_df[
            (aunts_df[c] == conditions[c]) | (aunts_df[c].isna())
        ]
    print(aunts_df.to_dict('index'))

    aunts_df = pd.DataFrame.from_dict(aunts, orient='index')
    for c in conditions:
        if c in ['cats', 'trees']:
            aunts_df = aunts_df[
                (aunts_df[c] > conditions[c]) | (aunts_df[c].isna())
            ]
        elif c in ['pomeranian', 'goldfish']:
            aunts_df = aunts_df[
                (aunts_df[c] < conditions[c]) | (aunts_df[c].isna())
            ]
        else:
            aunts_df = aunts_df[
                (aunts_df[c] == conditions[c]) | (aunts_df[c].isna())
            ]
    print(aunts_df.to_dict('index'))
