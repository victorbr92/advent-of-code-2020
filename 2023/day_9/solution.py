def read():
    with open("day_9/input.txt") as f:
        input = f.read()
    return input

def get_diff(l):
    return [j-i for i, j in zip(l[:-1], l[1:])]

if __name__ == "__main__":
    inp = read()
    lines = inp.splitlines()
    part_1 = 0
    part_2 = 0
    for line in lines:
        sequence = [int(i) for i in line.split(' ')]
        seq_sum = 0
        condition = all(s==0 for s in sequence)
        initial = sequence[0]
        r = 0
        while not condition:
            part_1 += sequence[-1]
            if r % 2 == 0:
                seq_sum += sequence[0]
                part_2 += sequence[0]
            else:
                seq_sum -= sequence[0]
                part_2 -= sequence[0]
            sequence = get_diff(sequence)
            condition = all(s==0 for s in sequence)
            r += 1
        print('---', seq_sum)
    print('PART 1')
    print(part_1)
    print('PART 2')
    print(part_2)
