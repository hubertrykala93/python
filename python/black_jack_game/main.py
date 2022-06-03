"""Main module for BlackJack Python Game."""

from game import Game
from exceptions import GameOverCroupierException, GameOverUserException

if __name__ == '__main__':
    try:
        game = Game()
        game.play()
    except GameOverCroupierException:
        print('The player has won.')
    except GameOverUserException:
        print('The croupier has won.')
