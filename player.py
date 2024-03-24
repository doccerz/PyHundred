from card import Card


class Player:
  def __init__ (self, name):
    self._name = name
    self._cards = []
    self._score = 0
    self._winscore = 0

  @property
  def name(self):
    return self._name

  @property
  def cards(self):
    return self._cards

  @property
  def score(self):
    return self._score

  @property
  def winscore(self):
    return self._winscore

  def add_card(self, card: Card):
    self._cards.append(card)
    self._score += card.value
    if (card.id == 1 and self._score > 21):
        self._score -= 10

  def wins(self):
    self._winscore += 1

  def clear(self):
    self._cards = []
    self._score = 0

