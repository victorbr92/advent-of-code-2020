from typing import List, Tuple, NamedTuple, Dict
from itertools import product
from collections import Counter


class Food(NamedTuple):
    ingredients: set
    allergents: set

    @staticmethod
    def parse(food_string: str):
        food_list = food_string.strip(')').split(' (contains ')
        return Food(
            ingredients=set(food_list[0].split(' ')),
            allergents=set(food_list[1].split(', '))
        )


def get_possible_contaminants(all_foods: List[Food]):
    bad_ingredients = {}
    for food in all_foods:
        for allergent in food.allergents:
            if allergent in bad_ingredients:
                bad_ingredients[allergent] = food.ingredients.intersection(bad_ingredients[allergent])
            else:
                bad_ingredients[allergent] = food.ingredients

    return bad_ingredients


def get_clean_food(bad_ingredients: Dict[str, set], all_foods: List[Food]):
    counter = []
    contaminants = set().union(*(bad_ingredient for bad_ingredient in bad_ingredients.values()))
    for food in all_foods:
        counter += list(food.ingredients - contaminants)
    return counter


def get_dangerous_ingredients(contaminants: Dict[str, set]):
    solved = {}
    to_remove = set()
    for name in contaminants:
        if len(contaminants[name]) == 1:
            solved[name] = next(iter(contaminants[name]))
            to_remove.add(solved[name])

    while len(solved) < len(contaminants):
        for name in contaminants:
            for i in to_remove:
                if i in contaminants[name]:
                    contaminants[name].remove(i)

            if len(contaminants[name]) == 1:
                solved[name] = next(iter(contaminants[name]))
                to_remove = {v for v in solved.values()}

    result = ''
    for value in sorted(solved.keys()):
        result += ',' + solved[value]
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        raw_data = f.read().splitlines()
        foods = [Food.parse(food_string=e) for e in raw_data]

    possible_contaminants = get_possible_contaminants(foods)
    non_contaminants = get_clean_food(possible_contaminants, foods)
    print(len(non_contaminants))
    print(get_dangerous_ingredients(possible_contaminants))
