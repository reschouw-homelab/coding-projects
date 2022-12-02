class card:
    """ Class for a BINGO card"""

    def __init__(self):
        """ Creates an empty bingo card """
        self.grid = [[None for x in range(5)] for y in range(5)]

    #def __str__(self):
    #    return self.grid.