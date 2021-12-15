from random import randint
from copy import deepcopy

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.grid = deepcopy(self.board)
        self.block = None

    # Checks if a block on the board is falling
    def is_falling(self):
        return self.block != None

    # Generates a new block
    def generate_block(self):
        # Ensure only one block is generated at a time
        if self.is_falling():
            raise Exception("Block already falling")
        else:
            pass
    
    # Drops a block into its starting position on the board
    def drop_block(self):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] == 7:
                    self.grid[row + self.block.y - 1][col + self.block.x] = self.block.block[row][col]
                elif self.block.block[row][col] != 0:
                    self.grid[row + self.block.y][col + self.block.x] = self.block.block[row][col]
                    # print(f"row: {row + self.block.y}, col: {col + self.block.x}")
                    
    # Makes the current block fall
    def falling(self):
        if self.detect_collision(y=1):
            self.fix_block()
        else:
            self.block.y += 1

    # Checks if current block collides with another block or board boundaries
    def detect_collision(self, y=1):
        return self.board_collision(y) or self.block_collision(y)
    
    def board_collision(self, y=1):
        return self.block.y + y >= self.height

    def block_collision(self, y=1):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] == 7:
                    if self.grid[row + self.block.y][col + self.block.x] != 0:
                        return True
                elif self.block.block[row][col] != 0:
                    if self.grid[row + self.block.y + y][col + self.block.x] != 0:
                        return True
        return False

    # Fixes the block in the current position and adds to the board
    def fix_block(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.grid[row][col] != 0:
                    self.board[row][col] = self.grid[row][col]
        self.block.x = self.width // 2 - self.block.width // 2
        self.block.y = 0
        self.block = None