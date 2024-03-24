class Card:
    _card_names = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    _card_value = {
        1: 11,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10
    }

    def __init__(self, id):
        self._id = id

    def __str__(self):
        return self._card_names[self._id]

    def __repr__(self):
        return f'"{str(self)}"'

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._card_value[self._id]
