from pprint import pprint

TO_ADD = 10000000000000

def parse_claw(inp):
    return [int(i.split('+')[-1]) for i in inp.split(':')[-1].split(', ')]

def parse_prize(inp):
    return [int(i.split('=')[-1]) for i in inp.split(':')[-1].split(', ')]

def parse_prize_2(inp):
    return [TO_ADD + int(i.split('=')[-1]) for i in inp.split(':')[-1].split(', ')]


def read_input():
    with open("input.txt") as f:
        text = f.read().split('\n\n')
    configs = []
    for sample in text:
        A, B, P = sample.splitlines()
        config = {
            'A': parse_claw(A),
            'B': parse_claw(B),
            'P': parse_prize(P),
        }
        configs.append(config)
    return configs
    
def read_part2():
    with open("input.txt") as f:
        text = f.read().split('\n\n')
    configs = []
    for sample in text:
        A, B, P = sample.splitlines()
        config = {
            'A': parse_claw(A),
            'B': parse_claw(B),
            'P': parse_prize_2(P),
        }
        configs.append(config)
    return configs

def explore_combinations(config, limit=100):
    cost = None

    for B in range(1,1+limit):
        for A in range(1,1+limit):
            total_X = A*config['A'][0] + B*config['B'][0]
            total_Y = A*config['A'][1] +  B*config['B'][1]
            if total_X > config['P'][0] or total_Y > config['P'][1]:
                continue
            if total_X == config['P'][0] and total_Y == config['P'][1]:
                t_cost = A*3 + B*1
                if not cost or t_cost < cost:
                    cost = t_cost
                    break
    return 0 if not cost else cost

def solve_linear_equation(config):
    A = (
            config['P'][0]*config['B'][1] - config['P'][1]*config['B'][0]
        )/(
            config['A'][0]*config['B'][1] - config['A'][1]*config['B'][0]
    )
    B = (config['P'][0] -A*config['A'][0])/(config['B'][0])
    if (A % 1 == 0) and (B % 1 == 0):
        return int(A*3 + B*1)
    else:
        return 0

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    configs = read_input()
    # pprint(configs)
    for config in configs:
        cost = explore_combinations(config)
        part1 += cost
    print(f"Result of part1: {part1}")
    print("---------------------------")

    configs = read_part2()

    for config in configs:
        cost = solve_linear_equation(config)
        print(cost)
        part2 += cost
    print(f"Result of part2: {part2}")
