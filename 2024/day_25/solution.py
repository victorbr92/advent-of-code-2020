from rich import print


def read_input():
    with open("input.txt") as f:
        schematics = f.read().split('\n\n')

        keys, locks = [], []
        for i in schematics:
            var = i.splitlines()
            if var[0] == '.'*5:
                pin = [5,5,5,5,5]
                for i, l in enumerate(var):
                    for j, el in enumerate(l):
                        if el == '.':
                            pin[j] = 5 - i
                keys.append(pin)
            elif var[0] == '#'*5:
                pin = [0,0,0,0,0]
                for i, l in enumerate(var):
                    for j, el in enumerate(l):
                        if el == '#':
                            pin[j] = i
                locks.append(pin)
            else:
                print('Err')

        return keys, locks


def match(key, lock):
    for i, (k, l) in enumerate(zip(key, lock)):
        if k + l > 5:
            return False
    return True

if __name__ == "__main__":
    keys, locks = read_input()
    print(f'There are {len(keys)} keys. There are {len(locks)} locks.')

    part1 = 0
    for i, key in enumerate(keys):
        for j, lock in enumerate(locks):
            if match(key, lock):
                part1 += 1
                print(f'Match between key {i}({key}) and lock {j}({lock})')

    print(f"Result of part1: {part1}")
