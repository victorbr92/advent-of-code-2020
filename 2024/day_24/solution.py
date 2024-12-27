from rich import print


OPS_DICT = {
    'AND': lambda x,y: x & y,
    'OR': lambda x,y: x | y,
    'XOR': lambda x,y: x ^ y,
}


def read_input():
    with open("input.txt") as f:
        gates, ops = f.read().split('\n\n')

        numbers = {}
        for i in gates.splitlines():
            var, n = i.split(': ')
            numbers[var] = int(n)

        ops_final = []
        for i in ops.splitlines():
            ops_final.append(i.split(' '))

        return numbers, ops_final

if __name__ == "__main__":
    numbers, ops = read_input()

    for op in ops:
        var1, operator, var2 = numbers[op[0]], op[1], numbers[op[2]]
        numbers[op[4]] = OPS_DICT[operator](var1, var2)
        print(op, numbers[op[4]])
    total = 0
    print(f"Result of part1: {total}")
    print('----------------------------')
    print(f"Result of part2: {0}")
