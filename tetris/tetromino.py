from random import randint
from block import Block
from rotate import Rotate


class Tetromino(Rotate, Block):
    O_MINO = {
        "block": [[1, 1, 0],
                  [1, 1, 0],
                  [0, 0, 0]],
        "rotations": 1
        }
    
    S_MINO = {
        "block": [[0, 2, 2],
                  [2, 2, 0],
                  [0, 0, 0]],
        "rotations": 2
        }

    Z_MINO = {
        "block": [[3, 3, 0],
                  [0, 3, 3],
                  [0, 0, 0]],
        "rotations": 2
        }

    J_MINO = {
        "block": [[0, 4, 0],
                  [0, 4, 0],
                  [4, 4, 0]],
        "rotations": 4
        }

    L_MINO = {
        "block": [[0, 5, 0],
                  [0, 5, 0],
                  [0, 5, 5]],
        "rotations": 4
        }

    T_MINO = {
        "block": [[0, 6, 0],
                  [6, 6, 6],
                  [0, 0, 0]],
        "rotations": 4
        }

    I_MINO = {
        "block" : [[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [7, 7, 7, 7, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]],
        "rotations": 2
        }
    
    def __init__(self, generator):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.mino = self.tetrominos[generator]
        self.block = self.mino["block"]
        self.rotations = self.mino["rotations"]
        self.current_orientation = 0
        self.orientations = self.get_orientations()
        
    def get_orientations(self):
        orientation = [
            self.block,
            Rotate(self.block).rotate_right(),
            Rotate(self.block).rotate().rotate_right(),
            Rotate(self.block).rotate().rotate().rotate_right()
        ]
        return orientation[:self.rotations]

    def rotate_right(self):
        self.current_orientation += 1
        return self.orientations[self.current_orientation % self.rotations]
    
    def rotate_left(self):
        self.current_orientation -= 1
        return self.orientations[self.current_orientation % self.rotations]

    def width(self):
        return super().width()

    def height(self):
        return super().height()
