from deck import Deck


def test_creation():
    deck = Deck()
    assert len(deck.cards) == 52


def test_deck():
    deck = Deck()
    cards = [(card.value, card.color) for card in deck.cards]
    for color in ['\u2661', '\u2664', '\u2662', '\u2667']:
        cards_in_color = [card for card in cards if card[1] == color]
        assert len(cards_in_color) == 13


def test_deck_shuffle():
    deck_1 = Deck()
    cards_1 = deck_1.cards
    deck_2 = Deck()
    deck_2.shuffle()
    cards_2 = deck_2.cards
    assert deck_1 != deck_2


def test_deck_hit():
    deck = Deck()
    last_card = deck.cards[-1]
    hitted_card = deck.hit()
    assert hitted_card == last_card
    assert len(deck.cards) == 51
    assert hitted_card not in deck.cards
