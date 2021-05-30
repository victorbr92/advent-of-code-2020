from __future__ import annotations
from typing import Dict, List
import re
from itertools import permutations

test_data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".splitlines()


with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def parse(data: List[str]):
    ingredients = {}
    for line in data:
        name = line.split(':')[0]
        properties_values = re.findall('\-*\d+', line)
        ingredients[name] = {
            'capacity': int(properties_values[0]),
            'durability': int(properties_values[1]),
            'flavor': int(properties_values[2]),
            'texture': int(properties_values[3]),
            'calories': int(properties_values[4]),
        }
    return ingredients


class Recipe:

    def __init__(self, ing: Dict, amount: List = None):
        self.ingredients_properties = ing
        if not amount:
            amount = [int(100 / len(self.ingredients_properties)) for _ in self.ingredients_properties]
        self.ingredients_amounts = {ingredient: amount[i] for i, ingredient in enumerate(ing)}

    @property
    def total_score(self):
        score = 1
        for prop in ['capacity', 'durability', 'flavor', 'texture']:
            score *= max(sum(
                self.ingredients_amounts[ing]*self.ingredients_properties[ing][prop] for ing in self.ingredients_amounts
            ), 0)
        return score

    @property
    def partial_score(self):
        score = {}
        for prop in ['capacity', 'durability', 'flavor', 'texture']:
            score[prop] = max(sum(
                self.ingredients_amounts[ing] * self.ingredients_properties[ing][prop] for ing in
                self.ingredients_amounts
            ), 0)
        return score

    @property
    def calories(self):
        return sum(
                self.ingredients_amounts[ing]*self.ingredients_properties[ing]['calories'] for ing in self.ingredients_amounts
            )


def find_maximum(ingredients_available: Dict, total_calories: int = None):
    maximum = 0
    m_recipe = None

    for values in possible_values(elements=len(ingredients_available), target=100):
        r = Recipe(ing=ingredients_available, amount=values)

        if r.total_score > maximum:
            if total_calories:
                if r.calories == total_calories:
                    maximum = r.total_score
                    m_recipe = r
            else:
                maximum = r.total_score
                m_recipe = r

    return m_recipe


def possible_values(elements, target):
    values = [i for i in range(target+1)]
    for c in permutations(values, elements):
        if sum(c) == target:
            yield c


if __name__ == '__main__':
    ingredients = parse(test_data)
    recipe = Recipe(ingredients, [44, 56])
    assert recipe.total_score == 62842880

    ingredients = parse(test_data)
    recipe = find_maximum(ingredients)
    assert recipe.total_score == 62842880

    ingredients = parse(test_data)
    recipe = find_maximum(ingredients, total_calories=500)
    assert recipe.total_score == 57600000

    ingredients = parse(raw_data)
    recipe = find_maximum(ingredients)
    print(recipe.total_score, recipe.partial_score)

    ingredients = parse(raw_data)
    recipe = find_maximum(ingredients, total_calories=500)
    print(recipe.total_score, recipe.partial_score)
