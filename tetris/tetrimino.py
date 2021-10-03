import random

class Tetrimino:

    def __init__(self):
        self.block = []
        self.size = []
        self.x = 4
        self.y = 0
        self.colour = 0  # The colour of the block using Pyxel.COLOUR_
        self.rotation = 0  # The direction of rotation "1" for anticlockwise, "-1" for clockwise

    def block_size(self, block):
        return [len(block), len(block[0])]

    def move_block_left(self):
        self.x -= 1
        return self.x

    def move_block_right(self):
        self.x += 1
        return self.x

    def move_block_down(self):
        self.y += 1
        return self.y

    def place_block(self):
        pass

    def rotate_block(self, block):

        if self.rotation == 1:
            new_block = list(map(list, zip(*block[::-1])))
            rotate_new_block = list(map(list, zip(*new_block[::-1])))
            return list(map(list, zip(*rotate_new_block[::-1])))

        elif self.rotation == -1:
            new_block = list(map(list, zip(*block[::-1])))
            return new_block


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
        for _ in range(4):
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

