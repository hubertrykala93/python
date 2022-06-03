"""Creating class Player."""

from card import Card
from exceptions import GameOverException


class Player:
    """Creating player object."""
    def __init__(self):
        self.cards = []

    def take_card(self, card: Card):
        """
        Drawing card by player.
        :param card: list
        :return: None
        """
        self.cards.append(card)

    def calculate_points(self) -> int:
        """
        Calculate the number of points for user and croupier.
        :return: int
        """
        points = 0
        number_of_aces = len([card for card in self.cards if card.value == 'Ace'])

        if number_of_aces == 2 and len(self.cards) == 2:
            return 21

        if number_of_aces == 1 and len(self.cards) == 2:
            points = 10

        for card in self.cards:
            if card.value == 'Ace':
                points += 1
            elif card.value in ['Jack', 'Queen', 'King']:
                points += 10
            else:
                points += card.value

        if points > 21:
            raise GameOverException('The player has exceed 21 points.')

        return points
