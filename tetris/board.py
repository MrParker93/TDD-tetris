import pyxel
import random
from block import Block
from movable_mino import MovableMino

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0] * self.cols for _ in range(self.rows)]
        self.block = None

    def generate_block(self):
        if not self.is_falling():
            block = MovableMino(0, 0, random.choice(["I", "J", "L", "T", "Z", "S", "O"]))
            return block
        raise ValueError("Block is already falling")

    def generate_block_on_board(self):
        new_board = []
        for row in range(len(self.board)):
            new_board.append([])
            for col in range(len(self.board[row])):
                new_board[row].append(self.check_grid_at(row, col))
        return new_board

    def start_falling(self):
        if self.is_falling():
            self.block = self.block.move_block(0, int(len(self.board[0]) / 2))
            # self.falling()
        else:
            block = self.generate_block()
            self.block = block.move_block(0, int(len(self.board[0]) / 2))
            # self.falling()
    
    def falling(self):
        block = self.block.move_block_down()
        if self.detect_collision(block):
            self.stop_falling()
        else:
            self.block = block

    def is_falling(self):
        return self.block != None

    def check_grid_at(self, row, col):
        if self.is_falling() and self.block.block_position(row, col):
            return self.block.block
        else:
            return self.board[row][col]

    def detect_collision(self, block):
        return self.invalid_position(block) or self.block_collision(block)
    
    def invalid_position(self, block):
        return block.row >= self.board_length() or \
                block.col < 0 or \
                    block.col >= self.board_width()                    

    def block_collision(self, block):
        return self.board[block.row][block.col] != 0

    def stop_falling(self):
        self.place_block()
        self.block = None
        self.generate_block()

    def place_block(self):
        self.board[self.block.row][self.block.col] = self.block.block

    def rows(self):
        return len(self.board)

    def cols(self):
        return len(self.board[0])
