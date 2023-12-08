from itertools import cycle
from math import lcm 

def read():
    with open("day_8/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    inp = read()
    lines = inp.splitlines()
    print('PART 1')
    nodes = {}
    instructions = lines[0]
    rank = []
    current_nodes = []
    for line in lines[2:]:
        parsed_line = line.split(' = ')
        node = parsed_line[0]
        if node[2] == 'A':
            current_nodes.append(node)
        paths = parsed_line[1][1:-1].split(', ')
        nodes[node] = (paths[0], paths[1])
    # node = 'AAA'
    # steps = 0
    # for direction in cycle(instructions):
    #     # print(node)
    #     if node == 'ZZZ':
    #         break
    #     paths = nodes[node]
    #     if direction == 'L':
    #         node = paths[0]
    #     else:
    #         node = paths[1]
    #     steps += 1
    # print(steps)
    print('PART 2')
    print(current_nodes)
    scores = [0 for _ in current_nodes]
    cycles = [0 for _ in current_nodes]
    part_2 = 0
    for direction in cycle(instructions):
        score = 0
        new_nodes = []
        for i, current_node in enumerate(current_nodes):
            paths = nodes[current_node]
            if direction == 'L':
                node = paths[0]
            else:
                node = paths[1]
            new_nodes.append(node)
            if node[2] == 'Z':
                scores[i] = 1
                cycles[i] = part_2+1
                print(i, node, part_2+1)
        current_nodes = new_nodes.copy()
        part_2 += 1
        if sum(scores) == len(current_nodes):
            break
    print(cycles)
    print(lcm(*cycles))
