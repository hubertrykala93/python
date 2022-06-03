"""Creating class Deck."""

from random import shuffle
from card import Card


class Deck:
    """Creating deck object."""
    def __init__(self):
        self.cards = []
        for color in Card.POSSIBLE_COLORS:
            for value in Card.POSSIBLE_VALUES:
                self.cards.append(
                    Card(color=color, value=value)
                )

    def shuffle(self):
        """Deck shuffle function."""
        shuffle(self.cards)

    def hit(self):
        """
        Discard the last card from deck.
        :return: list
        """
        return self.cards.pop()
