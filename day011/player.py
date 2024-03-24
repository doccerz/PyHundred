from card import Card
from deck import Deck


class Player:

    def __init__(self, name):
        self._name = name
        self._score = 0
        self.clear()

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        return self._cards

    @property
    def hand(self):
        return self._hand

    @property
    def score(self):
        return self._score

    @property
    def bust(self):
        return self._bust

    def set_deck(self, deck: Deck):
        self._deck = deck

    def hit(self):
        card = self._deck.draw()
        self._cards.append(card)
        self._hand += card.value
        # set soft if ace
        self.is_soft = (self.is_soft or card.id == 1)

        # reduce aces values if score is over 21
        if self._hand > 21:
            self._hand = 0
            # reset soft value
            self.is_soft = False
            sorted_cards = sorted(self._cards, key=lambda x: x.value)
            for c in sorted_cards:
                self._hand += c.value
                if c.id == 1 and self._hand > 21:
                    self._hand -= 10
                else:  # set to soft
                    self.is_soft = (self.is_soft or c.id == 1)
        # check if hand is still bust
        self._bust = (self._hand > 21)
        self.round_message = (self._bust and "BUST!")
        print(f"{self._name} has drawn {card}")

    def wins(self):
        self._score += 1

    def clear(self):
        self._cards = []
        self._hand = 0
        self.is_soft = False
        self._bust = False
        self.round_message = ""
