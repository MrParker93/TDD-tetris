import pyxel
import random
from constants import *
from copy import deepcopy

BOARDWIDTH = 10
BOARDHEIGHT = 20
WINDOWWIDTH = 256
WINDOWHEIGHT = 256

GRID_SIZE = 12
BAG = [_ for _ in range(7)]

LEVEL = 1
FALL_SPEED = 4
SCORE = 0
POINTS = {
    "1": 40,
    "2": 100,
    "3": 300,
    "4": 1200
}
LINES = 0 
COMBOS = 0
SPINS = 0
CLEARED = -1

class App:
    def __init__(self):
        pyxel.init(WINDOWWIDTH, WINDOWHEIGHT, caption="Tetris", fps=60)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.t = Tetromino()
        self.b = Board()
        self.s = Score()

        self.state = "running"
        self.is_gameover = False
        
        self.block = self.t.block
        self.next_block = self.t.next_block
        self.x = self.t.x
        self.y = self.t.y
        self.m = Move(self.b.board, self.t, self.x, self.y)

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
            if pyxel.frame_count % 60 == 0:
                print("HERE")
                self.y = self.b.falling(self.block, self.x, self.y)
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                self.x = self.m.move_left()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                self.x = self.m.move_right()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                self.y = self.m.move_down()
                self.b.grid = deepcopy(self.b.board)
            
            if pyxel.btnp(pyxel.KEY_SPACE, 10, 2):
                self.y = self.m.hard_drop()
                self.b.grid = deepcopy(self.b.board)
            
            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.block = self.m.rotate_right()
                self.b.grid = deepcopy(self.b.board)

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.block = self.m.rotate_left()
                self.b.grid = deepcopy(self.b.board)

    def draw(self):
        pyxel.cls(0)
        Text().text()
        self.b.draw_block_to_grid(self.block, self.x, self.y)
        self.b.draw_grid()
        self.draw_grid()
        self.draw_borders()
        # print(f"x: {self.x // GRID_SIZE}, y: {self.y // GRID_SIZE}")

        if self.state == "paused":
            pyxel.text(WINDOWWIDTH // 2 - 20, WINDOWHEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 16)

    def draw_borders(self):
        pyxel.rectb(4, 8, (BOARDWIDTH * GRID_SIZE) + 1, (BOARDHEIGHT * GRID_SIZE) + 1, 5)
        pyxel.rectb((WINDOWWIDTH / 2) + 42, 16, 37, 48, 5)
        pyxel.rectb(WINDOWWIDTH / 2 , 16, 37, 48, 5)

    def draw_grid(self):
        for row in range(BOARDWIDTH):
            pyxel.line(4 + (GRID_SIZE * row), 8, 4 + (GRID_SIZE * row), (BOARDHEIGHT * 12) + 8, 13)
            pyxel.line(4, 8 + (GRID_SIZE * row), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * row), 13)
            pyxel.line(4, 8 + (GRID_SIZE * (row + 10)), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * (row + 10)), 13)

