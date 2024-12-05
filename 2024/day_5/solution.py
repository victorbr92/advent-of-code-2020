def read():
    with open("input.txt") as f:
        return f.read().splitlines()

def correct_order(update, rules):
    for rule in rules:
        if (rule[0] in update) and (rule[1] in update):
            index_first = update.index(rule[0])
            index_second = update.index(rule[1])
            if index_second < index_first:
                update[index_first] = rule[1]
                update[index_second] = rule[0]
    return update

def check_update(update, rules):
    for rule in rules:
        if (rule[0] in update) and (rule[1] in update):
            index_first = update.index(rule[0])
            index_second = update.index(rule[1])
            if index_second < index_first:
                return 0
    return update[len(update)//2]


if __name__ == "__main__":
    text = read()
    first_list = []

    rules = []
    updates = []
    for line in text:
        if '|' in line:
            rules.append([int(i) for i in line.split('|')])
        if ',' in line:
            updates.append([int(i) for i in line.split(',')])

    part1 = 0
    incorrectly_ordered = []
    for update in updates:
        mid = check_update(update=update, rules=rules)
        if mid == 0:
            incorrectly_ordered.append(update)
        part1 += mid
    print(part1)
    print('-------')

    part2 = 0
    for update in incorrectly_ordered:
        incorrect = True
        i = 0
        while incorrect:
            update = correct_order(update, rules)
            mid = check_update(update=update, rules=rules)
            if mid > 0:
                mid = update[len(update)//2]
                part2 += mid
                incorrect = False
    print(part2)
