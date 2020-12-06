from collections import Counter

with open('input.txt', 'r') as f:
    raw_data = [line.split('\n') for line in f.read().split('\n\n')]

if __name__ == '__main__':

    group_yes = []
    common_yes = []

    for data in raw_data:
        n_answers = len(data)
        answers = ''.join(data)
        answers_count = Counter(answers)

        group_yes.append(len(answers_count))
        common_yes.append(len([answers_count[q] for q in answers_count if answers_count[q] == n_answers]))

    print(f'Union {sum(group_yes)}')
    print(f'Intersection {sum(common_yes)}')

