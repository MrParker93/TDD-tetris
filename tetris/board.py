from copy import deepcopy
from random import randint
from tetromino import Tetromino


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.grid = deepcopy(self.board)
        self.block = None
        self.start_pos_x = None
        self.start_pos_y = None

    # Checks if a block on the board is falling
    def is_falling(self):
        return self.block != None

    # Generates a new block
    def generate_block(self, generator):
        # Ensure only one block is generated at a time
        if self.is_falling():
            raise Exception("Block already falling")
        else:
            self.block = Tetromino(generator)
            self.start_pos_x = deepcopy(self.block.x)
            self.start_pos_y = deepcopy(self.block.y)
    
    # Drops a block into its starting position on the board
    def drop_block(self):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] != 0:
                    print(f"y: {self.block.y}, x: {self.block.x}")
                    print(f"row: {row + self.block.y}, col: {col + self.block.x}")
                    print()
                    self.grid[row + self.block.y][col + self.block.x] = self.block.block[row][col]
                    
    # Makes the current block fall
    def falling(self):
        if self.detect_collision(y=1):
            self.fix_block()
        else:
            self.block.y += 1

    # Checks if current block collides with another block or board boundaries
    def detect_collision(self, x=0, y=0):
        return self.block_collision(x, y)
    
    # def board_collision(self, x=0, y=0):
    #     return self.block.y + y >= self.height or 0 > self.block.x + x > self.width

    def block_collision(self, x=0, y=0):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] != 0:
                    if row + self.block.y + y >= self.height:
                        return True
                    elif self.grid[row + self.block.y + y][col + self.block.x + x] != 0:
                        return True
        return False

    # Fixes the block in the current position and adds to the board
    def fix_block(self):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] != 0:
                    self.board[row + self.block.y][col + self.block.x] = self.block.block[row][col]
        # for row in range(len(self.board)):
        #     for col in range(len(self.board[0])):
        #         if self.grid[row][col] != 0:
        #             self.board[row][col] = self.grid[row][col]
        self.block.x = self.start_pos_x
        self.block.y = self.start_pos_y
        self.block = None