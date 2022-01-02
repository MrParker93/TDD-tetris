import constants
from block import Block
from rotate import Rotate
from random import randint


class Tetromino(Rotate, Block):

    O_MINO = {
        "block": [[5, 5],
                  [5, 5]],
        "rotations": 1,
        "width": 2,
        "height": 2,
        "x": (constants.BOARDWIDTH // 2 - 2 // 2),
        "y": 0
        }
    
    S_MINO = {
        "block": [[0, 4, 4],
                  [4, 4, 0],
                  [0, 0, 0]],
        "rotations": 2,
        "width": 3,
        "height": 2,
        "x": (constants.BOARDWIDTH // 2 - 3 // 2) - 1,
        "y": 0
        }

    Z_MINO = {
        "block": [[14, 14, 0],
                  [0, 14, 14],
                  [0, 0, 0]],
        "rotations": 2,
        "width": 3,
        "height": 2,
        "x": (constants.BOARDWIDTH // 2 - 3 // 2) - 1,
        "y": 0
        }

    J_MINO = {
        "block": [[0, 0, 0],
                  [8, 8, 8],
                  [0, 0, 8]],
        "rotations": 4,
        "width": 2,
        "height": 3,
        "x": (constants.BOARDWIDTH // 2 - 3 // 2) - 1,
        "y": -1
        }

    L_MINO = {
        "block": [[0, 0, 0],
                  [10, 10, 10],
                  [10, 0, 0]],
        "rotations": 4,
        "width": 2,
        "height": 3,
        "x": (constants.BOARDWIDTH // 2 - 3 // 2) - 1,
        "y": -1
        }

    T_MINO = {
        "block": [[0, 0, 0],
                  [9, 9, 9],
                  [0, 9, 0]],
        "rotations": 4,
        "width": 3,
        "height": 2,
        "x": (constants.BOARDWIDTH // 2 - 3 // 2) - 1,
        "y": -1
        }

    I_MINO = {
        "block" : [[0, 0, 0, 0],
                   [12, 12, 12, 12],
                   [0, 0, 0, 0]],
        "rotations": 2,
        "width": 4,
        "height": 1,
        "x": (constants.BOARDWIDTH // 2 - 4 // 2),
        "y": -1
        }
    
    def __init__(self, generator):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.mino = self.tetrominos[generator]
        self.block = self.mino["block"]
        self.rotations = self.mino["rotations"]
        self.wallkicks = self.get_wallkicks(generator)
        self.x = self.mino["x"]
        self.y = self.mino["y"]
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
        return self.orientations[self.current_orientation % self.rotations]
    
    def rotate_left(self):
        self.current_orientation -= 1
        return self.orientations[self.current_orientation % self.rotations]

    def width(self):
        return self.mino["width"]

    def height(self):
        return self.mino["height"]

    def get_wallkicks(self, generator): 
        if generator != 6:
            wallkicks = [
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 0 orientation: 0
                [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],  # 0 -> R  orientation: 1
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 2 orientation: 2
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],  # 2 -> L orientation: 3
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 0 orientation: 0
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],  # 0 -> L orientation: -1
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 2 orientation: -2
                [(0, 0), (-1, 0), (-1, 1), (0, 2), (-1, 2)]  # 2 -> R orientation: -3
            ]
        else:
            wallkicks = [
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],  # L -> 0 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # 0 -> R 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],  # R -> 2 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # 2 -> L 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # R -> 0 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],  # 0 -> L 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # L -> 2 
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)]  # 2 -> R 
            ]
        return wallkicks


t = Tetromino(6)
a = Tetromino(6)

print(t == a)