from typing import List, Dict, Tuple

with open('input.txt', 'r') as f:
    raw_data = f.read().split('\n\n')

ALL_CRITERIA = {}
for r in raw_data[0].split('\n'):
    name = r.split(': ')[0]
    value = r.split(': ')[1].split(' or ')
    ALL_CRITERIA[name] = [(int(v.split('-')[0]), int(v.split('-')[1])) for v in value]

MY_TICKET = raw_data[1].split('\n')[1]
NEARBY_TICKETS = raw_data[2].split('\n')[1::]


class Ticket:

    def __init__(self, definition: str):
        self.data = [int(v) for v in definition.split(',')]

    def validate(self, criteria: Dict[str, List[Tuple[int,int]]]) -> List[int]:
        possible = set(self.data)
        valid = set()
        for value in possible:
            for name in criteria:
                for limit in criteria[name]:
                    minimimum = limit[0]
                    maximum = limit[1]
                    if minimimum <= value <= maximum:
                        valid.add(value)

        return list(possible - valid)

    def validate_field(self, criteria: List[Tuple[int, int]]) -> List[int]:
        """
        Returns as possible positions for this field in this ticket
        """
        possible = self.data
        score = set()
        for position, value in enumerate(possible):
            for limit in criteria:
                minimimum = limit[0]
                maximum = limit[1]
                if minimimum <= value <= maximum:
                    score.add(position)

        return score


def decompose(positions: Dict[str, set]):
    solved = {}
    to_remove = set()
    for name in positions:
        if len(positions[name]) == 1:
            solved[name] = next(iter(positions[name]))
            to_remove.add(solved[name])
    print(f"What can be solved first is {solved}")

    while len(solved) < len(positions):
        for name in positions:
            for i in to_remove:
                if i in positions[name]:
                    positions[name].remove(i)

            if len(positions[name]) == 1:
                solved[name] = next(iter(positions[name]))
                to_remove = {v for v in solved.values()}

    return solved


if __name__ == '__main__':

    my_ticket = Ticket(definition=MY_TICKET)
    nearby_tickets = [Ticket(definition=t) for t in NEARBY_TICKETS]

    invalid_values = []
    valid_tickets = [my_ticket]

    for ticket in nearby_tickets:
        to_add = ticket.validate(ALL_CRITERIA)
        invalid_values += to_add
        if len(to_add) == 0:
            valid_tickets.append(ticket)

    print(f'Ticket scanning error rate {sum(invalid_values)}')
    print(f'We have {len(valid_tickets)} valid tickets.')

    valid = {}
    for name in ALL_CRITERIA.keys():
        possible_positions = []
        for ticket in valid_tickets:
            result = ticket.validate_field(criteria=ALL_CRITERIA[name])
            possible_positions.append(result)
        valid[name] = set.intersection(*possible_positions)

    # Start with the class which has less possibles and eliminate progressively
    solved = decompose(valid)
    print('\n')
    result = 1
    for name in solved:
        if name.startswith('departure'):
            print(f'{name} - position: {solved[name]} - my value: {my_ticket.data[solved[name]]}')
            result *= my_ticket.data[solved[name]]
    print(f'\nResult: {result}')
