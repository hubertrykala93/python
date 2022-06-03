"""Creating class Card."""

from exceptions import InvalidColor, InvalidValue


class Card:
    """Creating card object."""
    POSSIBLE_COLORS = {
        'spades': '\u2664',
        'diamonds': '\u2662',
        'hearts': '\u2661',
        'clubs': '\u2667',
    }

    POSSIBLE_VALUES = list(range(2, 11)) + [
        'Ace',
        'King',
        'Queen',
        'Jack'
    ]

    def __init__(self, color: str, value: [int, str]):
        if color not in self.POSSIBLE_COLORS:
            raise InvalidColor('Invalid card color!')

        self.color = self.POSSIBLE_COLORS[color]

        if value not in self.POSSIBLE_VALUES:
            raise InvalidValue('Invalid card value!')

        self.value = value

    def __repr__(self):
        return f'{self.value} -> {self.color}'
