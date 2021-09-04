import random
import numpy as np
from enum import IntEnum


class Orientation(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Tetrimino:
    def __init__(self):
        self.block = [[]]
        self.x = 0  # Position x of the block
        self.y = 0  # Position y of the block
        self.w = 0  # The width of the block
        self.h = 0  # The height of the block
        self.colour = 0  # The colour of the block using Pyxel.COLOUR_
        self.rotation = 0  # The direction of rotation "-1" for anticlockwise, "1" for clockwise
        self.orientation = Orientation.RIGHT  # The direction the block is facing

    def move_block_left(self, block):
        pass

    def move_block_right(self, block):
        pass

    def move_block_down(self, block):
        pass

    def rotate_block(self, block):

        pass


class TetriminoO(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [5, 5],
            [5, 5]
        ]

        self.colour = 5


class TetriminoI(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [0, 6, 0, 0],
            [0, 6, 0, 0],
            [0, 6, 0, 0],
            [0, 6, 0, 0]
        ]

        self.colour = 6


class TetriminoZ(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [8, 8, 0],
            [0, 8, 8],
            [0, 0, 0]
        ]

        self.colour = 8


class TetriminoS(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [0, 10, 10],
            [10, 10, 0],
            [0, 0, 0]
        ]

        self.colour = 10


class TetriminoL(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1]
        ]

        self.colour = 1


class TetriminoJ(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [0, 2, 2],
            [0, 2, 0],
            [0, 2, 0]
        ]

        self.colour = 2


class TetriminoT(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [0, 9, 0],
            [0, 9, 9],
            [0, 9, 0]
        ]

        self.colour = 9


class TetriminoGenerator:
    def __init__(self):
        self.get_block = TetriminoOptions()
        self.next_block = []
        for max_number_of_blocks in range(4):
            self.next_block.append(self.get_block.generate())

    def generate(self):
        current_block = self.next_block.pop(0)
        self.next_block.append(self.get_block.generate())
        return current_block


class TetriminoOptions:
    def __init__(self):
        self.tetrimino = (TetriminoO, TetriminoI, TetriminoZ,
                          TetriminoS, TetriminoL, TetriminoJ, TetriminoT)
        self.bag = random.sample(
            list(range(len(self.tetrimino))), len(self.tetrimino))

    def generate(self):
        tetrimino = self.tetrimino[self.bag.pop()]().block
        return tetrimino


# t = TetriminoO()
# o = np.array(t.block)

# for i in range(len(o)):
#     if 0 == o[i]:
#         continue
#     x = i % 4
#     y = i // 4
#     print(f"x is: {x} and y is: {y}")

# print(o)