class Tetromino:
    O_MINO = {
        "shape": "O",
        "block": [[5, 5],
                  [5, 5]],
        "rotations": 1,
        "width": 2,
        "height": 2,
        "x": ((BOARDWIDTH * GRID_SIZE // 2) - (2 * GRID_SIZE // 2)) // GRID_SIZE,
        "y": 0
        }
    
    S_MINO = {
        "shape": "S",
        "block": [[0, 4, 4],
                  [4, 4, 0],
                  [0, 0, 0]],
        "rotations": 2,
        "width": 3,
        "height": 2,
        "x": ((BOARDWIDTH * GRID_SIZE // 2) - (2 * GRID_SIZE // 2) - GRID_SIZE) // GRID_SIZE,
        "y": 0
        }

    Z_MINO = {
        "shape": "Z",
        "block": [[14, 14, 0],
                  [0, 14, 14],
                  [0, 0, 0]],
        "rotations": 2,
        "width": 3,
        "height": 2,
        "x": ((BOARDWIDTH * GRID_SIZE // 2) - (2 * GRID_SIZE // 2) - GRID_SIZE) // GRID_SIZE,
        "y": 0
        }

    J_MINO = {
        "shape": "J",
        "block": [[0, 0, 0],
                  [8, 8, 8],
                  [0, 0, 8]],
        "rotations": 4,
        "width": 3,
        "height": 2,
        "x": ((BOARDWIDTH * GRID_SIZE // 2) - (2 * GRID_SIZE // 2) - GRID_SIZE) // GRID_SIZE,
        "y": 0
        }

    L_MINO = {
        "shape": "L",
        "block": [[0, 0, 0],
                  [10, 10, 10],
                  [10, 0, 0]],
        "rotations": 4,
        "width": 3,
        "height": 2,
        "x": ((BOARDWIDTH * GRID_SIZE // 2) - (2 * GRID_SIZE // 2) - GRID_SIZE) // GRID_SIZE,
        "y": 0
        }

    T_MINO = {
        "shape": "T",
        "block": [[0, 0, 0],
                  [9, 9, 9],
                  [0, 9, 0]],
        "rotations": 4,
        "width": 3,
        "height": 2,
        "x": ((BOARDWIDTH * GRID_SIZE // 2) - (2 * GRID_SIZE // 2) - GRID_SIZE) // GRID_SIZE,
        "y": 0
        }

    I_MINO = {
        "shape": "I",
        "block" : [[0, 0, 0, 0],
                   [12, 12, 12, 12],
                   [0, 0, 0, 0]],
        "rotations": 2,
        "width": 4,
        "height": 1,
        "x": ((BOARDWIDTH * GRID_SIZE // 2) - (2 * GRID_SIZE // 2)) // GRID_SIZE,
        "y": 0
        }

    def __init__(self):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.randomize = random.shuffle(BAG)
        self.bag = deepcopy(BAG)
        self.mino = self.tetrominos[self.bag.pop(0)]
        self.next_mino = self.tetrominos[self.bag.pop(1)]
        self.shape = self.mino["shape"]
        self.block = self.mino["block"]
        self.next_block = self.next_mino["block"]
        self.rotations = self.mino["rotations"]
        self.wallkicks = self.get_wallkicks(self.mino)
        self.x = self.mino["x"]
        self.y = self.mino["y"]
        self.width = self.width()
        self.height = self.height()
        self.current_orientation = 0
        self.orientations = self.get_orientations(self.block)

    def get_orientations(self, block):
        orientation = [
            block,
            Rotate(block).rotate_right(),
            Rotate(block).rotate().rotate_right(),
            Rotate(block).rotate().rotate().rotate_right()
        ]
        if block[1][0] == 4: orientation[1], orientation[3] = orientation[3], orientation[1]
        return orientation[:self.rotations]

    def rotate_right(self):
        self.current_orientation += 1
        return self.orientations[self.current_orientation % self.rotations]
    
    def rotate_left(self):
        self.current_orientation -= 1
        return self.orientations[self.current_orientation % self.rotations]

    def width(self):
        return self.mino["width"]

    def height(self):
        return self.mino["height"]

    def get_wallkicks(self, mino): 
        if mino["shape"] != "I":
        #     wallkicks = [
        #         [(0, 0), (-GRID_SIZE, 0), (-GRID_SIZE, GRID_SIZE), (0, -(GRID_SIZE * 2)), (-GRID_SIZE, -(GRID_SIZE * 2))],  # L -> 0 orientation: 0
        #         [(0, 0), (-GRID_SIZE, 0), (-GRID_SIZE, -GRID_SIZE), (0, (GRID_SIZE * 2)), (-GRID_SIZE, (GRID_SIZE * 2))],  # 0 -> R  orientation: 1
        #         [(0, 0), (GRID_SIZE, 0), (GRID_SIZE, GRID_SIZE), (0, -(GRID_SIZE * 2)), (GRID_SIZE, -(GRID_SIZE * 2))],  # R -> 2 orientation: 2
        #         [(0, 0), (GRID_SIZE, 0), (GRID_SIZE, -GRID_SIZE), (0, (GRID_SIZE * 2)), (GRID_SIZE, (GRID_SIZE * 2))],  # 2 -> L orientation: 3
        #         [(0, 0), (GRID_SIZE, 0), (GRID_SIZE, GRID_SIZE), (0, -(GRID_SIZE * 2)), (GRID_SIZE, -(GRID_SIZE * 2))],  # R -> 0 orientation: 0
        #         [(0, 0), (GRID_SIZE, 0), (GRID_SIZE, -GRID_SIZE), (0, (GRID_SIZE * 2)), (GRID_SIZE, (GRID_SIZE * 2))],  # 0 -> L orientation: -1
        #         [(0, 0), (-GRID_SIZE, 0), (-GRID_SIZE, GRID_SIZE), (0, -(GRID_SIZE * 2)), (-GRID_SIZE, -(GRID_SIZE * 2))],  # L -> (GRID_SIZE * 2) orientation: -2
        #         [(0, 0), (-GRID_SIZE, 0), (-GRID_SIZE, GRID_SIZE), (0, (GRID_SIZE * 2)), (-GRID_SIZE, (GRID_SIZE * 2))]  # 2 -> R orientation: -3
        #     ]
        # else:
        #     wallkicks = [
        #         [(0, 0), (GRID_SIZE, 0), (-(GRID_SIZE * 2), 0), (GRID_SIZE, (GRID_SIZE * 2)), (-(GRID_SIZE * 2), -GRID_SIZE)],  # L -> 0 
        #         [(0, 0), (-(GRID_SIZE * 2), 0), (GRID_SIZE, 0), (-(GRID_SIZE * 2), GRID_SIZE), (GRID_SIZE, -(GRID_SIZE * 2))],  # 0 -> R 
        #         [(0, 0), (-GRID_SIZE, 0), ((GRID_SIZE * 2), 0), (-GRID_SIZE, -(GRID_SIZE * 2)), ((GRID_SIZE * 2), GRID_SIZE)],  # R -> 2 
        #         [(0, 0), ((GRID_SIZE * 2), 0), (-GRID_SIZE, 0), ((GRID_SIZE * 2), -GRID_SIZE), (-GRID_SIZE, (GRID_SIZE * 2))],  # 2 -> L 
        #         [(0, 0), ((GRID_SIZE * 2), 0), (-GRID_SIZE, 0), ((GRID_SIZE * 2), -GRID_SIZE), (-GRID_SIZE, (GRID_SIZE * 2))],  # R -> 0 
        #         [(0, 0), (-GRID_SIZE, 0), ((GRID_SIZE * 2), 0), (-GRID_SIZE, -(GRID_SIZE * 2)), ((GRID_SIZE * 2), GRID_SIZE)],  # 0 -> L 
        #         [(0, 0), (-(GRID_SIZE * 2), 0), (GRID_SIZE, 0), (-(GRID_SIZE * 2), GRID_SIZE), (GRID_SIZE, -(GRID_SIZE * 2))],  # L -> 2 
        #         [(0, 0), (GRID_SIZE, 0), (-(GRID_SIZE * 2), 0), (GRID_SIZE, (GRID_SIZE * 2)), (-(GRID_SIZE * 2), -GRID_SIZE)]  # 2 -> R 
        #     ]
        # return wallkicks
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
        
class Move:
    def __init__(self, board, mino, x, y):
        self.board = board
        self.mino = mino
        self.block = self.mino.block
        self.width = self.mino.width
        self.height = self.mino.height
        self.wallkicks = self.mino.wallkicks
        # self.x = x // GRID_SIZE
        self.x = x
        # self.y = y // GRID_SIZE
        self.y = y

    def move_left(self):
        print(f"x before: {self.x}")
        w = self.width
        h = self.height
        if not self.board_collision(w, h, x=-1) and not self.block_collision(self.block, x=-1):
            self.x -= 1
            print(f"x after: {self.x}")
            return self.x
        return self.x

    def move_right(self):
        print(f"x before: {self.x}")
        w = self.width
        h = self.height
        if not self.board_collision(w, h, x=1) and not self.block_collision(self.block, x=1):
            self.x += 1
            print(f"x after: {self.x}")
            return self.x
        return self.x

    def move_down(self):
        print(f"y before: {self.y}")
        w = self.width
        h = self.height
        if not self.board_collision(w, h, y=1) and not self.block_collision(self.block, y=1):
            self.y += 1
            print(f"y after: {self.y}")
            return self.y
        return self.y

    def hard_drop(self):
        w = self.width
        h = self.height
        for row in range(len(self.block)):
            for col in range(len(self.block[0])):
                if self.block[row][col] != 0:
                    drop = BOARDHEIGHT - 1 - 1 - self.y if self.block[row][col] != 12 else BOARDHEIGHT - 1 - self.y
                    if not self.board_collision(w, h, y=drop) and not self.block_collision(self.block, y=drop):
                        self.y += drop
                        return self.y
        return self.y

    def rotate_right(self):
        self.block = self.mino.rotate_right()
        self.width, self.height = self.height, self.width
        if self.board_collision(self.width, self.height):
        # if self.can_rotate_right(self.block, self.width, self.height):
            if 0 < self.x < BOARDWIDTH // 2:
                self.x + 1
                return self.block
            else:
                self.x - 1
                return self.block
        else:
            return self.block
        self.block = self.mino.rotate_left()
        self.width, self.height = self.height, self.width
        return self.block

    
    def rotate_left(self):
        self.block = self.mino.rotate_left()
        self.width, self.height = self.height, self.width
        if not self.board_collision(self.width, self.height):
            return self.block
        # if self.can_rotate_left(self.block):
        self.block = self.mino.rotate_right()
        self.width, self.height = self.height, self.width
        return self.block 

        # return self.block

    def block_collision(self, block, x=0, y=0):
        for row in range(len(block)):
            for col in range(len(block[0])):
                is_above_board = row + self.y + y < 0
                if is_above_board:
                    continue
                if block[row][col] != 0:
                    try:
                        if block[row][col] == 4 or block[row][col] == 5 or block[row][col] == 14:
                            if self.board[row + self.y + y][col + self.x + x] != 0:
                                return True
                        else:
                            if self.board[row + self.y + y - 1][col + self.x + x] != 0:
                                return True
                    except IndexError:
                        return True
        return False
    
    def board_collision(self, w, h, x=0, y=0):
        if self.mino.current_orientation % self.mino.rotations == 3:
            return self.x + x + w - 1 < 0 or self.x + x + w >= BOARDWIDTH or self.y + y + h - 2 >= BOARDHEIGHT
        elif self.mino.current_orientation % self.mino.rotations == 2 and self.mino.rotations == 4:
            return self.x + x < 0 or self.x + x + w - 1 >= BOARDWIDTH or self.y + y + h - 2 >= BOARDHEIGHT
        elif self.mino.current_orientation % self.mino.rotations == 1 and self.mino.rotations == 4:
            return self.x + x < 0 or self.x + x + w - 1 >= BOARDWIDTH or self.y + y + h - 2 >= BOARDHEIGHT
        elif self.mino.shape == "Z" and self.mino.current_orientation % self.mino.rotations != 0:
            return self.x + x + w - 1 < 0 or self.x + x + w >= BOARDWIDTH or self.y + y + h - 1 >= BOARDHEIGHT
        elif self.mino.shape == "I" and self.mino.current_orientation % self.mino.rotations != 0:
            return self.x + x + 1 < 0 or self.x + x + w >= BOARDWIDTH or self.y - 1 + y + h - 1 >= BOARDHEIGHT
        return self.x + x < 0 or self.x + x + w - 1 >= BOARDWIDTH or self.y + y + h - 1 >= BOARDHEIGHT
    
    def can_rotate_right(self, block, w ,h):
        wallkicks = self.wallkicks[4:]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.get_each_rotation_position(wallkicks, rotation)
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        print("-----------------------------")
                        print(f"Test x: {x}, Test y: {y}")
                        if self.board_collision(w, h, x=x, y=y):
                            print(f"Board collision: {x}, {y}")
                            continue

                        if self.block_collision(block, x=x, y=y):
                            print(f"Block collision: {x}, {y}")
                            continue
                            
                        # if self.x < 0:
                        #     self.x += x + 1
                        else:
                            print(f"No collision: {x}, {y}")
                            return True
        print(f"Can't rotate")
        return False

    def get_each_rotation_position(self, wallkicks, curr_rotation):
        for _ in range(len(wallkicks)):
            return wallkicks[curr_rotation]

class Board:
    def __init__(self):
        self.board = [[0] * BOARDWIDTH for _ in range(BOARDHEIGHT)]
        self.grid = deepcopy(self.board)

    def is_falling(self, block):
        return block != None

    def draw_block_to_grid(self, block, x, y):
        if self.is_falling(block):
            for row in range(len(block)):
                for col in range(len(block[0])):
                    if block[row][col] != 0:
                        if block[row][col] == 4 or block[row][col] == 5 or block[row][col] == 14:
                            self.grid[row + y][col + x] = block[row][col]
                        else:
                            self.grid[row + y - 1][col + x] = block[row][col]
                            #     pyxel.rect(col * GRID_SIZE + 4 + x, row * GRID_SIZE + 8 + y, 11, 11, block[row][col])
                        # else:
                        #     pyxel.rect(col * GRID_SIZE + 4 + x, row * GRID_SIZE - 4 + y, 11, 11, block[row][col])

    def draw_grid(self):
        for row in range(BOARDHEIGHT):
            for col in range(BOARDWIDTH):
                if self.grid[row][col] != 0:
                    pyxel.rect(col * GRID_SIZE + 4, row * GRID_SIZE + 8, 12, 12, self.grid[row][col])
                # colour = 7 if self.board[row][col] == 0 else self.board[row][col]
                # pyxel.rect(col * GRID_SIZE + 4, row * GRID_SIZE + 8, 12, 12, colour)
    
    def falling(self, block, x, y):
        if self.is_falling(block):
            if self.block_collision(block, x, y):
                self.fix_block(block, x, y)
            else:
                y += 1
                return y
    
    def block_collision(self, block, x=0, y=1):
        for row in range(len(block)):
            for col in range(len(block[0])):
                is_above_board = row + y + 1 < 0
                if is_above_board:
                    continue
                if block[row][col] != 0:
                    if row + y + 1 >= BOARDHEIGHT:
                        return True
                    try:
                        if block[row][col] == 4 or block[row][col] == 5 or block[row][col] == 14:
                            if self.board[row + y + 1][col + x] != 0:
                                return True
                        else:
                            if self.board[row + y + 1 - 1][col + x] != 0:
                                return True
                    except IndexError:
                        return True
        return False
    
    def fix_block(self, block, x, y):
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    self.board[row + y][col + x] = block[row][col]

class Rotate:
    def __init__(self, block):
        self.block = block

    def rotate_right(self):
        return self.rotate().block

    def rotate_left(self):
        return self.rotate().rotate().rotate().block

    def rotate(self):
        return Rotate(list(map(list, zip(*self.block[::-1]))))

class Score:
    def __init__(self):
        self.level = LEVEL
        self.score = SCORE
        self.lines = LINES
        self.combos = COMBOS
        self.spins = SPINS
        self.cleared = CLEARED
        self.fall_speed = FALL_SPEED

    def points(self, cleared):
        if cleared != None:
            self.lines += cleared
            self.cleared += 1
            if self.check_combo_count(self.combos):
                multiplier = (cleared * self.level) + (50 * self.level)
                self.score += POINTS[str(cleared)] * (self.level + 1) + multiplier
            else:
                self.score += POINTS[str(cleared)] * (self.level + 1)
        else:
            self.cleared = -1
        return self.score

    def check_combo_count(self):
        if self.cleared > 0:
            self.combos += 1
            return True
        return False

    def can_level_up(self):
        return self.lines > self.level * 5

class Text:
    def text(self):
        pyxel.text(WINDOWWIDTH / 2 + 1, 9, "HOLD: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 43, 9, "NEXT: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 1, 70, "LEVEL: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 70, str(Score().level), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 80, "SCORE: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 80, str(Score().score), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 90, "LINES: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 90, str(Score().lines), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 100, "COMBOS: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 100, str(Score().combos), 6)
        pyxel.text(WINDOWWIDTH / 2 + 1, 110, "SPINS: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 30, 110, str(Score().spins), 6)

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
    App()