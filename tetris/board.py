import pyxel
import random
import numpy as np
from tetrimino import TetriminoGenerator


class Board:
    WIDTH = 15
    HEIGHT = 23

    def __init__(self):
        self.board = np.zeros((Board.WIDTH * Board.HEIGHT)
                              ).reshape(Board.HEIGHT, Board.WIDTH)
        self.gen = TetriminoGenerator()
        self.generate_block = self.gen.generate()
        self.block = self.generate_block.block
        self.generate_block.get_dimensions_and_position_x_of_block()
        self.block_x = self.generate_block.x
        self.block_y = self.generate_block.y
        self.next_block = self.gen.next_block.pop(0).block

    def draw_board(self):

        # Draw board where blocks will fall and stack
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                colour = 0 if 0 == self.board[row][col] else self.board[row][col]
                pyxel.rect(col * 8 + 4, row * 8 + 8, 8, 8, colour)

    def draw_block(self):
        for row in range(len(self.block)):
            for col in range(len(self.block)):
                colour = self.block[row][col]
                x = self.block_x
                y = self.block_y
                self.board[row + y][col + x] = colour

    def falling_block(self):
        pass
    
    def draw_next_block(self):
        for row in range(len(self.next_block)):
            for col in range(len(self.next_block)):
                colour = self.next_block[row][col]
                if colour != 0:
                    if colour == 6:
                        pyxel.rect((col * 8) + 180 * 0.80,
                                   24 + (row * 8), 8, 8, colour)
                    elif colour == 5:
                        pyxel.rect((col * 8) + 180 * 0.815,
                                   40 + (row * 8), 8, 8, colour)
                    elif colour == 1 or colour == 2 or colour == 9:
                        pyxel.rect((col * 8) + 180 * 0.77,
                                   32 + (row * 8), 8, 8, colour)
                    else:
                        pyxel.rect((col * 8) + 180 * 0.79,
                                   40 + (row * 8), 8, 8, colour)

    def check_collisions(self):
        return False
