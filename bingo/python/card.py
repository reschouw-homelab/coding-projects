class card:
    """ Class for a bingo card"""

    def __init__(self):
        """ Creates an empty bingo card """
        self.grid = {
            "b" = [None for x in range(5)],
            "i" = [None for x in range(5)],
            "n" = [None for x in range(5)],
            "g" = [None for x in range(5)],
            "o" = [None for x in range(5)]
        }

    #def __str__(self):
    #    return self.grid.