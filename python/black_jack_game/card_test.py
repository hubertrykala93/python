from card import Card, InvalidValue, InvalidColor
import pytest


def test_creation():
    card = Card('hearts', 'Ace')
    assert card.color == '♡'
    assert card.value == 'Ace'


def test_creation_wrong_value():
    with pytest.raises(expected_exception=InvalidValue) as message:
        card = Card('hearts', 'A')
        assert message == 'Invalid card value!'


def test_creation_wrong_color():
    with pytest.raises(expected_exception=InvalidColor) as message:
        card = Card('abc', 'A')
        assert message == 'Invalid card color!'


def test_card_represenation():
    card = Card('hearts', 'Ace')
    assert repr(card) == 'Ace -> ♡'
