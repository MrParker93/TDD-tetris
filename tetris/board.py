import pyxel
import random
from block import Block

class Board:
    WIDTH = 3
    HEIGHT = 3
    def __init__(self) -> None:
        self.board = [[0] * Board.WIDTH for _ in range(Board.HEIGHT)]
        self.block = None

    def is_falling(self):
        return self.block != None

    def start_falling(self):
        if self.is_falling():
            self.block = self.block.move_block(0, int(len(self.board[0]) / 2))
            # self.falling()
        else:
            block = self.generate_block()
            self.block = block.move_block(0, int(len(self.board[0]) / 2))
            # self.falling()

    def generate_block_on_board(self):
        new_board = []
        for row in range(len(self.board)):
            new_board.append([])
            for col in range(len(self.board[row])):
                new_board[row].append(self.check_grid_at(row, col))
        return new_board

    def check_grid_at(self, row, col):
        if self.is_falling() and self.block.block_position(row, col):
            return self.block.block
        else:
            return self.board[row][col]

    def generate_block(self):
        if not self.is_falling():
            block = Block(0, 0, random.choice(["I", "J", "L", "T", "Z", "S", "O"]))
            return block
        raise ValueError("Block is already falling")
    
    def falling(self):
        block = self.block.move_block_down()
        if self.detect_collision(block):
            self.stop_falling()
        else:
            self.block = block

    def detect_collision(self, block):
        return self.invalid_position(block) or self.block_collision(block)
    
    def invalid_position(self, block):
        return block.row >= Board.HEIGHT or \
                block.col < 0 or \
                    block.col >= Board.WIDTH                    

    def block_collision(self, block):
        return self.board[block.row][block.col] != 0

    def stop_falling(self):
        self.place_block()
        self.block = None
        self.generate_block()

    def place_block(self):
        self.board[self.block.row][self.block.col] = self.block.block
