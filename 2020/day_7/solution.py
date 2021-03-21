from typing import Dict
import re

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def parse_from_str(definition: str) -> Dict[str, Dict[str, int]]:
    color, remaining = definition.split(' bags contain ')

    bags = {}
    bags_inside = {}

    if remaining != 'no other bags.':
        remaining_list = remaining.split(',')

        for item_str in remaining_list:
            inner_amount, inner_color = re.findall(r"(\d+) (.+) bag", item_str)[0]
            bags_inside[inner_color] = int(inner_amount)

    bags[color] = bags_inside
    return color, bags_inside


def check_for_shiny_gold(bags: Dict):
    has_shiny_gold = 0
    for bag_color in bags:
        bags_to_check = set(bags[bag_color].keys())
        while len(bags_to_check) > 0:
            if 'shiny gold' in bags_to_check:
                has_shiny_gold += 1
                break
            else:
                present = bags_to_check.copy()
                for color in present:
                    bags_to_check.remove(color)
                    bags_to_check |= bags[color].keys()
    return has_shiny_gold


def check_inside(
        color: str,
        reference: Dict,
):
    acc = 0
    bags_to_check = [(color, 1)]
    while bags_to_check:
        color, parent_amount = bags_to_check.pop()
        inside_bags = reference[color]
        for color, amount in inside_bags.items():
            acc += parent_amount*amount
            bags_to_check.append((color, parent_amount*amount))
    return acc


def sum_bags_inside(color: str, reference: Dict[str, Dict[str, int]], level: int = 0, cache: Dict = {}):
    # space = '\t'*level
    level += 1
    count = 0
    if len(reference[color]):
        for inside_color, amount in reference[color].items():
            count += amount
            bag_sum = sum_bags_inside(color=inside_color, reference=bags, level=level, cache=cache)
            count += amount * bag_sum
            # print(f'{space}Finished loop of {color},{amount} with {count}')
        return count
    else:
        return 0


if __name__ == '__main__':

    bags = {}
    for line in raw_data:
        c, bags_inside = parse_from_str(line)
        bags[c] = bags_inside

    n_has_shiny_gold = check_for_shiny_gold(bags=bags)
    print(f'{n_has_shiny_gold} has shiny gold inside it.')

    total = sum_bags_inside(color='shiny gold', reference=bags)
    print(f'{total} are inside shiny gold.')

