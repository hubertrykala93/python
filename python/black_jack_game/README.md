Python Project of Black Jack Card Game.

This project includes:
- card.py - initialization Card class,
- deck.py - initialization Deck class,
- game.py - initialization Game class,
- main.py - run project,
- player.py - initialization Player class,
- exceptions.py - exceptions for whole project,
- card_test.py - tests for card.py,
- deck_test.py - tests for deck.py,
- player_test.py - test for player.py.


Module card.py:

In this module class Card was created.

Class Card constructor has following attributes:

- self.color (Card color) as string,
- self.value (Card figure) as integer or string.

This class has variables like POSSIBLE_COLOR and POSSIBLE_VALUES:

- POSSIBLE_COLORS - a dictionary with name of colors in keys and unicode types for them in values,
- POSSIBLE_VALUES - list of card figures creating by range function (1 - 10) and as string (Jack, Queen, King, Ace).

In the __init__ method has been implemented validation, which inform a user that chose invalid card, otherwise attribute of Card class is created. Please note that this is a dictionary so it should be operated by keys and values. That same validation has been implemented in attribute value.

Class Card has following methods:

- def __repr__ - return the string representation of card. Method returns string.


Module deck.py:

In this module class Deck was created.

At the top of this file was imported random library and Card class.

Constructor of this class takes no attributes in __init__, only required self.

Class Deck has following attributes:

- self.cards as empty list.

Below was used nested for loop to generate all cards configurations. All of cards were added to empty list of cards.

Class Deck has following methods:

- def shuffle - shuffle cards in list of cards. Method returns None,
- def hit - discard the last card from list of cards. Method returns None.


Module player.py:

In this module class Player was created.

At the top of this file was imported Card class and GameOverException from exceptions.

Constructor of this class takes no attributes in __init__, only required self.

Class Player has following attributes:

- self.cards as empty list.

Class Deck has following methods:

- def take_card - takes a parameter card as Card class object and return None. User draws card which is added to empty card list.
- def calculate_points - method calculating users points and return them as integer. At the top of this method two variables was created.
  - points - calculate user points
  - number_of_aces - calculate aces in user hand.
  
  It method has also very important conditions:
  
  - if number of aces in user hand is equal to 2 and if user has only 2 cards, method returns 21 points,
  - if number of aces in user hand is equal to 1 and user has only 2 cards, method returns 10 points,
  - for loop iterating through all cards in user hand,
    - if card is equal to Ace, user gets 1 point,
    - if card is equal to Jack, Queen, King, user gets 10 points,
    - otherwise if value card is equal to (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) user gets equivalent to the value of the card.
  - if sum of all user cards is greater than 21, game raises GameOverException error imported from exceptions.py


Module game.py:

In this module class Game was created.

At the top of this file was imported Player and Deck classes and GameOverException, GameOverUserException, GameOverCroupierException from exceptions.py.

Constructor of this class takes no attributes in __init__, only required self.

Class Game has following attributes:

- self.deck is a class Deck.

Below deck is shuffled using def shuffle() method from Deck class.

Class Game has following methods:

- def print_menu - protected static method returns None - this method prints game menu.
- def croupier_plays - also protected method with user_points parameter as integer, returns croupier points as integer.
  In method body was created instance of Player class named croupier, while croupier points are less than user points croupier is taking card.
- def user_playes - also protected method returns integer or None. Creating Player class instance, adding cards to player hands and printing by while loop   private static method 'menu' while the game not is over.
- def play - playing game and checking results. Method returns None.


Module exceptions.py:

In this module were created five classes with exceptions for BlackJack Python Game.

- class InvalidColor - inherets from Exception class. This exception is raising when class Card will be initialized with wrong card color.
- class InvalidValue - inherets from Exception class. This exception is raising when class Card will be initialized with wrong card value.
- class GameOverException - inherets from Exception class. This exception is raising when the game is over.
- class GameOverUserException - inherets from Exception class. This exception is raising when user loss.
- class GameOverCroupierException - inherets from Exception class. This exception is raising when croupier loss.


Module main.py:

Main module for BlackJack Python Game. Play and check if you will with croupier! Enjoy!
