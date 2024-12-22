import heapq

DIRECTIONS = [(-1, 0),(+1, 0),(0, +1),(0, -1)]

def read_input():
    with open("input.txt") as f:
        ms = [m.split(',') for m in f.read().splitlines()]
    return [(int(m[0]), int(m[1])) for m in ms]


def find_shortest_path(sx, sy, ex, ey, fallen):
    pq = []
    heapq.heappush(pq, (0, sx, sy))
    visited = {(sx, sy)} | fallen

    while pq:
        steps, x, y = heapq.heappop(pq)
        if (x, y) == (ex, ey):
            # print('Found end')
            return steps


        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (0 <= nx <= ex) and (0 <= ny <= ey):
                if (nx, ny) not in visited:
                    new_steps = steps + 1
                    visited.add((nx, ny))
                    heapq.heappush(pq, (new_steps, nx, ny))

    return -1

if __name__ == "__main__":
    sx, sy = 0,0
    ex, ey = 70,70
    fall_limit = 1024
    ms = read_input()
    fallen = set(ms[:fall_limit])

    part1 = find_shortest_path(sx, sy, ex, ey, fallen)
    print(f"Result of part1: {part1}")
    print("---------------------------")

    ans = part1
    while ans != -1:
        fall_limit += 1
        fallen = set(ms[:fall_limit])
        ans = find_shortest_path(sx, sy, ex, ey, fallen)
        print(f'Found end on {ans} steps. Last bytes was {ms[fall_limit]}')

    print(f"Result of part2: {fall_limit}")
