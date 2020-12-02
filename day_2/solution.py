with open('input.txt', 'r') as f:
    lines = [line.split(':') for line in f.read().splitlines()]
    inputs = [(int(line[0].split()[0].split('-')[0]), int(line[0].split()[0].split('-')[1]), line[0].split()[1], line[1]) for line in lines]


def evaluate_pwd_old(case):
    letter = case[2]
    pwd = case[3]
    low, high = case[0], case[1]
    return low <= pwd.count(letter) <= high


def evaluate_pwd(case):
    letter = case[2]
    pwd = case[3]
    pos1, pos2 = case[0], case[1]
    return (letter == pwd[pos1]) ^ (letter == pwd[pos2])


if __name__ == '__main__':
    correct_old_policy = sum([evaluate_pwd_old(case) for case in inputs])
    print(f'Correct cases according to old policy {correct_old_policy}')

    correct_policy = sum([evaluate_pwd(case) for case in inputs])
    print(f'Correct cases according to new policy {correct_policy}')
