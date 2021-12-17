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
        self.cleared_lines = None
        self.consecutive_clears = -1

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

        self.clear_lines()
        self.block.x = self.start_pos_x
        self.block.y = self.start_pos_y
        self.block = None

    def clear_lines(self):
        lines_to_clear = []
        for index, row in enumerate(range(self.height)):
            if self.board[row].count(0) == 0:
                lines_to_clear.append(index)

        if len(lines_to_clear) > 0:
            for index in range(len(lines_to_clear)):
                self.board.pop(lines_to_clear[index])
                self.board.insert(0, [0] * self.width)
            
            self.cleared_lines = len(lines_to_clear)
            self.consecutive_clears += 1
        else:
            self.consecutive_clears = -1
        self.grid = deepcopy(self.board)