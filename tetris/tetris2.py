import pyxel
import random
from constants import *
from scores import Scores
from copy import deepcopy

BOARDWIDTH = 10
BOARDHEIGHT = 20
WINDOWWIDTH = 256
WINDOWHEIGHT = 256

GRID_SIZE = 12
BAG = [_ for _ in range(7)]


class Tetromino:
    O_MINO = {
        "block": [
            [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],
             
            [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": 0
        }
    
    S_MINO = {
        "block": [
            [[0, 4, 4, 0],
             [4, 4, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 4, 0, 0],
             [0, 4, 4, 0],
             [0, 0, 4, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [0, 4, 4, 0],
             [4, 4, 0, 0],
             [0, 0, 0, 0]],

            [[4, 0, 0, 0],
             [4, 4, 0, 0],
             [0, 4, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": 0
        }

    Z_MINO = {
        "block": [
            [[14, 14, 0, 0],
             [0, 14, 14, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 14, 0],
             [0, 14, 14, 0],
             [0, 14, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [14, 14, 0, 0],
             [0, 14, 14, 0],
             [0, 0, 0, 0]],

            [[0, 14, 0, 0],
             [14, 14, 0, 0],
             [14, 0, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": 0
        }

    J_MINO = {
        "block": [
            [[0, 0, 0, 0],
             [8, 8, 8, 0],
             [0, 0, 8, 0],
             [0, 0, 0, 0]],

            [[0, 8, 0, 0],
             [0, 8, 0, 0],
             [8, 8, 0, 0],
             [0, 0, 0, 0]],

            [[8, 0, 0, 0],
             [8, 8, 8, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 8, 8, 0],
             [0, 8, 0, 0],
             [0, 8, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": 0
        }

    L_MINO = {
        "block": [
            [[0, 0, 0, 0],
             [10, 10, 10, 0],
             [10, 0, 0, 0],
             [0, 0, 0, 0]],

            [[10, 10, 0, 0],
             [0, 10, 0, 0],
             [0, 10, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 10, 0],
             [10, 10, 10, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 10, 0, 0],
             [0, 10, 0, 0],
             [0, 10, 10, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": 0
        }

    T_MINO = {
        "block": [
            [[0, 0, 0, 0],
             [9, 9, 9, 0],
             [0, 9, 0, 0],
             [0, 0, 0, 0]],

            [[0, 9, 0, 0],
             [9, 9, 0, 0],
             [0, 9, 0, 0],
             [0, 0, 0, 0]],

            [[0, 9, 0, 0],
             [9, 9, 9, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 9, 0, 0],
             [0, 9, 9, 0],
             [0, 9, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": 0
        }

    I_MINO = {
        "block" : [
            [[0, 0, 0, 0],
             [12, 12, 12, 12],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 12, 0],
             [0, 0, 12, 0],
             [0, 0, 12, 0],
             [0, 0, 12, 0]],

            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [12, 12, 12, 12],
             [0, 0, 0, 0]],

            [[0, 12, 0, 0],
             [0, 12, 0, 0],
             [0, 12, 0, 0],
             [0, 12, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": 0
        }
    
    def __init__(self, generator):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.mino = self.tetrominos[generator]
        self.block = self.mino["block"][0]
        self.rotations = 4
        self.current_orientation = 0
        self.orientations = self.get_orientations()
        self.x = self.mino["x"]
        self.y = self.mino["y"]
        self.wallkicks = self.get_wallkicks(generator)
        
    def get_orientations(self):
        orientation = [
            self.block,
            self.mino["block"][1],
            self.mino["block"][2],
            self.mino["block"][3]
        ]
        return orientation

    def rotate_right(self):
        self.current_orientation += 1
        return self.orientations[self.current_orientation % self.rotations]
    
    def rotate_left(self):
        self.current_orientation -= 1
        return self.orientations[self.current_orientation % self.rotations]

    def get_wallkicks(self, generator): 
        if generator != 6:
            wallkicks = [
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 0 orientation: 0
                [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],  # 0 -> R  orientation: 1
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 2 orientation: 2
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],  # 2 -> L orientation: 3
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 0 orientation: 0
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],  # 0 -> L orientation: -1
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 2 orientation: -2
                [(0, 0), (-1, 0), (-1, 1), (0, 2), (-1, 2)]  # 2 -> R orientation: -3
            ]
        else:
            wallkicks = [
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],  # L -> 0 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # 0 -> R 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],  # R -> 2 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # 2 -> L 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # R -> 0 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],  # 0 -> L 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # L -> 2 
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)]  # 2 -> R 
            ]
        return wallkicks

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.grid = deepcopy(self.board)
        self.blocks = self.generate_block(BAG[0], BAG[1])
        self.block = self.blocks[0]
        self.next_block = self.blocks[1]
        self.start_pos_x = self.block.x
        self.start_pos_y = self.block.y
        self.cleared_lines = 0
        self.consecutive_clears = -1

    # Checks if a block on the board is falling
    def is_falling(self):
        return self.block != None

    # Generates a new block
    def generate_block(self, gen, gen2):
        # Ensure only one block is generated at a time
        # if self.is_falling():
        #     raise Exception("Block already falling")
        # else:
        block = Tetromino(gen)
        next_block = Tetromino(gen2)
        return [block, next_block]
    
    # Drops a block into its starting position on the board
    def drop_block(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        temp_x, temp_y = x, y

        while not self.detect_collision(temp_x, temp_y, mino, orientation):
            temp_y += 1
        
        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    self.grid[row + temp_y][col + temp_x] = 7
        
        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    self.grid[row + y][col + x] = block[row][col]

    def draw_board(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] != 0:
                    pyxel.rect(col * GRID_SIZE + 4, row * GRID_SIZE + 8, 12, 12, self.grid[row][col])

    def draw_next(self, x, y, mino, orientation):
        block = mino["block"][orientation]
        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    if block[row][col]  == 4 or block[row][col]  == 14:
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 65 + x, row * GRID_SIZE + 18 + GRID_SIZE + y, 12, 12, block[row][col])
                    elif block[row][col] == 1:
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 59 + x, row * GRID_SIZE + 18 + GRID_SIZE + y, 12, 12, block[row][col])
                    elif block[row][col] == 12:
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 59 + x, row * GRID_SIZE + 20 + y, 12, 12, block[row][col])
                    else:
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 65 + x, row * GRID_SIZE + 18 + y, 12, 12, block[row][col])
                    
                    
    # Makes the current block fall
    def falling(self, x, y, mino, orientation):
        if self.detect_collision(x, y, mino, orientation):
            self.fix_block()
        else:
            y += 1

    def detect_collision(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    if row + y + 1 > BOARDHEIGHT - 1:
                        return True
                    elif self.board[row + y + 1][col + x] != 0 and self.board[row + y + 1][col + x] != 7:
                        return True
        return False

    # Fixes the block in the current position and adds to the board
    def fix_block(self):
        for row in range(len(self.block.block)):
            for col in range(len(self.block.block[0])):
                if self.block.block[row][col] != 0:
                    self.board[row + self.block.y][col + self.block.x] = self.block.block[row][col]

        self.clear_lines()
        self.block.x = self.block.mino["x"]
        self.block.y = self.block.mino["y"]
        if not self.is_falling():
            self.block = self.next_block
            random.shuffle(BAG)
            self.blocks = self.generate_block(BAG[0], BAG[1])
            self.next_block = self.blocks[0]

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

class Move:
    def __init__(self, x, y, orientation, mino, board):
        self.mino = mino
        self.block = self.mino.block
        self.wallkicks = self.mino.wallkicks
        self.board = board
        self.x = x
        self.y = y
        self.orientation = orientation

    def move_left(self):
        print(f"x before: {self.x}")
        self.x -= 1
        print(f"x after: {self.x}")
        if not self.block_collision(self.block, x=-1):
            return self.x
        self.x += 1
        return self.x

    def move_right(self):
        print(f"x before: {self.x}")
        self.x += 1
        print(f"x after: {self.x}")
        if not self.block_collision(self.block, x=1):
            return self.x
        self.x -= 1
        return self.x

    def move_down(self):
        print(f"y before: {self.y}")
        self.y += 1
        print(f"y after: {self.y}")
        if not self.block_collision(self.block, y=1):
            return self.y
        self.y -= 1
        return self.y

    def hard_drop(self):
        for row in reversed(range(BOARDHEIGHT)):
            print(f"y: {self.y}")
            drop = row - self.y if self.y >=0 else row + self.y
            self.y += drop
            if not self.block_collision(self.block, y=drop):
                return self.y
        self.y -= drop
        return self.y

    def rotate_right(self):
        # self.block = self.mino.rotate_right()
        if self.orientation == 3:
            self.orientation = 0
            return self.orientation
        else:
            self.orientation += 1
        return self.orientation
        # if self.can_rotate_right(self.block):
        # if not self.block_collision(self.block):
        # self.block = self.mino.rotate_left()
        # return self.block
    
    def rotate_left(self):
        if self.orientation == 0:
            self.orientation = 3
            return self.orientation
        else:
            self.orientation -= 1
        return self.orientation
        # if self.can_rotate_left(self.block):
        # if not self.block_collision(self.block):
        # self.block = self.mino.rotate_right()
        # return self.block

    def block_collision(self, block, x=0, y=0):
        for row in range(len(block)):
            for col in range(len(block[0])):
                is_above_board = row + self.y< 0
                if is_above_board:
                    continue
                if block[row][col] != 0:
                    if col + self.x < 0 or col + self.x > BOARDWIDTH - 1:
                        print(f"col {col} + x {self.x}: {self.x + col}")
                        return True

                    if row + self.y > BOARDHEIGHT - 1:
                        return True

                    if self.board[row + self.y][col + self.x] != 0:
                        return True
        return False

    def can_rotate_right(self, block):
        wallkicks = self.wallkicks[4:]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.get_each_rotation_position(wallkicks, rotation)
        # if self.y < 0:
        #     new_y = self.y + 1
        # else:
        #     new_y = self.y
            
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if col + self.x + x < 0 or col + self.x + x >= BOARDWIDTH \
                             or row + self.y + y >= BOARDHEIGHT:
                            continue

                        if self.block_collision(block, x, y):
                            continue

                        if 0 <= col + self.x + x < BOARDWIDTH and row + self.y + y < BOARDHEIGHT:
                            self.x += x
                            self.y += y
                            return True
        return False

    def can_rotate_left(self, block):
        wallkicks = self.wallkicks[:4]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.get_each_rotation_position(wallkicks, rotation)
        # if self.mino.y < 0:
        #     new_y = self.mino.y + 1
        # else:
        #     new_y = self.mino.y
            
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if col + self.x + x < 0 or col + self.x + x >= BOARDWIDTH \
                             or row + self.y + y >= BOARDHEIGHT:
                            continue

                        if self.block_collision(block, x, y):
                            continue

                        if 0 <= col + self.x + x < BOARDWIDTH and row + self.y + y < BOARDHEIGHT:
                            self.x += x
                            self.y += y
                            return True
        return False

    def get_each_rotation_position(self, wallkicks, curr_rotation):
        for _ in range(len(wallkicks)):
            return wallkicks[curr_rotation]

class Tetris:
    def __init__(self):
        pyxel.init(WINDOWWIDTH, WINDOWHEIGHT, caption="Tetris", fps=60)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.state = "running"
        self.is_gameover = False

        self.level = Scores().level
        self.score = Scores().score
        self.lines = Scores().lines
        self.combos = Scores().combos
        self.spins = Scores().spins
        self.fall_speed = Scores().fall_speed

        random.shuffle(BAG)
        self.t = Tetromino(BAG[0])
        self.b = Board(BOARDWIDTH, BOARDHEIGHT)

        self.block = self.t.block
        self.next = Tetromino(BAG[1])
        self.next_block = self.next.block
        
        self.x = self.t.x
        self.y = self.t.y
        self.orientation = self.t.current_orientation

        self.board = self.b.board
        self.move = Move(self.x, self.y, self.orientation, self.t, self.board)


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
            if pyxel.frame_count % 60 * self.fall_speed == 0:
                if not self.b.detect_collision(self.x, self.y, self.t.mino, self.orientation):
                    self.y += 1
                    self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                self.x = self.move.move_left()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                self.x = self.move.move_right()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                self.y = self.move.move_down()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btn(pyxel.KEY_SPACE):
                self.y = self.move.hard_drop()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.orientation = self.move.rotate_right()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.orientation = self.move.rotate_left()
                self.b.grid = deepcopy(self.b.board)
                
    def draw(self):
        pyxel.cls(0)
        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)
        self.b.draw_next(self.next.x, self.next.y, self.next.mino, self.next.current_orientation)
        self.b.draw_board()
        self.draw_grid()
        self.draw_borders()
        self.text()

        if self.state == "paused":
            pyxel.text(WINDOWWIDTH // 2 - 20, WINDOWHEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 16)

    def draw_borders(self):
        pyxel.rectb(4, 8, (BOARDWIDTH * GRID_SIZE) + 1, (BOARDHEIGHT * GRID_SIZE) + 1, 5)
        pyxel.rectb((WINDOWWIDTH / 2) + 59, 16, 54, 48, 5)
        pyxel.rectb(WINDOWWIDTH / 2 , 16, 54, 48, 5)

    def draw_grid(self):
        for row in range(10):
            pyxel.line(4 + (GRID_SIZE * row), 8, 4 + (GRID_SIZE * row), (BOARDHEIGHT * 12) + 8, 13)
            pyxel.line(4, 8 + (GRID_SIZE * row), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * row), 13)
            pyxel.line(4, 8 + (GRID_SIZE * (row + 10)), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * (row + 10)), 13)
        
    def text(self):
        pyxel.text(WINDOWWIDTH / 2 + 1, 9, "HOLD: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 60, 9, "NEXT: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 1, 70, "LEVEL: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 70, str(self.level), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 80, "SCORE: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 80, str(self.score), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 90, "LINES: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 90, str(self.lines), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 100, "COMBOS: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 100, str(self.combos), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 110, "SPINS: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 110, str(self.spins), 6)

        pyxel.text(WINDOWWIDTH / 2 + 1, 130, "P: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 130, "PAUSE", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 140, "Q: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 140, "QUIT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 150, "R: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 150, "RESTART", 6)

        pyxel.text(WINDOWWIDTH / 2 + 1, 170, "LEFT: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 170, "MOVE LEFT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 180, "RIGHT: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 180, "MOVE RIGHT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 190, "DOWN: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 190, "MOVE DOWN", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 200, "SPACE: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 200, "HARD DROP", 6)

        pyxel.text(WINDOWWIDTH / 2 + 1, 220, "Z: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 220, "ROTATE LEFT", 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 230, "X: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 20, 230, "ROTATE RIGHT", 6)

if __name__ == "__main__":
    Tetris()