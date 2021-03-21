from timeit import default_timer as timer

TEST_INPUT = '389125467'
INPUT = '364289715'


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class CrabGame:

    def __init__(self, labeling: str):
        cups = [int(n) for n in labeling]
        self.min = min(cups)
        self.nodes = {}

        prev = None
        for pos in range(len(cups)-1, -1, -1):
            node = Node(value=cups[pos], nxt=None)
            node.next = prev
            self.nodes[cups[pos]] = node
            prev = node

        self.current = self.nodes[cups[0]]
        self.nodes[cups[len(cups)-1]].next = self.nodes[cups[0]]

        self.moves = 0

    def move(self):
        self.moves += 1

        pickups = []
        pickup = self.current.next
        for _ in range(3):
            pickups.append(pickup.value)
            pickup = pickup.next
        self.current.next = pickup
        destination = self.select_next_destination(pickups=pickups)
        dest_node = self.nodes[destination]

        left_before = dest_node.next
        dest_node.next = self.nodes[pickups[0]]
        self.nodes[pickups[0]].next = self.nodes[pickups[1]]
        self.nodes[pickups[1]].next = self.nodes[pickups[2]]
        self.nodes[pickups[2]].next = left_before
        self.current = self.current.next

    def n_moves(self, n=10):
        for _ in range(n):
            self.move()

    def select_next_destination(self, pickups):
        destination = self.current.value - 1
        while destination >= self.min:
            if destination not in pickups:
                return destination

            destination -= 1

        return max(x for x in self.nodes.keys() if x not in pickups)

    @property
    def result(self):
        s = self.nodes[1]
        node = s.next
        r = ''
        while node != s:
            r += str(node.value)
            node = node.next
        return r


class CrabGame2:

    def __init__(self, labeling: str):
        cups = [int(n) for n in labeling]
        self.min = min(cups)
        self.nodes = {}

        higher = None
        for pos in range(len(cups)-1, -1, -1):
            node = Node(value=cups[pos], nxt=None)
            node.next = higher
            self.nodes[cups[pos]] = node
            higher = node

        for value in range(1_000_000, 9, -1):
            node = Node(value=value, nxt=higher)
            self.nodes[value] = node
            higher = node

        self.nodes[cups[-1]].next = self.nodes[10]
        self.current = self.nodes[cups[0]]
        self.moves = 0

    def move(self):
        self.moves += 1

        pickups = []
        pickup = self.current.next
        for _ in range(3):
            pickups.append(pickup.value)
            pickup = pickup.next
        self.current.next = pickup
        destination = self.select_next_destination(pickups=pickups)
        dest_node = self.nodes[destination]

        left_before = dest_node.next
        dest_node.next = self.nodes[pickups[0]]
        self.nodes[pickups[0]].next = self.nodes[pickups[1]]
        self.nodes[pickups[1]].next = self.nodes[pickups[2]]
        self.nodes[pickups[2]].next = left_before
        self.current = self.current.next

    def n_moves(self, n=10):
        for _ in range(n):
            self.move()

    def select_next_destination(self, pickups):
        destination = self.current.value - 1
        while destination >= self.min:
            if destination not in pickups:
                return destination

            destination -= 1

        return max(x for x in self.nodes.keys() if x not in pickups)

    @property
    def result(self):
        s = self.nodes[1]
        n1 = s.next.value
        n2 = s.next.next.value
        print(n1, n2)
        return n1*n2


if __name__ == '__main__':
    start = timer()
    game = CrabGame(labeling=INPUT)
    game.n_moves(100)
    end = timer()
    print('\n', game.result)
    print('Elapsed time: ', end - start)

    start = timer()
    game = CrabGame2(labeling=INPUT)
    game.n_moves(10_000_000)
    end = timer()
    print('\n', game.result)
    print('Elapsed time: ', end - start)
