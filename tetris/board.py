import pyxel
from constants import *


class Board:
    def __init__(self):
        self.board = BOARD_GRID
        self.next_piece_board = NEXT_GRID

    def draw_border(self):
        # Main area for gameplay
        pyxel.rectb(4, 8, 10 * 8, 22 * 7.8, 5)

        # Show next block
        pyxel.rectb(87, 16, 30, 6 * 8, 5)

    def draw_block(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    pyxel.blt(col * 8, row * 8, 0, 0, self.board[row][col], 8, 8)

    def draw_next_block(self):
        for row in range(6):
            for col in range(4):
                if self.next_piece_board[row][col] != 0:
                    if self.next_piece_board[row][col] == 8:
                        pyxel.blt((col * 8) + 95, (row * 8) + 40, 0, 0, self.next_piece_board[row][col], 8, 8)

                    elif self.next_piece_board[row][col] == 88:
                        pyxel.blt((col * 8) + 82, (row * 8) + 24, 0, 0, self.next_piece_board[row][col], 8, 8)

                    else:
                        pyxel.blt((col * 8) + 87, (row * 8) + 32, 0, 0, self.next_piece_board[row][col], 8, 8)

