import pyxel
import random
from constants import *
from board import Board
from movement import Move
from scores import Scores
from tetromino import Tetromino


class Tetris:
    WINDOWWIDTH = 256
    WINDOWHEIGHT = 256
    def __init__(self):
        pyxel.init(Tetris.WINDOWWIDTH, Tetris.WINDOWHEIGHT, caption="Tetris", fps=60)
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
            # if pyxel.frame_count % self.fall_speed == 2:
            #     self.board.falling()

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                self.board.block.x = self.move.move_left()

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                self.board.block.x = self.move.move_right()

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                self.board.block.y = self.move.move_down()

            if pyxel.btn(pyxel.KEY_SPACE):
                self.board.block.y = self.move.hard_drop()

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.board.block.block = self.move.rotate_right()

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.board.block.block = self.move.rotate_left()
                
    def draw(self):
        pyxel.cls(0)
        self.draw_board()
        self.draw_grid()
        self.draw_borders()
        self.text()

        if self.state == "paused":
            pyxel.text(Tetris.WINDOWWIDTH // 2 - 20, Tetris.WINDOWHEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 16)

    def draw_borders(self):
        pyxel.rectb(4, 8, (BOARDWIDTH * GRID_SIZE) + 1, (BOARDHEIGHT * GRID_SIZE) + 1, 5)
        pyxel.rectb((Tetris.WINDOWWIDTH / 2) + 42, 16, 37, 48, 5)
        pyxel.rectb(Tetris.WINDOWWIDTH / 2 , 16, 37, 48, 5)

    def draw_grid(self):
        for row in range(10):
            pyxel.line(4 + (GRID_SIZE * row), 8, 4 + (GRID_SIZE * row), (BOARDHEIGHT * 12) + 8, 13)
            pyxel.line(4, 8 + (GRID_SIZE * row), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * row), 13)
            pyxel.line(4, 8 + (GRID_SIZE * (row + 10)), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * (row + 10)), 13)

    def draw_board(self):
        for row in range(BOARDHEIGHT):
            for col in range(BOARDWIDTH):
                if self.board.board[row][col] != 0:
                    pyxel.rect(col * GRID_SIZE + 4, row * GRID_SIZE + 8, 12, 12, self.board.board[row][col])
                else:
                    pyxel.rect(col * GRID_SIZE + 4, row * GRID_SIZE + 8, 12, 12, 7)
        
        for row in range(len(self.board.block.block)):
            for col in range(len(self.board.block.block[0])):
                if self.block.block[row][col] != 0:
                    pyxel.rect(col * GRID_SIZE + 4 + (Tetris.WINDOWWIDTH - BOARDWIDTH * GRID_SIZE) // 2 - self.block.x - GRID_SIZE - 16, row * GRID_SIZE + 9, 12, 12, self.board.block.block[row][col])
                    
    def text(self):
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 9, "HOLD: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 43, 9, "NEXT: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 70, "LEVEL: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 70, str(self.level), 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 80, "SCORE: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 80, str(self.score), 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 90, "LINES: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 90, str(self.lines), 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 100, "COMBOS: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 100, str(self.combos), 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 110, "SPINS: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 110, str(self.spins), 6)

        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 130, "P: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 20, 130, "PAUSE", 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 140, "Q: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 20, 140, "QUIT", 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 150, "R: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 20, 150, "RESTART", 6)

        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 170, "LEFT: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 170, "MOVE LEFT", 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 180, "RIGHT: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 180, "MOVE RIGHT", 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 190, "DOWN: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 190, "MOVE DOWN", 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 200, "SPACE: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 30, 200, "HARD DROP", 6)

        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 220, "Z: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 20, 220, "ROTATE LEFT", 6)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 1, 230, "X: ", 10)
        pyxel.text(Tetris.WINDOWWIDTH / 2 + 20, 230, "ROTATE RIGHT", 6)


if __name__ == "__main__":
    Tetris()