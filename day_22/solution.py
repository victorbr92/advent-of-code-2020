from typing import List
from collections import deque


def parse(starting_hand: str):
    deck = [int(n) for n in starting_hand[10::].split('\n')]
    return deck


def queue_to_str(q: deque):
    return ','.join([str(i) for i in q])


class Combat:

    def __init__(self, p_1: List[int], p_2: List[int], games: int = 1):
        self.p1_deck = deque(p_1)
        self.p2_deck = deque(p_2)

    def finish(self, detailed: bool = False):

        r = 0

        while len(self.p1_deck) > 0 and len(self.p2_deck) > 0:
            r += 1
            if detailed:
                print(f'\n-- Round {r} --')
                print(f"Player 1's deck: {','.join([str(i) for i in self.p1_deck])}")
                print(f"Player 2's deck: {','.join([str(i) for i in self.p2_deck])}")

            self.play_round(detailed, r)

        score1 = sum([n * (len(self.p1_deck) - pos) for pos, n in enumerate(self.p1_deck)])
        score2 = sum([n * (len(self.p2_deck) - pos) for pos, n in enumerate(self.p2_deck)])

        if detailed:
            print(f'\n\n== Post-game results ==')
            print(f"Player 1's deck: {','.join([str(i) for i in self.p1_deck])} | Score: {score1}")
            print(f"Player 2's deck: {','.join([str(i) for i in self.p2_deck])} | Score: {score2}")

        return max(score1, score2)

    def play_round(self, detailed: bool = False, r: int = 0):
        player_1_card = self.p1_deck.popleft()
        player_2_card = self.p2_deck.popleft()

        if detailed:
            print(f'Player 1 plays: {player_1_card}')
            print(f'Player 2 plays: {player_2_card}')

        if player_1_card > player_2_card:
            self.p1_deck.append(player_1_card)
            self.p1_deck.append(player_2_card)
            print(f'Player 1 wins round {r}!')

        elif player_1_card < player_2_card:
            self.p2_deck.append(player_2_card)
            self.p2_deck.append(player_1_card)
            print(f'Player 2 wins round {r}!')


class RecursiveCombat:

    def __init__(self, p_1: List[int], p_2: List[int], games: int = 1):
        self.p1_deck = deque(p_1)
        self.p2_deck = deque(p_2)
        self.games = games
        self.stored_rounds = set()
        self.repeating = False

    def finish(self):

        r = 0

        while len(self.p1_deck) > 0 and len(self.p2_deck) > 0 and not self.repeating:
            r += 1
            print(f'\n-- Round {r} of game {self.games} --')
            print(f"Player 1's deck: {','.join([str(i) for i in self.p1_deck])}")
            print(f"Player 2's deck: {','.join([str(i) for i in self.p2_deck])}")

            self.play_round(r)

        score1 = sum([n * (len(self.p1_deck) - pos) for pos, n in enumerate(self.p1_deck)])
        score2 = sum([n * (len(self.p2_deck) - pos) for pos, n in enumerate(self.p2_deck)])

        if self.games == 1:
            print(f'\n\n== Post-game results ==')
            print(f"Player 1's deck: {queue_to_str(self.p1_deck)} | Score: {score1}")
            print(f"Player 2's deck: {queue_to_str(self.p2_deck)} | Score: {score2}")

        winner = 1 if (score1 > score2) else 2
        return 1 if self.repeating else winner

    def play_round(self, r: int = 0):
        round_cards = (queue_to_str(self.p1_deck), queue_to_str(self.p2_deck))
        if round_cards in self.stored_rounds:
            print(f'Player 1 wins round {r} of game {self.games} by repetition!')
            self.repeating = True
        else:
            self.stored_rounds.add(round_cards)
            player_1_card = self.p1_deck.popleft()
            player_2_card = self.p2_deck.popleft()

            if player_1_card <= len(self.p1_deck) and player_2_card <= len(self.p2_deck):
                print('Playing a sub-game to determine the winner...')
                sub_game = RecursiveCombat(
                    p_1=list(self.p1_deck)[0:player_1_card],
                    p_2=list(self.p2_deck)[0:player_2_card],
                    games=self.games+1,
                )
                winner = sub_game.finish()
                print(f'\n.. anyway, back to game {self.games}.')
                if winner == 2:
                    self.p2_deck.append(player_2_card)
                    self.p2_deck.append(player_1_card)
                    print(f'Player 2 wins round {r} of game {self.games}!')
                else:
                    self.p1_deck.append(player_1_card)
                    self.p1_deck.append(player_2_card)
                    print(f'Player 1 wins round {r} of game {self.games}!')

            else:
                if player_1_card > player_2_card:
                    self.p1_deck.append(player_1_card)
                    self.p1_deck.append(player_2_card)
                    # print(f'Player 1 wins round {r} of game {self.games}!')

                elif player_1_card < player_2_card:
                    self.p2_deck.append(player_2_card)
                    self.p2_deck.append(player_1_card)
                    # print(f'Player 2 wins round {r} of game {self.games}!')


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        raw_data = f.read().split('\n\n')

    player_1_deck = parse(raw_data[0])
    player_2_deck = parse(raw_data[1])

    # game = Combat(player_1_deck, player_2_deck)
    # score = game.finish(detailed=True)
    # print(score)

    game = RecursiveCombat(player_1_deck, player_2_deck)
    score = game.finish()
    print(score)
