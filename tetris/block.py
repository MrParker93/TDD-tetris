import pyxel

class Block:
    def __init__(self, row, col, block=None):
        self.row = row
        self.col = col
        self.block = block

    def move_block(self, row, col):
        return Block(row, col, self.block)

    def move_block_down(self):
        return Block(self.row + 1, self.col, self.block)

    def block_position(self, row, col):
        return row == self.row and col == self.col 