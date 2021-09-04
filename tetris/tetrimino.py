import random
from enum import IntEnum


class Orientation(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Tetrimino:
    def __init__(self):
        self.block = [0, 0, 0, 0,  # The 4x4 grid for all blocks
                      0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0]
        self.x = 0  # Position x of the block
        self.y = 0  # Position y of the block
        self.w = 0  # The width of the block
        self.h = 0  # The height of the block
        self.colour = 0  # The colour of the block using Pyxel.COLOUR_
        self.orientation = Orientation.RIGHT  # The direction the block is facing

    def move_block_left(self, block):
        pass

    def move_block_right(self, block):
        pass

    def move_block_down(self, block):
        pass

    def rotate_block(self, block, orientation):
        pass


class TetriminoO(Tetrimino):
    def __init__(self):
        super().__init__()
        self.blocks = [5, 5, 0, 0,
                       5, 5, 0, 0,
                       0, 0, 0, 0,
                       0, 0, 0, 0]

        self.colour = 5


class TetriminoI(Tetrimino):
    def __init__(self):
        super().__init__()
        self.blocks = [6, 0, 0, 0,
                       6, 0, 0, 0,
                       6, 0, 0, 0,
                       6, 0, 0, 0]

        self.colour = 6


class TetriminoZ(Tetrimino):
    def __init__(self):
        super().__init__()
        self.blocks = [0, 8, 0, 0,
                       8, 8, 0, 0,
                       8, 0, 0, 0,
                       0, 0, 0, 0]

        self.colour = 8


class TetriminoS(Tetrimino):
    def __init__(self):
        super().__init__()
        self.blocks = [10, 0, 0, 0,
                       10, 10, 0, 0,
                       0, 10, 0, 0,
                       0, 0, 0, 0]

        self.colour = 10


class TetriminoL(Tetrimino):
    def __init__(self):
        super().__init__()
        self.blocks = [1, 0, 0, 0,
                       1, 0, 0, 0,
                       1, 1, 0, 0,
                       0, 0, 0, 0]

        self.colour = 1


class TetriminoJ(Tetrimino):
    def __init__(self):
        super().__init__()
        self.blocks = [2, 2, 0, 0,
                       2, 0, 0, 0,
                       2, 0, 0, 0,
                       0, 0, 0, 0]

        self.colour = 2


class TetriminoT(Tetrimino):
    def __init__(self):
        super().__init__()
        self.blocks = [9, 0, 0, 0,
                       9, 9, 0, 0,
                       9, 0, 0, 0,
                       0, 0, 0, 0]

        self.colour = 9


class TetriminoGenerator:
    def __init__(self):
        self.options = (TetriminoO, TetriminoI, TetriminoZ,
                        TetriminoS, TetriminoL, TetriminoJ, TetriminoT)
        self.bag = random.sample(
            list(range(len(self.options))), len(self.options)).pop()
        self.block = self.options[self.bag]()
        self.next_block = []


tetra = TetriminoGenerator()
print(tetra.block)
