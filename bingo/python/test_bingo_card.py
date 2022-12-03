import bingo_card 
import pytest

# Create a bingo card
def test_create_card():
    card = bingo_card.card()

# Print a bingo Card
def test_print_card():
    card = bingo_card.card()
    print(card)

# Get the value of a square on the card, and make sure the free square exists
def test_get_square():
    card = bingo_card.card()
    assert(type(card.get_square("b", 3)) == type(5))  
    assert(card.get_square("n", 2) == "Free")

# Check that the values of all the squares are valid and follow rules
def test_check_squares_are_valid():
    rules = {
        "b" : range(1 , 16),
        "i" : range(16, 31),
        "n" : range(31, 46),
        "g" : range(31, 46),
        "o" : range(61, 76),
    }
    card = bingo_card.card()
    for column in ["b","i","n","g","o",]:
        for row in range(5):
            square = card.get_square(column, row)
            if square == "Free":
                continue
            assert(square in rules[column])
            

    
#test
#def test_get_card():
#    board = bingo_card.card()
#    empty_state = [[False for x in range(10)] for y in range(10)]
#    assert(board.get() == empty_state)
