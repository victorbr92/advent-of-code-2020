from collections import namedtuple

DIRECTIONS = [(1, 0),(0, 1),(-1, 0),(0, -1)]

Pos = namedtuple("Point", "row column value")

def read_input():
    with open("input.txt") as f:
        text = f.read().splitlines()
        return text
    
def get_score(queue, topmap):
    seen_9 = set()
    while len(queue) > 0:
        # print(f'------ {queue}')
        current = queue.pop(-1)
        current_val = int(current.value)
        if current_val == 9:
            seen_9.add(current)
            # print(f'Found 9 {current}')
            continue
        for direction in DIRECTIONS:
            next_pos = (current.row + direction[0], current.column + direction[1])
            if (0 <= next_pos[0] < len(topmap[0])) and (0 <= next_pos[1] < len(topmap)):
                next_val = topmap[next_pos[0]][next_pos[1]]
                if next_val != '.' and int(next_val) == current_val + 1:
                    to_add = Pos(row=next_pos[0], column=next_pos[1], value=int(next_val))
                    queue.append(to_add)
    return len(seen_9)


def get_rating(queue, topmap):
    score = 0
    while len(queue) > 0:
        # print(f'------ {queue}')
        current = queue.pop(-1)
        current_val = int(current.value)
        if current_val == 9:
            score += 1
            # print(f'Found 9 {current}')
            continue
        for direction in DIRECTIONS:
            next_pos = (current.row + direction[0], current.column + direction[1])
            if (0 <= next_pos[0] < len(topmap[0])) and (0 <= next_pos[1] < len(topmap)):
                next_val = topmap[next_pos[0]][next_pos[1]]
                if next_val != '.' and int(next_val) == current_val + 1:
                    to_add = Pos(row=next_pos[0], column=next_pos[1], value=int(next_val))
                    queue.append(to_add)
    return score

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    top_map = read_input()
    trailheads = []
    i = 0
    for row, line in enumerate(top_map):
        for column, letter in enumerate(line):
            if letter == '0':
                t = Pos(row=row, column=column, value=0)
                trailheads.append(t)

    for trailhead in trailheads:
        score = get_score(queue=[trailhead], topmap=top_map)
        part1 += score
    print(f"Result of part1: {part1}")
    # print("---------------------------")

    for trailhead in trailheads:
        rating = get_rating(queue=[trailhead], topmap=top_map)
        part2 += rating
    print(f"Result of part2: {part2}")
