import enum
import random
import numpy as np
from enum import IntEnum
from copy import copy, deepcopy


class Orientation(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Tetrimino:
    MOVEMENT_SPEED = 4

    def __init__(self):
        self.block = [[]]
        self.position = [0, 0]  # The [x, y] coordinates of the block on the board
        self.w = 0  # The width of the block
        self.h = 0  # The height of the block
        self.colour = 0  # The colour of the block using Pyxel.COLOUR_
        self.rotation = 0  # The direction of rotation "-1" for anticlockwise, "1" for clockwise
        self.orientation = Orientation.RIGHT  # The direction the block is facing

    def get_width_and_height(self):
        copy_block = copy(self.block)
        copy_block = np.array(copy_block)

        self.w = copy_block.max(axis=0).tolist().count(
            self.colour)  # Gets the width of the current block
        self.h = copy_block.max(axis=1).tolist().count(
            self.colour)  # Gets the height of the current block

    def move_block_left(self):
        self.position = [self.position[0] - 1, self.position[1]]
        return self.position

    def move_block_right(self):
        self.position = [self.position[0] + 1, self.position[1]]
        return self.position

    def move_block_down(self):
        self.position = [self.position[0], self.position[1] + 1]
        return self.position

    def place_block(self):
        pass
        # return [self.position[0], ]

    def rotate_block(self, block):

        if self.rotation == 1:
            self.orientation += self.rotation % 4
            return np.rot90(block, self.rotation)

        elif self.rotation == -1:
            self.orientation += self.rotation % 4
            return np.rot90(block, self.rotation)


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
            [6],
            [6],
            [6],
            [6]
        ]

        self.colour = 6


class TetriminoZ(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [0, 8],
            [8, 8],
            [8, 0]
        ]

        self.colour = 8


class TetriminoS(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [10, 0],
            [10, 10],
            [0, 10]
        ]

        self.colour = 10


class TetriminoL(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [1, 0],
            [1, 0],
            [1, 1]
        ]

        self.colour = 1


class TetriminoJ(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [2, 2],
            [2, 0],
            [2, 0]
        ]

        self.colour = 2


class TetriminoT(Tetrimino):
    def __init__(self):
        super().__init__()
        self.block = [
            [9, 0],
            [9, 9],
            [9, 0]
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
        tetrimino = self.tetrimino[self.bag.pop()]()
        return tetrimino


# t = TetriminoT()
# i = TetriminoI()
# l = TetriminoL()
# o = TetriminoO()
# j = TetriminoJ()
# t = [
#     [0, 8],
#     [8, 8],
#     [8, 0]
# ]
# print(3 % 3 + 1)

# t = np.array(t)
# print(np.unique(t, axis=0, return_inverse=True,))
# w = t.max(axis=0).tolist().count(8)
# h = t.max(axis=1).tolist().count(8)
# t_90 = np.rot90(t, k=-1)
# print(3 % 4)
# print(np.rot90(t_90, k=-1), w, h)

# i = [
#     [6],
#     [6],
#     [6],
#     [6]
# ]

# for row in range(len(i)):
#     print(i[row])
#     for col in range(len(i[row])):
#         print(i[row][col])
