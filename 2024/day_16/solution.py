from collections import defaultdict
import heapq

DIRECTIONS = {
    '^': (-1, 0),
    'v': (+1, 0),
    '>': (0, +1),
    '<': (0, -1)
}

def read_input():
    with open("input.txt") as f:
        tilemap = f.read().splitlines()
    return tilemap

def is_in_grid(pos, grid):
    return (
        0 <= pos[0] < len(grid) 
        and 0 <= pos[1] < len(grid[0]) 
        and grid[pos[0]][pos[1]] != '#'
    )


def find_min_score(start_pos, grid):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start_pos, DIRECTIONS['>']))

    while pq:
        score, pos, last_direction = heapq.heappop(pq)

        visited.add((pos, last_direction))

        if grid[pos[0]][pos[1]] == 'E':
            return score

        for direction, (dx, dy) in DIRECTIONS.items():
            new_pos = pos[0] + dx, pos[1] + dy
            if is_in_grid(new_pos, grid) and (new_pos, direction) not in visited:
                new_score = score
                new_score += 1001 if last_direction and last_direction != direction else 1
                heapq.heappush(pq, (new_score, new_pos, direction))

    return 0

def find_best_pathes(start_pos, grid, best_score):
    best_score_pos = {}
    MAX = 1e12
    backtrack = defaultdict(set)
    pq = []
    states = set()
    heapq.heappush(pq, (0, start_pos, DIRECTIONS['>']))

    while pq:
        score, pos, last_direction = heapq.heappop(pq)

        if grid[pos[0]][pos[1]] == 'E':
            if score == best_score:
                states.add((pos, last_direction))

        for direction, (dx, dy) in DIRECTIONS.items():
            new_pos = pos[0] + dx, pos[1] + dy
            if is_in_grid(new_pos, grid) and (new_pos, direction):
                new_score = score
                new_score += 1001 if last_direction and last_direction != direction else 1
                if new_score > best_score_pos.get((new_pos, direction), MAX) or new_score > best_score:
                    continue
                if new_score < best_score_pos.get((new_pos, direction), MAX):
                    backtrack[(new_pos, direction)] = set()
                    best_score_pos[(new_pos, direction)] = new_score
                backtrack[(new_pos, direction)].add((pos, last_direction))
                heapq.heappush(pq, (new_score, new_pos, direction))


    states = list(states)
    best_states = set(states)
    visited = set()
    while states:
        pos, direction = states.pop(0)
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))
        for new_pos, new_dir in backtrack.get((pos, direction), []):
            if (new_pos, new_dir) not in best_states:
                states.append((new_pos, new_dir))
                best_states.add(new_pos)

    return len(best_states)


if __name__ == "__main__":
    tilemap = read_input()
    grid = [list(line) for line in tilemap]

    for i, line in enumerate(tilemap):
        for j, el in enumerate(line):
            if el == 'S':
                start_pos = (i, j)
                break

    part1 = find_min_score(start_pos=start_pos, grid=grid)
    print(f"Result of part1: {part1}")
    print("---------------------------")
    part2 = find_best_pathes(start_pos=start_pos, grid=grid, best_score=part1)
    print(f"Result of part2: {part2}")
