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
        self.generate_block.get_width_and_height()
        self.block_x = self.generate_block.x
        self.block_y = self.generate_block.y
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
                if not self.any_collisions():
                    self.falling_block()

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                if not self.any_collisions():
                    self.block_x = self.generate_block.move_block_left()

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                if not self.any_collisions():
                    self.block_x = self.generate_block.move_block_right()

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                if not self.any_collisions():
                    self.block_y = self.generate_block.move_block_down()

            if pyxel.btnp(pyxel.KEY_SPACE, 10, 2):
                if not self.any_collisions():
                    self.block_y = self.generate_block.place_block()

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                if not self.any_collisions():
                    self.generate_block.rotation = 1
                    self.block = self.generate_block.rotate_block(self.block)[0]
                    self.block_w = self.generate_block.rotate_block(self.block)[1]
                    self.block_h = self.generate_block.rotate_block(self.block)[2]

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                if not self.any_collisions():
                    self.generate_block.rotation = -1
                    self.block = self.generate_block.rotate_block(self.block)[0]
                    self.block_w = self.generate_block.rotate_block(self.block)[1]
                    self.block_h = self.generate_block.rotate_block(self.block)[2]

    def draw_board(self):

        # Draw board where blocks will fall and stack
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                colour = 0 if 0 == self.board[row][col] else self.board[row][col]
                pyxel.rect(col * 8 + 4, row * 8 + 8, 8, 8, colour)

    def stack_block(self):
        # for row in range
        pass

    def draw_block(self):
        for row in range(len(self.block)):
            for col in range(len(self.block[row])):
                colour = self.block[row][col]
                if colour != 0:
                    x = self.block_x + self.block_w
                    y = self.block_y + self.block_h
                    if colour == 6:
                        pyxel.rect((col * 8) + (x + 5), (y + 6) +
                                (row * 8), 8, 8, colour)
                    elif colour == 5:
                        pyxel.rect((col * 8) + (x + 4), (y + 8) +
                                (row * 8), 8, 8, colour)
                    else:
                        pyxel.rect((col * 8) + (x + 4), (y + 7) +
                                (row * 8), 8, 8, colour)
        # print(f"top left pos: ({self.block_x}, {self.block_y})")
        # print(f"top right pos: ({x},{self.block_y}), bottom left pos: ({self.block_x}, {y}), bottom right pos: ({x}, {y})")

    def falling_block(self):
        if not self.any_collisions():
            self.block_y += self.block_h

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

    def any_collisions(self):
        for row in range(len(self.block)):
            for col in range(len(self.block[row])):
                if self.block[row][col] != 0:
                    x = self.block_x + self.block_w
                    y = self.block_y + self.block_h
                    if self.block_x < 0 or x < 0:
                        return True
                    if self.block_h == 1:
                        if self.block_y > 174:
                            return True
                    elif self.block_h == 2:
                        if self.block_y > 163:
                            return True
                    elif self.block_h == 3:
                        if self.block_y > 154:
                            return True
                    else:
                        if self.block_y > 146:
                            return True
        return False



# b = Board()
# print(type(b.generate_block.w))
# for row in range(len(b.block)):
#     print(b.block[row])
#     for col in range(len(b.block)):
#         print(b.block[row][col])
