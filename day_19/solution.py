from typing import List, Dict, Set
from itertools import product


def parse_rules(line_list: List[str]) -> Dict:
    """
    Rules can be a set of strings or a List of List of strings.
    """
    rules_dict = {}
    for line in line_list.splitlines():
        k, rule = line.split(': ')[0], line.split(': ')[1]
        if rule.startswith('"'):
            rule = {rule[1:-1]}
        elif rule[0].isdigit():
            additive_rules = rule.split(' | ')
            rule = []
            for single_rule in additive_rules:
                elements = [int(e) for e in single_rule.split()]
                rule.append(elements)

        rules_dict[int(k)] = rule

    return rules_dict


def decode_rules(key: int, rules_dict: Dict) -> Set[str]:

    if isinstance(rules_dict[key], set):
        return rules_dict

    result = set()
    for parts_or in rules_dict[key]:
        final = set()
        for element in parts_or:
            while isinstance(element, int):
                rules_dict = decode_rules(key=element, rules_dict=rules_dict)
                element = rules_dict[element]
            if final:
                final = {''.join(e) for e in list(product(final, element))}
            else:
                final |= element
        result |= final

    rules_dict[key] = result
    return rules_dict


def modify_list_recursion(key: int, rules_dict: Dict) -> List:
    first_part = rules_dict[key][0]
    second_part = rules_dict[key][1]

    result = [first_part]

    if key in second_part:
        pos = second_part.index(key)
        b = second_part[0:pos]
        e = second_part[pos+1::]
        for _ in range(1, 3):
            s = b + first_part + e
            result.append(s)
            pos += 1
            b = s[0:pos]
            e = s[pos::]

    return result


if __name__ == '__main__':

    PART2 = False
    with open('input.txt', 'r') as f:
        raw_data = f.read().split('\n\n')
        rules = parse_rules(line_list=raw_data[0])
        messages = raw_data[1].splitlines()

    MAX_LEN = max([len(m) for m in messages])
    if PART2:
        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]
        rules[8] = modify_list_recursion(rules_dict=rules, key=8)
        rules[11] = modify_list_recursion(rules_dict=rules, key=11)

    rules = decode_rules(key=0, rules_dict=rules)
    count_0 = sum([True for message in messages if message in rules[0]])
    print(count_0)
