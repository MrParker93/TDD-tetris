import constants
from block import Block
from rotate import Rotate
from random import randint


class Tetromino(Rotate, Block):
    O_MINO = {
        "block": [[1, 1],
                  [1, 1]],
        "rotations": 1,
        "width": 2,
        "height": 2
        }
    
    S_MINO = {
        "block": [[0, 2, 2],
                  [2, 2, 0],
                  [0, 0, 0]],
        "rotations": 2,
        "width": 3,
        "height": 2
        }

    Z_MINO = {
        "block": [[3, 3, 0],
                  [0, 3, 3],
                  [0, 0, 0]],
        "rotations": 2,
        "width": 3,
        "height": 2
        }

    J_MINO = {
        "block": [[0, 4, 0],
                  [0, 4, 0],
                  [4, 4, 0]],
        "rotations": 4,
        "width": 2,
        "height": 3
        }

    L_MINO = {
        "block": [[0, 5, 0],
                  [0, 5, 0],
                  [0, 5, 5]],
        "rotations": 4,
        "width": 2,
        "height": 3
        }

    T_MINO = {
        "block": [[0, 6, 0],
                  [6, 6, 6],
                  [0, 0, 0]],
        "rotations": 4,
        "width": 3,
        "height": 2
        }

    I_MINO = {
        "block" : [[0, 0, 0, 0],
                   [7, 7, 7, 7],
                   [0, 0, 0, 0]],
        "rotations": 2,
        "width": 4,
        "height": 1
        }
    
    def __init__(self, generator):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.mino = self.tetrominos[generator]
        self.block = self.mino["block"]
        self.rotations = self.mino["rotations"]
        self.x = constants.BOARDWIDTH // 2 - self.width() // 2
        self.y = 0
        self.width = self.width()
        self.height = self.height()
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
        self.width, self.height = self.height, self.width
        return self.orientations[self.current_orientation % self.rotations]
    
    def rotate_left(self):
        self.current_orientation -= 1
        self.width, self.height = self.height, self.width
        return self.orientations[self.current_orientation % self.rotations]

    def width(self):
        return self.mino["width"]

    def height(self):
        return self.mino["height"]

    def get_wallkicks(self, generator): 
        if generator != 6:
            wallkicks = [
                
            ]