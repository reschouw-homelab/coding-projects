import card as _card
import pytest

def test_create_card():
    card = _card.card()
    

def test_get_card():
    board = _card.card()
    empty_state = [[False for x in range(10)] for y in range(10)]
    assert(board.get() == empty_state)
