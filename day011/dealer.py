from player import Player


class Dealer(Player):

    def __init__(self):
        super().__init__("DEALER")

    def hits(self):
        # keep on hitting until score is 17 or more, or if soft 17
        while self._hand < 17 or (self._hand == 17 and self.is_soft):
            self.hit()

    @property
    def facedown(self):
        return ['*'] + self._cards[1:]
