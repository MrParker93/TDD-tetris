from typing import Final

class Coordinates:
    """Sets the coordinates"""
    ROW: Final = int()
    COL: Final = int()
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
