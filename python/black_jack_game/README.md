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


Class Card:

Class Card constructor has following attributes:

- self.color (Card color) as string,
- self.value (Card figure) as integer or string.

This class has variables like POSSIBLE_COLOR and POSSIBLE_VALUES:

- POSSIBLE_COLORS - a dictionary with name of colors in keys and unicode types for them in values,
- POSSIBLE_VALUES - list of card figures creating by range function (1 - 10) and as string (Jack, Queen, King, Ace).

In the __init__ method has been implemented validation, which inform a user that chose invalid card, otherwise attribute of Card class is created. Please note that this is a dictionary so it should be operated by keys and values. That same validation has been implemented in attribute value.

Class Card has following methods:

- def __repr__ - return the string representation of card.


Class Deck:

At the top of this file was imported random library and Card class.

Constructor of this class takes no attributes in __init__, only required self.

Class Deck has following attributes:

- self.cards as empty list.

Below was used nested for loop to generate all cards configurations. All of cards were added to empty list of cards.

Class Deck has following methods:

- def shuffle - shuffle cards in list of cards.
- def hit - discard the last card from list of cards.


Class Player:

At the top of this file was imported Card class and GameOverException from exceptions.

Constructor of this class takes no attributes in __init__, only required self.

Class Player has following attributes:

- self.cards as empty list.

Class Deck has following methods:

- def take_card - with parameter card as Card class. User draws card which is added to empty card list.
- def calculate_points - method calculating users points. At the top of this method two variables was created.
  - points - calculate user points
  - number_of_aces - calculate aces in user hand.
  
  It method has also very important conditions:
  
  - if number of aces in user hand is equal to 2 and if user has only 2 cards, method returns 21 points,
  - if number of aces in user hand is equal to 1 and user has only 2 cards, method returns 10 points,
  

