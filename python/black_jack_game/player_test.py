from player import Player
from card import Card


def test_calculate_player_points():
    card_1 = Card('spades', 2)
    card_2 = Card('hearts', 5)
    player = Player()
    player.cards.append(card_1)
    player.cards.append(card_2)
    assert player.calculate_points() == 7


def test_calculate_player_points_two_aces():
    card_1 = Card('spades', 'Ace')
    card_2 = Card('hearts', 'Ace')
    player = Player()
    player.cards.append(card_1)
    player.cards.append(card_2)
    assert player.calculate_points() == 21


def test_calculate_player_points_one_ace():
    card_1 = Card('spades', 'Ace')
    card_2 = Card('hearts', 2)
    player = Player()
    player.cards.append(card_1)
    player.cards.append(card_2)
    assert player.calculate_points() == 13


def test_calculate_player_points_three_cards():
    card_1 = Card('spades', 'Ace')
    card_2 = Card('hearts', 'Ace')
    card_3 = Card('diamonds', 'Ace')
    player = Player()
    player.cards.append(card_1)
    player.cards.append(card_2)
    player.cards.append(card_3)
    assert player.calculate_points() == 3
