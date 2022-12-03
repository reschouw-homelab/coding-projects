import bingo_card 
import pytest

# Create a bingo card
def test_create_card():
    card = bingo_card.card()

# Print a bingo Card
def test_print_card():
    card = bingo_card.card()
    assert(type(str(card)) == type("I am a string"))
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
    assert(card.get_square("n", 2) == "Free")

# Set the value of a square and check it
def test_set_square_number():
    card = bingo_card.card()
    card.set_square("o", 0, 65)
    assert(card.get_square("o", 0) == 65)
    card.set_square("n", 2, 40)
    assert(card.get_square("n", 2) == 40)
    card.set_square("b", 4, 15)
    assert(card.get_square("b", 4) == 15)

# Make sure that the "Free" square is marked by default
def test_free_marked():
    card = bingo_card.card()
    assert(card.is_marked("n", 2))

# Make sure that the "Free square is marked by default"
def test_marking():
    card = bingo_card.card()
    assert(not card.is_marked("o", 4))
    card.mark("o", 4)
    assert(card.is_marked("o", 4))

# Mark that a number has been called
def test_number_called():
    card = bingo_card.card()
    square_number = card.get_square("b", 3)
    assert(not card.is_marked("b", 3))
    card.call("b", square_number)
    assert(card.is_marked("b", 3))