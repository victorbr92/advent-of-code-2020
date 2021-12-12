import networkx as nx
from collections import deque, Counter
from typing import List

TEST_STR = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_graph = nx.Graph()
test_graph.add_edges_from([e.split('-') for e in TEST_STR.splitlines()])

TEST_STR_2 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

test_graph_2 = nx.Graph()
test_graph_2.add_edges_from([e.split('-') for e in TEST_STR_2.splitlines()])

with open('input.txt', 'r') as f:
    graph = nx.Graph()
    graph.add_edges_from([e.split('-') for e in f.read().splitlines()])


def can_add(node: str, path: List[str], part_2: bool):
    to_add = True
    if node == 'start':
        to_add = False
    elif node.lower() == node and node not in ['start', 'end']:
        # only enters if it is a small node now
        small_caves_path = [n for n in path if (n.lower() == n and n not in ['start', 'end'])]
        small_caves_amount = Counter(small_caves_path)

        if not part_2:
            # check if this small cave is already there
            if small_caves_amount[node] >= 1:
                to_add = False
        else:
            # check if there is some small cave already with 2 and if
            will_be_bigger_than_2 = small_caves_amount[node] >= 1
            has_bigger_than_2 = any([small_caves_amount[v] >= 2 for v in small_caves_amount])
            if will_be_bigger_than_2 and has_bigger_than_2:
                to_add = False

    return to_add


def find_all_paths(
        g: nx.Graph,
        initial: str = 'start',
        end: str = 'end',
        report: bool = False,
        part_2: bool = False
):
    path = [initial]
    queue = deque()
    queue.append(path.copy())
    c = 0

    while queue:
        path = queue.popleft()
        last = path[-1]

        if last == end:
            c += 1
            if report:
                print(','.join(n for n in path))

        else:
            neighbors = list(g.neighbors(last))
            for current_node in neighbors:
                if can_add(current_node, path, part_2):
                    new = path.copy()
                    new.append(current_node)
                    queue.append(new)

    return c


if __name__ == '__main__':
    print('===== PART1 ======')
    print('> test input')
    print(find_all_paths(test_graph))
    print(find_all_paths(test_graph_2))
    print('> input')
    print(find_all_paths(graph))

    print('===== PART2 ======')
    print('> test input')
    print(find_all_paths(test_graph, part_2=True))
    print(find_all_paths(test_graph_2, part_2=True))
    print('> input')
    print(find_all_paths(graph, part_2=True))
