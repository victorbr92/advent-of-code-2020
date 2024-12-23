from rich import print
from rich.panel import Panel

DIRECTIONS = [(-1, 0),(+1, 0),(0, +1),(0, -1)]
POSSIBLE_SKIPS = [
    (-2, 0),(+2, 0),(0, +2),(0, -2),
    (-1, +1),(+1, +1),(-1, -1),(+1, -1),
]

def read_input():
    with open("input.txt") as f:
        tilemap = f.read().splitlines()
    return tilemap

def show_grid(grid):
    s = '\n'.join(''.join(f' {str(cell).zfill(2)} ' if cell is not None else ' ## ' for cell in row) for row in grid)
    return Panel.fit(s, style="bold blue")

def is_in_grid(pos, grid):
    return (0 <= pos[0] < len(grid)  and 0 <= pos[1] < len(grid[0]))


def fill_distances(start_pos, grid):
    distances = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    x, y = start_pos
    distances[x][y] = 0
    dist = 0
    while grid[x][y] != 'E':
        for (dx, dy) in DIRECTIONS:
            new_pos = x + dx, y + dy
            nx, ny = new_pos

            if is_in_grid(new_pos, grid):
                if grid[nx][ny] != '#' and distances[nx][ny] is None:
                    dist += 1
                    distances[nx][ny] = dist
                    x, y = nx, ny
                    break

    print(show_grid(distances))
    return distances

def find_cheats(dist):
    dist_possibilities = {}
    for x, l in enumerate(dist):
        for y, _ in enumerate(l):
            if dist[x][y] is None:
                continue
            for (dx, dy) in POSSIBLE_SKIPS:
                nx, ny = x + dx, y + dy
                if is_in_grid((nx, ny), dist) and dist[nx][ny] is not None:
                    skipped = dist[nx][ny] - dist[x][y] - 2
                    if skipped > 0:
                        # print(f'From {x,y} ({dist[x][y]}) to {nx, ny} ({dist[nx][ny]})')
                        dist_possibilities[skipped] = dist_possibilities.get(skipped, 0) + 1
    return dist_possibilities


def find_cheats_part2(dist, max_cheats=20, min_skipped=50):
    dist_possibilities = {}
    for x, l in enumerate(dist):
        for y, _ in enumerate(l):
            if dist[x][y] is None:
                continue
            for dx in range(-20, 21):
                for dy in range(-20, 21):
                    steps = abs(dx) + abs(dy)
                    if steps > max_cheats:
                        continue
                    nx, ny = x + dx, y + dy
                    if is_in_grid((nx, ny), dist) and dist[nx][ny] is not None:
                        skipped = dist[nx][ny] - dist[x][y] - steps
                        if skipped >= min_skipped:
                            # print(f'From {x,y} ({dist[x][y]}) to {nx, ny} ({dist[nx][ny]})')
                            dist_possibilities[skipped] = dist_possibilities.get(skipped, 0) + 1
    return dist_possibilities



if __name__ == "__main__":
    tilemap = read_input()
    grid = [list(line) for line in tilemap]
    walls = set()

    for i, line in enumerate(tilemap):
        for j, el in enumerate(line):
            if el == 'S':
                start_pos = (i, j)
                break

    distances = fill_distances(start_pos=start_pos, grid=grid)

    possible_cheats = find_cheats(dist=distances)
    part1 = 0
    for skipped, amount in possible_cheats.items():
        if skipped >= 100:
            part1 += amount
    print(f"Result of part1: {part1}")
    print('----------------------------')
    possible_cheats = find_cheats_part2(dist=distances, max_cheats=20, min_skipped=100)
    part2 = 0
    for skipped in sorted(possible_cheats.keys()):
        # print(f'- There are {possible_cheats[skipped]} cheats that save {skipped} ps')
        if skipped >= 100:
            part2 += possible_cheats[skipped]
    print(f"Result of part2: {part2}")

