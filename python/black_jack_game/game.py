"""Creating class Game."""

from deck import Deck
from player import Player
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException


class Game:
    """Creating game object."""

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        """
        Printing menu.
        :return: None
        """
        print('What do you want to do?\n')
        print('1 - Draw a card.')
        print('2 - Pass.')

    def _croupier_plays(self, user_points: int) -> int:
        """
        Cheking croupier and player points and taking card by croupier
        while number of croupier points are smaller than player.
        :param user_points: int
        :return: int
        """
        croupier = Player()
        while croupier.calculate_points() < user_points:
            croupier.take_card(self.deck.hit())

        print(f'Croupier points -> {croupier.calculate_points()}.')
        return croupier.calculate_points()

    def _user_plays(self) -> int:
        """
        Creating Player class instance, adding cards to player hands
        and printing by while loop private static method 'menu' while the game not is over.
        :return: int
        """
        user = Player()
        for _ in range(2):
            card = self.deck.hit()
            user.take_card(card=card)

        print(user.cards)
        print(f'{user.calculate_points()} \n')
        print('Starting game...\n')

        while True:

            self._print_menu()

            print('\t')

            choice = int(input('Select an option: '))
            print('\t')
            if choice == 1:
                user.take_card(self.deck.hit())
                print(f'User cards -> {user.cards}.\n')
                print(f'User points -> {user.calculate_points()}.')
                print('\t')
            elif choice == 2:
                return user.calculate_points()
            else:
                print('\t')
                print('Wrong choice. Choose option 1 or 2.')
                print('\t')

    def play(self):
        """
        Playing game and checking result.
        :return: None
        """
        try:
            user_points = self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error

        try:
            croupier_points = self._croupier_plays(user_points)
        except GameOverException as error:
            raise GameOverCroupierException from error
        print('\t')
        print('The croupier has won.')
