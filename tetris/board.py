import pyxel
import pprint
from gamelogic import GameLogic
from tetrimino import TetriminoGenerator


class Board:
    WIDTH = 10
    HEIGHT = 20

    def __init__(self, block, x, y):
        self.block = block
        self.pos_x = x
        self.pos_y = y 
        self.board = [[0] * Board.WIDTH for _ in range(Board.HEIGHT)]  # Create the board where the game is played
        self.board_edge = [[0] * (Board.WIDTH + 2) for _ in range(Board.HEIGHT + 1)]  # Create the boundaries where the game is limited to
        
        for row in range(len(self.board_edge)):
            for col in range(len(self.board_edge[row])):
                if col == 0 or col == Board.WIDTH + 1 or row == Board.HEIGHT:  # Sets the boundaries of the board to -1
                    self.board_edge[row][col] = -1

    def draw_board(self):
        
        # Draw board where blocks will fall and stack
        for row in range(len(self.board_edge)):
            for col in range(len(self.board_edge[row])):
                if self.board_edge[row][col] != -1:
                    pyxel.rect(col * 8 + 4, row * 8 + 8, 8,
                            8, self.board_edge[row][col])

    def draw_block(self):

        for row in range(len(self.block)):
            for col in range(len(self.block[row])):
                if self.block[row][col] != 0:
                    colour = self.block[row][col]
                    self.board_edge[row + self.pos_y][col + self.pos_x] = colour

    def stack_block(self):
        for row in range(len()):
            pass    

    def falling_block(self):
        # self.y += 1
        pass

    def any_collisions(self, x, y, width, height):
        
        for row in range(len(self.board_edge)):
            for col in range(len(self.board_edge[row])):
                if self.board_edge[row][col + x] == -1 \
                    or self.board_edge[row][x] == -1 \
                    or self.board_edge[row + y][col] == -1:
                        return True
        return False
                

        # print(x, y)
        # if x < 0 or (x + size[1]) > Board.WIDTH \
        #     or y + size[0] > Board.HEIGHT:
        #         return False
        # return True
