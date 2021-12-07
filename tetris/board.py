import math
from random import randint
from copy import deepcopy
from tetromino import Tetromino

class Board(Tetromino):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.grid = deepcopy(self.board)
        self.block = None
        self.start_position = (int(self.width / 2), 0)
        self.current_position = self.start_position

    # Checks if a block on the board is falling
    def is_falling(self):
        return self.block != None

    # Generates a new block
    def generate_block(self):
        # Ensure only one block is generated at a time
        if self.is_falling():
            raise Exception("Block already falling")
        else:
            self.block = Tetromino(randint(0, 6)).block
            self.start_position = ((int(self.width / 2) - int(len(self.block[0])), 0))
    
    # Drops a block into its starting position on the board
    def drop_block(self):
        for row in range(len(self.block)):
            for col in range(len(self.block[0])):
                if self.block[row][col] != 0:
                    self.grid[row + self.current_position[1]][col + self.current_position[0] 
                    - int(len(self.block[0]) / 2)] = self.block[row][col]
                        
    # Makes the current block fall
    def falling(self):
        if self.detect_collision():
            self.fix_block()
        else:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)

    # Checks if current block collides with another block or board boundaries
    def detect_collision(self):
        return self.board_collision() or self.block_collision()
    
    def board_collision(self):
        return self.current_position[1] + math.ceil(len(self.block) / 2) >= self.height

    def block_collision(self):
        return self.grid[self.current_position[1] + 1][self.current_position[0]] != 0

    # Fixes the block in the current position and adds to the board
    def fix_block(self):
        self.board[self.current_position[0]][self.current_position[1]] = self.grid[self.current_position[0]][self.current_position[1]]
        self.current_position = self.start_position
        # self.block = None
