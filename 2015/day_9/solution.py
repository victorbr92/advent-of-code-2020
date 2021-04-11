from collections import deque, defaultdict

import numpy as np
import pandas as pd

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

test_data = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
'''.splitlines()


def parse(line: str):
    split_line = line.split(' = ')
    cities = split_line[0].split(' to ')
    city_from, city_to = cities[0], cities[1]
    distance = int(split_line[1])
    return city_from, city_to, distance


class Graph:

    def __init__(self, data):
        self.graph, self.cities, = self._parse_input(data)

    @staticmethod
    def _parse_input(data):
        adj_dict = defaultdict(dict)

        for line_data in data:
            city_from, city_to, distance = parse(line_data)
            adj_dict[city_from][city_to] = distance
            adj_dict[city_to][city_from] = distance

        return dict(adj_dict), list(adj_dict.keys())

    def shortest_path(self):

        min_total_distance = 0

        for initial_city in self.cities:
            total_distance = 0
            unvisited = set(self.cities)
            unvisited.remove(initial_city)
            print(f'\nStarting in {initial_city}')

            while unvisited:

                min_distance = 0
                for city in unvisited:

                    distance = self.graph[initial_city][city]
                    if distance > min_distance:
                        min_distance = distance
                        selected_city = city

                initial_city = selected_city
                unvisited.remove(initial_city)
                total_distance += min_distance
                print(f'Going to {selected_city} by {min_distance} summing to {total_distance}')

            if min_total_distance < total_distance:
                min_total_distance = total_distance

        print(f'\nLower total distance: {min_total_distance}')

# Adjacency Matrix: memory O(n2) access: O(1)
# Adjacency List: memory O(n + e) access: O(n)


if __name__ == '__main__':

    g = Graph(test_data)
    g.shortest_path()

    g = Graph(raw_data)
    g.shortest_path()
