import pyxel
import random
import numpy as np
from copy import deepcopy
from gamelogic import GameLogic
from tetrimino import TetriminoGenerator


class Board:
    WIDTH = 16
    HEIGHT = 24

    def __init__(self):
        self.board = [[0] * Board.WIDTH for _ in range(Board.HEIGHT)]
        self.board_copy = deepcopy(self.board)
        self.l = GameLogic()
        self.gen = TetriminoGenerator()
        self.generate_block = self.gen.generate()
        self.block = self.generate_block.block
        self.generate_block.get_width_and_height()
        self.position = self.generate_block.position
        self.block_w = self.generate_block.w
        self.block_h = self.generate_block.h
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
            if pyxel.frame_count % self.l.fall_speed == 2:
                if self.any_collisions(self.position[0], self.position[1]):
                    self.falling_block()

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                new_position = self.generate_block.move_block_left()
                if self.any_collisions(new_position[0], new_position[1]):
                    self.position = new_position

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                new_position = self.generate_block.move_block_right()
                if self.any_collisions(new_position[0], new_position[1]):
                    self.position = new_position

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                new_position = self.generate_block.move_block_down()
                if self.any_collisions(new_position[0], new_position[1]):
                    self.position = new_position

            if pyxel.btn(pyxel.KEY_SPACE):
                if not self.any_collisions():
                    self.position = self.generate_block.place_block()

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.generate_block.rotation = 1
                new_block = self.generate_block.rotate_block(self.block)
                if self.any_collisions(self.position[0], self.position[1]) and self.block[0][0] != 5:
                    self.block = new_block

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.generate_block.rotation = -1
                new_block = self.generate_block.rotate_block(self.block)
                if self.any_collisions(self.position[0], self.position[1]) and self.block[0][0] != 5:
                    self.block = new_block

    def draw_board(self):

        # Draw board where blocks will fall and stack
        for row in range(len(self.board_copy)):
            for col in range(len(self.board_copy[row])):
                if self.board_copy[row][col] != 0:
                    pyxel.rect(col * 8 + 4, row * 8 + 8, 8, 8, self.board_copy[row][col])

    def stack_block(self):
        # for row in range(len())
        pass

    def draw_block(self):

        for row in range(len(self.block)):
            for col in range(len(self.block[row])):
                colour = self.block[row][col]
                x = self.position[0]
                y = self.position[1]
                self.board_copy[row + y][col + x] = colour

                # pyxel.rect(col * 8, row * 8, 8, 8, colour)
                # if colour != 0:
                #     x = self.block_x + self.block_w
                #     y = self.block_y + self.block_h
                #     if colour == 6:
                #         pyxel.rect((col * 8) + (x + 5), (y + 6) +
                #                 (row * 8), 8, 8, colour)
                #     elif colour == 5:
                #         pyxel.rect((col * 8) + (x + 4), (y + 8) +
                #                 (row * 8), 8, 8, colour)
                #     else:
                #         pyxel.rect((col * 8) + (x + 4), (y + 7) +
                #                 (row * 8), 8, 8, colour)

    def falling_block(self):
        if self.any_collisions(self.position[0], self.position[1]):
            pass

    def draw_next_block(self):
        for row in range(len(self.next_block)):
            for col in range(len(self.next_block[row])):
                colour = self.next_block[row][col]
                if colour != 0:
                    if colour == 6:
                        pyxel.rect((col * 8) + 180 * 0.83,
                                   24 + (row * 8), 8, 8, colour)
                    elif colour == 5:
                        pyxel.rect((col * 8) + 180 * 0.815,
                                   40 + (row * 8), 8, 8, colour)
                    elif colour == 1 or colour == 2 or colour == 9:
                        pyxel.rect((col * 8) + 180 * 0.815,
                                   32 + (row * 8), 8, 8, colour)
                    else:
                        pyxel.rect((col * 8) + 180 * 0.815,
                                   32 + (row * 8), 8, 8, colour)

    def any_collisions(self, x, y):
        x = self.position[0]
        y = self.position[1]
        return y < Board.HEIGHT and 0 <= x < Board.WIDTH


b = Board()
print(b.block)
# for row in range(len(b.block)):
#     print(b.block[row])
#     for col in range(len(b.block)):
#         print(b.block[row][col])
