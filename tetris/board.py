import pyxel
from gamelogic import GameLogic
from tetrimino import TetriminoGenerator


class Board:
    WIDTH = 10
    HEIGHT = 20

    def __init__(self):
        self.board = [[0] * Board.WIDTH for _ in range(Board.HEIGHT)]
        self.l = GameLogic()
        self.gen = TetriminoGenerator()
        self.generate_block = self.gen.generate()
        self.block = self.generate_block.block
        self.x = self.generate_block.x
        self.y = self.generate_block.y
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
                if self.any_collisions(self.x, self.y, self.block):
                    self.falling_block()

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                new_x = self.generate_block.move_block_left()
                if self.any_collisions(new_x, self.y, self.block):
                    self.x = new_x

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                new_x = self.generate_block.move_block_right()
                if self.any_collisions(new_x, self.y, self.block):
                    self.x = new_x

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                new_y = self.generate_block.move_block_down()
                if self.any_collisions(self.x, new_y, self.block):
                    self.y = new_y

            if pyxel.btn(pyxel.KEY_SPACE):
                if not self.any_collisions():
                    self.position = self.generate_block.place_block()

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.generate_block.rotation = 1
                new_block = self.generate_block.rotate_block(self.block)
                if self.any_collisions(self.x, self.y, new_block) and self.block[0][0] != 5:
                    self.block = new_block

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.generate_block.rotation = -1
                new_block = self.generate_block.rotate_block(self.block)
                if self.any_collisions(self.x, self.y, new_block) and self.block[0][0] != 5:
                    self.block = new_block

    def draw_board(self):
        
        # Draw board where blocks will fall and stack
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                pyxel.rect(col * 8 + 4, row * 8 + 8, 8,
                           8, self.board[row][col])

    def draw_block(self):

        for row in range(len(self.block)):
            for col in range(len(self.block[row])):
                # if self.block[row][col] != 0:
                colour = self.block[row][col]
                self.board[row + self.y][col + self.x] = colour

    def stack_block(self):
        for row in range(len()):
            pass    


    def falling_block(self):
        # self.y += 1
        pass

    def draw_next_block(self):
        for row in range(len(self.next_block)):
            for col in range(len(self.next_block[row])):
                colour = self.next_block[row][col]
                if colour == 6:
                    pyxel.rect((col * 8) + 140 * 0.77,
                               24 + (row * 8), 8, 8, colour)
                elif colour == 5:
                    pyxel.rect((col * 8) + 140 * 0.74,
                               40 + (row * 8), 8, 8, colour)
                elif colour == 1 or colour == 2 or colour == 9:
                    pyxel.rect((col * 8) + 140 * 0.75,
                               32 + (row * 8), 8, 8, colour)
                else:
                    pyxel.rect((col * 8) + 140 * 0.74,
                               32 + (row * 8), 8, 8, colour)

    def any_collisions(self, x, y, block):
        size = self.generate_block.block_size(block)
        if x < 0 or (x + size[1]) > Board.WIDTH \
            or y + size[0] > Board.HEIGHT:
                return False
        return True
