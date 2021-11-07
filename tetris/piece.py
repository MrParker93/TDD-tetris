from grid import Grid
from rotatable import Rotatable

class Piece(Grid, Rotatable):
    def __init__(self, block):
        self.block = block

    def rotate_right(self):
        return Piece(self.rotate(self.block))
    
    def rotate_left(self):
        return self.rotate_right().rotate_right().rotate_right()

    def rotate(self, block):
        return list(map(list, zip(*block[::-1])))

    def rows(self):
        return len(self.block)

    def cols(self):
        return len(self.block[0])

    def block_position(self, row, col):
        return self.block[row][col]