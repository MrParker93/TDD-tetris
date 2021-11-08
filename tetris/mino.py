import pyxel
from grid import Grid
from piece import Piece
from rotatable import Rotatable
from coordinates import Coordinates

class Mino(Rotatable, Grid):
    def __init__(self, max_rotations, current_rotation, block):
        self.block = block
        self.first_rotation = self.first_rotation(Piece(block), current_rotation)
        self.rotations = self.all_rotations(self.first_rotation, max_rotations) 
        self.current_rotation = current_rotation
    
    def first_rotation(self, block, current_rotation):
        for _ in range(current_rotation):
            block = block.rotate_left()
        return block

    def all_rotations(self, first_rotation, max_rotations):
        rotations = [0] * max_rotations
        rotations[0] = first_rotation
        for i in range(1, len(rotations)):
            rotations[i] = rotations[i - 1].rotate_right()
        return rotations

    def tetromino(self, rotations, current_rotation):
        if current_rotation < 0:
            current_rotation += len(rotations)
        self.rotations = rotations
        self.current_rotation = current_rotation % len(rotations)

    def rotate_right(self):
        return self.tetromino(self.rotations, self.current_rotation + 1)

    def rotate_left(self):
        return self.tetromino(self.rotations, self.current_rotation - 1)

    def rows(self):
        return self.new_block().rows()

    def cols(self):
         return self.new_block().cols()

    def block_position(self, row, col):
        return self.new_block().block_position(Coordinates(row, col))  

    def new_block(self):
        return self.rotations[self.current_rotation]

    
class MinoO(Mino):
    def __init__(self):
        super().__init__(1, 0, 
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]])

class MinoS(Mino):
    def __init__(self):
        super().__init__(2, 0, 
        [[0, 1, 1],
         [1, 1, 0],
         [0, 0, 0]])

class MinoZ(Mino):
    def __init__(self):
        super().__init__(2, 0, 
        [[1, 1, 0],
         [0, 1, 1],
         [0, 0, 0]])

class MinoJ(Mino):
    def __init__(self):
        super().__init__(4, 0, 
        [[0, 1, 0],
         [0, 1, 0],
         [1, 1, 0]])

class MinoL(Mino):
    def __init__(self):
        super().__init__(4, 0, 
        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 1]])

class MinoT(Mino):
    def __init__(self):
        super().__init__(4, 0, 
        [[0, 1, 0],
         [1, 1, 1],
         [0, 0, 0]])

class MinoI(Mino):
    def __init__(self):
        super().__init__(2, 1, 
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]])

