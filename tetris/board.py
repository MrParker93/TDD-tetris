import pyxel
import random
from tetromino import Tetrominoes
from constants import BOARD_GRID, BLOCKS


class Board:
    def __init__(self, block=None, next_block=None):
        self.board = BOARD_GRID

        if block != None:
            self.block = block
        else:
            self.block = Tetrominoes(block=random.sample(BLOCKS, 7).pop())

        if next_block != None:
            self.next_block = next_block
        else:
            self.next_block = Tetrominoes(block=random.sample(BLOCKS, 7).pop())

    def draw_border(self):
        # Main area for gameplay
        pyxel.rectb(4, 8, 10 * 8, 22 * 7.8, 5)

        # Show next block
        pyxel.rectb(87, 16, 30, 6 * 8, 5)

    def draw_block(self, x=0, y=0):
        current_block = self.block.get_block_sections(self.block.position)

        for row in range(len(current_block["block"])):
            for col in range(len(current_block["block"][row])):
                if current_block["block"][row][col] != 0:
                    block_colour = current_block["block"][row][col]
                    pyxel.blt(col * 8 + x, row * 8 + y, 0, 0, block_colour, 8, 8)

    def draw_next_block(self):
        next_block = self.next_block.get_block_sections(self.next_block.position)

        for row in range(len(next_block["block"])):
            for col in range(len(next_block["block"][row])):
                if next_block["block"][row][col] != 0:
                    block_colour = next_block["block"][row][col]

                    if block_colour == 8:
                        pyxel.blt((col * 8) + 95, (row * 8) + 40, 0, 0, block_colour, 8, 8)                

                    elif block_colour == 88:
                        pyxel.blt((col * 8) + 87, (row * 8) + 24, 0, 0, block_colour, 8, 8)                

                    elif block_colour == 160 or block_colour == 192 or block_colour == 72:
                        pyxel.blt((col * 8) + 95, (row * 8) + 32, 0, 0, block_colour, 8, 8)

                    else:
                        pyxel.blt((col * 8) + 87, (row * 8) + 32, 0, 0, block_colour, 8, 8)
