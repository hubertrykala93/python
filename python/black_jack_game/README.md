Python Project of Black Jack Card Game.

The project includes:
- card.py - initialization Card class,
- deck.py - initialization Deck class,
- game.py - initialization Game class,
- main.py - run project,
- player.py - initialization Player class,
- exceptions.py - exceptions for whole project,
- card_test.py - tests for card.py,
- deck_test.py - tests for deck.py,
- player_test.py - test for player.py.

Card Class:

Class with Card constructor with following attributes:

- color (Card color) as string,
- value (Card figure) as integer or string.

This class has variables like POSSIBLE_COLOR and POSSIBLE_VALUES:

- POSSIBLE_COLORS - a dictionary with name of colors in keys and unicode types for them in values,
- POSSIBLE_VALUES - list of card figures creating by array (1 - 10) and as string (Jack, Queen, King, Ace).

In the __init__ method has been implemented validation, which inform a user that chose invalid card, otherwise attribute of Card class is created. Please note that this is a dictionary so it should be operated by keys and values. That same validation has been implemented in attribute value.

Card Class has following methods:

- def __repr__ - return the string representation of card.
