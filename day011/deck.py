import random

from card import Card


class Deck:

    def __init__(self):
        self.clear()

    def clear(self):
        self.cards = []
        # Create 4x card set
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
