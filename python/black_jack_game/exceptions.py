"""Exceptions module for BlackJack game."""


class InvalidColor(Exception):
    """Exception when color is invalid."""


class InvalidValue(Exception):
    """Exception when value is invalid."""


class GameOverException(Exception):
    """Exception when game ends."""


class GameOverUserException(Exception):
    """Exception when user loss"""


class GameOverCroupierException(Exception):
    """Exception when croupier loss"""
