from grid import Grid
from piece import Piece
from rotatable import Rotatable
from coordinates import Coordinates


class MovableMino(Rotatable, Grid):
    def __init__(self, mino):
        self.pos = Coordinates(0, 0)
        self.mino = mino

    def movable_mino(self, pos, mino):
        
    def rows(self):
        return self.mino.rows()

    def cols(self):
        return self.mino.cols()

    def block_position(self, row, col):
        return self.mino.block_position(row, col)

    def move_block(self, pos):
        return MovableMino(pos, self.mino)

    def move_down(self):
        return MovableMino(Coordinates(self.pos.row + 1, self.pos.col), self.mino)
    
    # def movable_mino(self, coord, mino):
    #     self.__init__(coord, mino)

    # def invalid_position(self, block):
    #     return block.row >= self.board_length() or \
    #             block.col < 0 or \
    #                 block.col >= self.board_width()
