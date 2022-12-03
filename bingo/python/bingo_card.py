from random import sample

class card:
    """ Class for a bingo card"""
    
    def __init__(self):
        """
        Creates an empty bingo card
        """

        # The numbers on the card
        self.numbers = {
            "b" : sample(range(1 , 16), 5),
            "i" : sample(range(16, 31), 5),
            "n" : sample(range(31, 46), 5),
            "g" : sample(range(31, 46), 5),
            "o" : sample(range(61, 76), 5),
        }
        self.numbers["n"][2] = "Free"

        # The status of a square: marked or unmarked
        self.marks = {
            "b" : [False] * 5,
            "i" : [False] * 5,
            "n" : [False] * 5,
            "g" : [False] * 5,
            "o" : [False] * 5,
        }
        self.marks["n"][2] = True

        
    #TODO: Rotate this output 90 degrees
    def __str__(self):
        """
        Returns string representation of a bingo card
        """
        text = ""
        for column in self.numbers:
            for row in range(5):
                text = text + str(self.numbers[column][row]) + " "
            text += "\n"
        return text

    def get_square(self, column, row):
        """
        Returns the number (or "Free") in a given square
        """
        return self.numbers[column][row]
    
    def set_square(self, column, row, value):
        """
        Sets the number in a specific square
        Used for testing, or if a player wants to choose their own numbers
        Can be used to override the "Free" square
        """
        self.numbers[column][row] = value

    def is_marked(self, column, row):
        """
        Returns true if square has been marked/called
        The "Free" square is marked by default on card creation
        """
        return self.marks[column][row]
    
    def mark(self, column, row):
        """
        Marks that a square has been called
        """
        self.marks[column][row] = True

    def call(self, column, number):
        """
        Similar to mark(), marks a square if it has been called
        However, this only makes a mark if the called number is on the card
        """
        if number in self.numbers[column]:
            row = self.numbers[column].index(number)
            self.mark(column, row)

    def has_won(self):
        """
        Checks to see if the card has a winning arrangement of marks
        """
        # Check Columns