import pyxel
import random
import numpy as np
from gamelogic import GameLogic
from tetrimino import TetriminoGenerator


class Board:
    WIDTH = 15
    HEIGHT = 23

    def __init__(self):
        self.board = np.zeros((Board.WIDTH * Board.HEIGHT)
                              ).reshape(Board.HEIGHT, Board.WIDTH)
        self.l = GameLogic()
        self.gen = TetriminoGenerator()
        self.generate_block = self.gen.generate()
        self.block = self.generate_block.block
        self.generate_block.get_dimensions_and_position_x_of_block()
        self.block_x = self.generate_block.x
        self.block_y = self.generate_block.y
        self.next_block = self.gen.next_block.pop(0).block
        self.game_state = "running"
        self.is_gameover = False
        
    def update(self):

        if pyxel.btn(pyxel.KEY_P):
            if self.game_state == "running" and not self.is_gameover:
                self.game_state = "paused"
            else:
                self.game_state = "running"

        if self.game_state == "running":
            if pyxel.frame_count % self.l.fall_speed == 0:
                self.falling_block()

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                if not self.check_collisions():
                   self.block_x = self.generate_block.move_block_left(self.block)

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                if not self.check_collisions():
                    self.block_x = self.generate_block.move_block_right(self.block)

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                if not self.check_collisions():
                    self.block_y = self.generate_block.move_block_down(self.block)

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                if not self.check_collisions():
                    self.generate_block.rotation = 1
                    self.block = self.generate_block.rotate_block(self.block)
                    print(self.board)
            
            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                if not self.check_collisions():
                    self.generate_block.rotation = -1
                    self.block = self.generate_block.rotate_block(self.block)
                    print(self.board)

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
                if colour != 0:
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
