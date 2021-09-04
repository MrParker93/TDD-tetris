import pyxel
import random
import numpy as np
from tetrimino import TetriminoGenerator


class Board:
    WIDTH = 15
    HEIGHT = 23

    def __init__(self):
        self.board = np.zeros((Board.WIDTH * Board.HEIGHT)).reshape(Board.HEIGHT, Board.WIDTH)
        self.generate_block = TetriminoGenerator()
        self.block = self.generate_block.generate()
        self.next_block = self.generate_block.next_block.pop(0)
        
    def create_board(self):

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                pyxel.rect(6, 10, 116, 180, self.board[row][col])

    def draw_board(self):

        # Draw board where blocks will fall and stack
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                colour = 0 if 0 == self.board[row][col] else self.board[row][col]
                pyxel.rect(col * 8 + 4, row * 8 + 8, 8, 8, colour)

    def draw_next_block(self):
        for row in range(len(self.next_block)):
            for col in range(len(self.next_block)):
                colour = self.next_block[row][col]
                if colour != 0:
                    if colour == 6:
                        pyxel.rect((col * 8) + 180 * 0.80, 24 + (row * 8), 8, 8, colour)
                    elif colour == 5:
                        pyxel.rect((col * 8) + 180 * 0.815, 40 + (row * 8), 8, 8, colour)
                    elif colour == 1 or colour == 2 or colour == 9:
                        pyxel.rect((col * 8) + 180 * 0.77, 32 + (row * 8), 8, 8, colour)
                    else:
                        pyxel.rect((col * 8) + 180 * 0.79, 40 + (row * 8), 8, 8, colour)



