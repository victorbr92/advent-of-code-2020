from rich import print
import matplotlib.pyplot as plt
import networkx as nx

def read_input():
    with open("input.txt") as f:
        return [i.split('-') for i in f.read().splitlines()]

if __name__ == "__main__":
    cons = read_input()
    graph = nx.from_edgelist(cons)
    print(graph)
    total = 0
    triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]
    # print(len(triangles))
    for cl in triangles:
        ok = False
        for cmp in cl:
            if cmp.startswith('t'):
                ok = True
                # print(cl)
                break
        total += int(ok)
    print(total)
    print(f"Result of part1: {total}")
    print('----------------------------')
    largest=','.join(sorted(max([clique for clique in nx.enumerate_all_cliques(graph)], key=len)))
    print(f"Result of part2: {largest}")
