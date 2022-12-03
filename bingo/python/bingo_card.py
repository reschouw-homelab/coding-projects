from random import sample

class card:
    """ Class for a bingo card"""
    
    def __init__(self):
        """ Creates an empty bingo card """
        self.grid = {
            "b" : sample(range(1 , 16), 5),
            "i" : sample(range(16, 31), 5),
            "n" : sample(range(31, 46), 5),
            "g" : sample(range(31, 46), 5),
            "o" : sample(range(61, 76), 5),
        }
        self.grid["n"][2] = "Free"
        

    def __str__(self):
        text = ""
        for column in self.grid:
            for row in range(5):
                text = text + str(self.grid[column][row]) + " "
            text += "\n"
        return text

    def get_square(self, column, row):
        return self.grid[column][row]