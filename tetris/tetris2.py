import pyxel
import random
from constants import *
from board import Board
from movement import Move
from scores import Scores
from copy import deepcopy 
from tetromino import Tetromino

BOARDWIDTH = 10
BOARDHEIGHT = 20
WINDOWWIDTH = 256
WINDOWHEIGHT = 256

GRID_SIZE = 12
BAG = [_ for _ in range(7)]

class Tetris:
    def __init__(self):
        pyxel.init(WINDOWWIDTH, WINDOWHEIGHT, caption="Tetris", fps=60)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.level = Scores().level
        self.score = Scores().score
        self.lines = Scores().lines
        self.combos = Scores().combos
        self.spins = Scores().spins
        self.fall_speed = Scores().fall_speed
        self.state = "running"
        self.is_gameover = False
        self.bag = random.shuffle(BAG)
        self.board = Board(BOARDWIDTH, BOARDHEIGHT)
        self.board.generate_block(BAG[0], BAG[1])
        self.block = self.board.block
        self.next_block = self.board.next_block
        self.move = Move(self.block, self.board.board)


    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.state == "running" or self.state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()
        
        if pyxel.btn(pyxel.KEY_P):
            if self.state == "running" and not self.is_gameover:
                self.state = "paused"
            else:
                self.state = "running"
        
        if self.state == "running":
            if pyxel.frame_count % 60 * self.fall_speed == 0:
                self.fall()
                self.board.grid = deepcopy(self.board.board)

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                self.board.block.x = self.move.move_left()
                self.board.grid = deepcopy(self.board.board)

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                self.board.block.x = self.move.move_right()
                self.board.grid = deepcopy(self.board.board)

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                self.board.block.y = self.move.move_down()
                self.board.grid = deepcopy(self.board.board)

            if pyxel.btn(pyxel.KEY_SPACE):
                self.board.block.y = self.move.hard_drop()
                self.board.grid = deepcopy(self.board.board)

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.board.block.block = self.move.rotate_right()
                self.board.grid = deepcopy(self.board.board)

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.board.block.block = self.move.rotate_left()
                self.board.grid = deepcopy(self.board.board)
                
    def draw(self):
        pyxel.cls(0)
        self.board.drop_block()
        self.board.draw_board()
        self.draw_grid()
        self.board.draw_next()
        self.draw_borders()
        self.text()

        if self.state == "paused":
            pyxel.text(WINDOWWIDTH // 2 - 20, WINDOWHEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 16)

    def draw_borders(self):
        pyxel.rectb(4, 8, (BOARDWIDTH * GRID_SIZE) + 1, (BOARDHEIGHT * GRID_SIZE) + 1, 5)
        pyxel.rectb((WINDOWWIDTH / 2) + 42, 16, 54, 48, 5)
        pyxel.rectb(WINDOWWIDTH / 2 , 16, 37, 48, 5)

    def draw_grid(self):
        for row in range(10):
            pyxel.line(4 + (GRID_SIZE * row), 8, 4 + (GRID_SIZE * row), (BOARDHEIGHT * 12) + 8, 13)
            pyxel.line(4, 8 + (GRID_SIZE * row), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * row), 13)
            pyxel.line(4, 8 + (GRID_SIZE * (row + 10)), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * (row + 10)), 13)

    def fall(self):
        if not self.block_collision(y=1):
            self.block.y += 1
        else:
            self.fix_block()

    def block_collision(self, x=0, y=0):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] != 0:
                    if row + self.block.y + y >= BOARDHEIGHT:
                        return True
                    elif self.board.board[row + self.block.y + y][col + self.block.x + x] != 0:
                        return True
        return False

    def fix_block(self):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] != 0:
                    self.board.board[row + self.block.y][col + self.block.x] = self.block.block[row][col]

        self.generate_new_blocks()

    def generate_new_blocks(self):
        self.block = self.next_block
        self.block.y = -2
        self.block.x = (BOARDWIDTH // 2 - 4 // 2)
        self.move = Move(self.block, self.board.board)
        self.board.generate_block(BAG[0], BAG[1])
        self.next_block = self.board.next_block
        
    def text(self):
        pyxel.text(WINDOWWIDTH / 2 + 1, 9, "HOLD: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 43, 9, "NEXT: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 1, 70, "LEVEL: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 70, str(self.level), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 80, "SCORE: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 80, str(self.score), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 90, "LINES: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 90, str(self.lines), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 100, "COMBOS: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 100, str(self.combos), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 110, "SPINS: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 110, str(self.spins), 6)

        pyxel.text(WINDOWWIDTH / 2 + 1, 130, "P: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 130, "PAUSE", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 140, "Q: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 140, "QUIT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 150, "R: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 150, "RESTART", 6)

        pyxel.text(WINDOWWIDTH / 2 + 1, 170, "LEFT: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 170, "MOVE LEFT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 180, "RIGHT: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 180, "MOVE RIGHT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 190, "DOWN: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 190, "MOVE DOWN", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 200, "SPACE: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 200, "HARD DROP", 6)

        pyxel.text(WINDOWWIDTH / 2 + 1, 220, "Z: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 220, "ROTATE LEFT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 230, "X: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 230, "ROTATE RIGHT", 6)


if __name__ == "__main__":
    Tetris()