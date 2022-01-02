import pyxel
import random
from copy import deepcopy

"""
TODO: Fix TGM random mode (spawning specific minos only)
TODO: Add soft drop points per grid (1/grid) max points possible 20.
TODO: Add hard drop points per grid (2/grid) max points possible 40.
TODO: Add hold tetromino option.
TODO: Add music and more/improved sound effects.
TODO: Add difficult settings (change fall speed, lines needed for level up, point distribution etc).
TODO: Add two player mode and invisible mode.
TODO: Test the time complexity of each function and use better algorithms where it can be improved.
TODO: Add leaderboard and keep a history of top scores.
TODO: Add spin scores for every tetromino except O.
TODO: Option for player to set controls."""

BOARDWIDTH = 10
BOARDHEIGHT = 30
WINDOWWIDTH = 256
WINDOWHEIGHT = 256

TITLE_SCENE = 0
GAME_SCENE = 1
GAMEOVER_SCENE = 2
RANDOMIZER = {
    "tetris 1985": True,
    "tetris nintendo": True,
    "tetris grand master": True,
    "tetris worlds": True
}

GRID_SIZE = 12  
BAG = [_ for _ in range(7)]
LOCK_DELAY = 60
LEVEL = 1
FALL_SPEED = 2
SCORE = 0
LINES = 0 
COMBOS = 0
SPINS = 0
T_SPIN = {
    "mini": 100,
    "single": 800,
    "double": 1200,
    "triple": 1600,
    "B2B double": 1800,
    "B2B triple": 2400
}

POINTS = {
    "0": 0,
    "1": 100,
    "2": 300,
    "3": 500,
    "4": 800
}

class Tetromino:
    O_MINO = {
        "shape": "O",
        "block": [
            [[0, 10, 10, 0],
             [0, 10, 10, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],
             
            [[0, 10, 10, 0],
             [0, 10, 10, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 10, 10, 0],
             [0, 10, 10, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 10, 10, 0],
             [0, 10, 10, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (0, 1)
        }
    
    S_MINO = {
        "shape": "S",
        "block": [
            [[0, 3, 3, 0],
             [3, 3, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 3, 0, 0],
             [0, 3, 3, 0],
             [0, 0, 3, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [0, 3, 3, 0],
             [3, 3, 0, 0],
             [0, 0, 0, 0]],

            [[3, 0, 0, 0],
             [3, 3, 0, 0],
             [0, 3, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    Z_MINO = {
        "shape": "Z",
        "block": [
            [[8, 8, 0, 0],
             [0, 8, 8, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 8, 0],
             [0, 8, 8, 0],
             [0, 8, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [8, 8, 0, 0],
             [0, 8, 8, 0],
             [0, 0, 0, 0]],

            [[0, 8, 0, 0],
             [8, 8, 0, 0],
             [8, 0, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    J_MINO = {
        "shape": "J",
        "block": [
            [[5, 0, 0, 0],
             [5, 5, 5, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 5, 5, 0],
             [0, 5, 0, 0],
             [0, 5, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [5, 5, 5, 0],
             [0, 0, 5, 0],
             [0, 0, 0, 0]],

            [[0, 5, 0, 0],
             [0, 5, 0, 0],
             [5, 5, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    L_MINO = {
        "shape": "L",
        "block": [
            [[0, 0, 9, 0],
             [9, 9, 9, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 9, 0, 0],
             [0, 9, 0, 0],
             [0, 9, 9, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [9, 9, 9, 0],
             [9, 0, 0, 0],
             [0, 0, 0, 0]],

            [[9, 9, 0, 0],
             [0, 9, 0, 0],
             [0, 9, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    T_MINO = {
        "shape": "T",
        "block": [
            [[0, 2, 0, 0],
             [2, 2, 2, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 2, 0, 0],
             [0, 2, 2, 0],
             [0, 2, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [2, 2, 2, 0],
             [0, 2, 0, 0],
             [0, 0, 0, 0]],

            [[0, 2, 0, 0],
             [2, 2, 0, 0],
             [0, 2, 0, 0],
             [0, 0, 0, 0]]
        ],
        "x": BOARDWIDTH // 2 - 4 // 2,
        "y": -2,
        "centre": (1, 1)
        }

    I_MINO = {
        "shape": "I",
        "block": [
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
        "x": BOARDWIDTH // 2 - 4 // 2 + 1,
        "y": -2,
        "centre": (1, 1)
        }
    
    def __init__(self, generator):
        self.tetrominos = [self.O_MINO, self.S_MINO, self.Z_MINO, self.J_MINO, self.L_MINO, self.T_MINO, self.I_MINO]
        self.index = generator
        self.mino = self.tetrominos[generator]
        self.block = self.mino["block"][0]
        self.rotations = 4
        self.current_orientation = 0
        self.orientations = self.get_orientations()
        self.x = self.mino["x"]
        self.y = self.mino["y"]
        self.wallkicks = self.get_wallkicks()

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

    def get_wallkicks(self): 
        if self.mino["shape"] != "I":
            wallkicks = [
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 0 orientation: 0
                [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],  # 0 -> R  orientation: 1
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 2 orientation: 2
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],  # 2 -> L orientation: 3
                [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],  # R -> 0 orientation: 0
                [(0, 0), (-1, 0), (-1, 1), (0, 2), (-1, 2)],  # 2 -> R orientation: 1
                [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # L -> 2 orientation: 2
                [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)]  # 0 -> L orientation: 3
            ]
        else:
            wallkicks = [
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],  # L -> 0 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # 0 -> R 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],  # R -> 2 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # 2 -> L 
                [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],  # R -> 0 
                [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],  # 2 -> R 
                [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],  # L -> 2 
                [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)]  # 0 -> L 
            ]
        return wallkicks

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.grid = deepcopy(self.board)
        self.cleared_lines = 0
        self.consecutive_clears = -1
    
    def drop_block(self, x, y, mino, orientation):
        block = mino["block"][orientation]
        shape = mino["shape"]

        temp_x, temp_y = x, y

        while not self.detect_collision(temp_x, temp_y, mino, orientation):
            temp_y += 1
        
        if shape != "I":
            if y > -1:
                for row in range(4):
                    for col in range(4):
                        if block[row][col] != 0:
                            self.grid[row + temp_y][col + temp_x] = 1
        else:
            if y > -2:
                for row in range(4):
                    for col in range(4):
                        if block[row][col] != 0:
                            self.grid[row + temp_y][col + temp_x] = 1

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    self.grid[row + y][col + x] = block[row][col]

    def draw_board(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] != 0:
                    pyxel.rect(col * GRID_SIZE + 4, row * GRID_SIZE + 8, 12, 12, self.grid[row][col])

    def draw_next(self, mino):
        block = mino["block"][0]
        shape = mino["shape"]
        
        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    if shape == "S" or shape == "Z":
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 9, row * GRID_SIZE + 18 + GRID_SIZE, 12, 12, block[row][col])
                    elif shape == "O":
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 3, row * GRID_SIZE + 18 + GRID_SIZE, 12, 12, block[row][col])
                    elif shape == "I":
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 3, row * GRID_SIZE + 20, 12, 12, block[row][col])
                    else:
                        pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 9, row * GRID_SIZE + 25, 12, 12, block[row][col])

    # def draw_hold(self, mino):
    #     block = mino["block"][0]
    #     shape = mino["shape"]

    #     for row in range(4):
    #         for col in range(4):
    #             if block[row][col] != 0:
    #                 if shape == "S" or shape == "Z":
    #                     pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 8, row * GRID_SIZE + 18 + GRID_SIZE, 12, 12, block[row][col])
    #                 elif shape == "O":
    #                     pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 3, row * GRID_SIZE + 18 + GRID_SIZE, 12, 12, block[row][col])
    #                 elif shape == "I":
    #                     pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 3, row * GRID_SIZE + 20, 12, 12, block[row][col])
    #                 else:
    #                     pyxel.rect(col * GRID_SIZE + (WINDOWWIDTH / 2) + 8, row * GRID_SIZE + 18, 12, 12, block[row][col])
                    
    def detect_collision(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:

                    if row + y + 1 > 18:
                        return True
                    elif self.board[row + y + 1][col + x] != 0 and self.board[row + y + 1][col + x] != 1:
                        return True
        return False

    # Fixes the block in the current position and adds to the board
    def fix_block(self, x, y, mino, orientation):
        block = mino["block"][orientation]

        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    self.board[row + y][col + x] = block[row][col]

    def clear_lines(self):
        lines_to_clear = []
        for index, row in enumerate(range(20)):
            if self.board[row].count(0) == 0:
                lines_to_clear.append(index)

        if len(lines_to_clear) > 0:
            for index in range(len(lines_to_clear)):
                self.board.pop(lines_to_clear[index])
                self.board.insert(2, [0] * BOARDWIDTH)
            
            self.cleared_lines = len(lines_to_clear)
            self.consecutive_clears += 1
            return True
        else:
            self.consecutive_clears = -1
            return False
        
class Move:
    def __init__(self, x, y, orientation, mino, board):
        self.mino = mino
        self.board = board
        self.x = x
        self.y = y
        self.orientation = orientation

    def move_left(self):
        if not self.left_collision(self.mino, self.x, self.y, self.orientation):
            self.x -= 1
            return self.x
        pyxel.play(3, 5, loop=False)
        return self.x

    def move_right(self):
        if not self.right_collision(self.mino, self.x, self.y, self.orientation):
            self.x += 1
            return self.x
        pyxel.play(3, 5, loop=False)
        return self.x

    def move_down(self):
        if not self.bottom_collision(self.mino, self.x, self.y, self.orientation):
            self.y += 1
            return self.y
        pyxel.play(3, 5, loop=False)
        return self.y

    def hard_drop(self):
        while not self.bottom_collision(self.mino, self.x, self.y, self.orientation):
            self.y += 1
        return self.y

    def rotate_right(self):
        if self.orientation == 3:
            self.orientation = 0
            return self.orientation
        else:
            self.orientation += 1
            return self.orientation
    
    def rotate_left(self):
        if self.orientation == 0:
            self.orientation = 3
            return self.orientation
        else:
            self.orientation -= 1
            return self.orientation

    def bottom_collision(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):

                if block[row][col] != 0:
                    if row + y + 1 > 18:
                        return True

                    if self.board[row + y + 1][col + x] != 0:
                        return True
        return False

    def left_collision(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):

                if block[row][col] != 0:
                    if col + x - 1 < 0:
                        return True
                    elif self.board[row + y][col + x - 1] != 0:
                        return True
        return False

    def right_collision(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]

        for row in range(4):
            for col in range(4):

                if block[row][col] != 0:
                    if col + x + 1 > BOARDWIDTH - 1:
                        return True
                    elif self.board[row + y][col + x + 1] != 0:
                        return True
        return False

    def can_rotate(self, mino, x, y, orientation):
        block = mino.mino["block"][orientation]
        
        for row in range(4):
            for col in range(4):
                if block[row][col] != 0:
                    if row + y > 18 or col + x < 0 or col + x > BOARDWIDTH - 1:
                        return False
                    
                    elif self.board[row + y][col + x] != 0:
                        return False
        return True

class Scores:
    def __init__(self):
        self.score = SCORE
        self.level = LEVEL
        self.lines = LINES
        self.combos = COMBOS
        self.spins = SPINS
        self.spin_type = ""
        self.score_type = ""
        self.fall_speed = FALL_SPEED
    
    def points(self, cleared_lines, combos, x, y, mino, orientation, board, rotated):
        score = 0
        if cleared_lines != 0:
            self.lines += cleared_lines
            if self.check_combo_count(combos):
                self.score_type = "COMBO!"
                if self.check_t_spins(x, y, mino, orientation, board, rotated):
                    if cleared_lines == 1:
                        score += T_SPIN["double"] * self.level  # B2B single is the same as double
                        self.spin_type = "BACK2BACK T-SPIN SINGLE!"
                    elif cleared_lines == 2:
                        score += T_SPIN["B2B double"] * self.level
                        self.spin_type = "BACK2BACK T-SPIN DOUBLE!"
                    elif cleared_lines == 3:
                        score += T_SPIN["B2B triple"] * self.level
                        self.spin_type = "BACK2BACK T-SPIN TRIPLE!"
                    return score
                else:
                    multiplier = (cleared_lines * self.level) + (50 * self.level)
                    score += POINTS[str(cleared_lines)] * (self.level + 1) + multiplier
                    return score

            elif self.check_t_spins(x, y, mino, orientation, board, rotated):
                if cleared_lines == 1:
                    score += T_SPIN["single"] * self.level
                    self.spin_type = "T-SPIN SINGLE!"
                elif cleared_lines == 2:
                    score += T_SPIN["double"] * self.level
                    self.spin_type = "T-SPIN DOUBLE!"
                elif cleared_lines == 3:
                    score += T_SPIN["triple"] * self.level
                    self.spin_type = "T-SPIN TRIPLE!"
                return score
            else:
                score += POINTS[str(cleared_lines)] * (self.level + 1)
                if cleared_lines == 4:
                    self.score_type = "TETRIS!"
                return score
        elif self.check_t_spins(x, y, mino, orientation, board, rotated):
            score += T_SPIN["mini"] * self.level
            self.spin_type = "MINI!"
            return score
        else:
            return score

    def check_combo_count(self, combo_count):
        if combo_count > 0:
            self.combos += combo_count
            return True
        return False

    def check_t_spins(self, x, y, mino, orientation, board, rotated):
        block = mino["block"][orientation]
        shape = mino["shape"]
        adjacent_blocks_occupied = 0
        
        if rotated and shape == "T":
            for row in range(4):
                for col in range(4):
                    if block[row][col] != 0:
                        if row == mino["centre"][0] and col == mino["centre"][1]:
                            try:
                                if board[row - 1 + y][col - 1 + x] != 0:
                                    adjacent_blocks_occupied += 1
                                
                                if board[row - 1 + y][col + 1 + x] != 0:
                                    adjacent_blocks_occupied += 1

                                if board[row + 1 + y][col - 1 + x] !=0:
                                    adjacent_blocks_occupied += 1
                                
                                if board[row + 1 + y][col + 1 + x] != 0:
                                    adjacent_blocks_occupied += 1
                            except IndexError:
                                adjacent_blocks_occupied += 1
            if adjacent_blocks_occupied >= 3:
                self.spins += 1
                return True
        else:
            return False

    def can_level_up(self, lines, level):
        return lines > level * 5

class Tetris:  
    def __init__(self):
        pyxel.init(WINDOWWIDTH, WINDOWHEIGHT, caption="Tetris", fps=60)
        self.reset()
        pyxel.load("assets/sounds.pyxres", image=True, sound=True)
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.state = "running"
        self.scene = TITLE_SCENE
        self.set_up = True
        self.randomizer = RANDOMIZER
        self.select_randomizer = False
        self.select_speed = False
        self.is_gameover = False
        self.first_spawn = True
        self.levelup = ""
        self.rotated = False
        # self.hold = False
        self.cleared = False
        self.lock_delay = LOCK_DELAY
        
        self.s = Scores()
        self.level = self.s.level
        self.score = self.s.score
        self.lines = self.s.lines
        self.combos = self.s.combos
        self.spins = self.s.spins
        self.fall_speed = self.s.fall_speed

    def setup(self):
        if self.randomizer["tetris 1985"]:
            print("85")
            self.bag = self.tetris_setting()
            self.t = next(self.bag)
            self.next = next(self.bag)
        elif self.randomizer["tetris nintendo"]:
            print("nin")
            self.bag = self.nintendo_setting()
            self.t = next(self.bag)
            self.next = next(self.bag)
        elif self.randomizer["tetris grand master"]:
            print("tgm")
            self.bag = self.tgm3_setting()
            self.t = Tetromino(next(self.bag))
            self.next = Tetromino(next(self.bag))
        elif self.randomizer["tetris worlds"]:
            print("worlds")
            self.bag = self.tetris_worlds_setting()
            self.t = self.bag.pop()
            self.next = self.bag.pop()

        self.b = Board(BOARDWIDTH, BOARDHEIGHT)
        self.last_mino = None
        self.last_x = None
        self.last_y = None
        # self.hold_mino = None 
        
        self.x = self.t.x
        self.y = self.t.y
        self.orientation = self.t.current_orientation

        self.board = self.b.board
        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)
        self.set_up = False

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.state == "running" or self.state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()
        
        if pyxel.btn(pyxel.KEY_P):
            if self.state == "running" and not self.is_gameover and self.scene == GAME_SCENE:
                self.state = "paused"
                pyxel.playm(4, loop=False)
            else:
                self.state = "running"
        
        if self.state == "running":
            if self.scene == TITLE_SCENE:
                
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2) and 88 <= pyxel.mouse_x <= 156 and 124 <= pyxel.mouse_y <= 134:
                    pyxel.play(1, 9, loop=False)
                    self.select_randomizer = True

                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2) and 98 <= pyxel.mouse_x <= 150 and 99 <= pyxel.mouse_y <= 109:
                    pyxel.play(1, 9, loop=False)
                    self.select_speed = True

                if self.select_speed:
                    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2) and 63 <= pyxel.mouse_x <= 73 and 118 <= pyxel.mouse_y <= 134:
                        self.fall_speed -= 1
                        pyxel.play(3, 1, loop=False)
                        if self.fall_speed < 1:
                            self.fall_speed = 1
                    
                    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2) and 182 <= pyxel.mouse_x <= 192 and 118 <= pyxel.mouse_y <= 134:
                        self.fall_speed += 1
                        pyxel.play(3, 1, loop=False)
                        if self.fall_speed > 20:
                            self.fall_speed = 20

                    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2) and 114 <= pyxel.mouse_x <= 139 and 165 <= pyxel.mouse_y <= 173:
                        pyxel.play(1, 9, loop=False)
                        self.select_speed = False

                if self.select_randomizer:
                    if 106 <= pyxel.mouse_x <= 152 and 49 <= pyxel.mouse_y <= 55:
                        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2):
                            pyxel.play(1, 9, loop=False)
                            self.randomizer = self.randomizer.fromkeys(self.randomizer, False)
                            self.randomizer["tetris 1985"] = True
                            self.select_randomizer = False
                    elif 98 <= pyxel.mouse_x <= 159 and 100 <= pyxel.mouse_y <= 108:
                        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2):
                            pyxel.play(1, 9, loop=False)
                            self.randomizer = self.randomizer.fromkeys(self.randomizer, False)
                            self.randomizer["tetris nintendo"] = True
                            self.select_randomizer = False
                    elif 92 <= pyxel.mouse_x <= 167 and 150 <= pyxel.mouse_y <= 158:
                        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2):
                            pyxel.play(1, 9, loop=False)
                            self.randomizer = self.randomizer.fromkeys(self.randomizer, False)
                            self.randomizer["tetris grand master"] = True
                            self.select_randomizer = False
                    elif 100 <= pyxel.mouse_x <= 154 and 201 <= pyxel.mouse_y <= 208:
                        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2):
                            pyxel.play(1, 9, loop=False)
                            self.randomizer = self.randomizer.fromkeys(self.randomizer, False)
                            self.randomizer["tetris worlds"] = True
                            self.select_randomizer = False
                
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 10, 2) and 66 <= pyxel.mouse_x <= 190 and 150 <= pyxel.mouse_y <= 160:
                    self.scene = GAME_SCENE

                elif pyxel.btnp(pyxel.KEY_ENTER, 10, 2):
                    self.scene = GAME_SCENE

            if self.scene == GAME_SCENE:        
                if pyxel.frame_count % int(60 / self.fall_speed) == 0:
                    if not self.b.detect_collision(self.x, self.y, self.t.mino, self.orientation):
                        self.y += 1
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)
                    else:
                        if pyxel.frame_count % self.lock_delay == 0:
                            self.b.fix_block(self.x, self.y, self.t.mino, self.orientation)
                            pyxel.play(2, 10, loop=False)
                            self.b.grid = deepcopy(self.b.board)
                            if self.check_game_over():
                                self.is_gameover = True
                                self.state = "stopped"
                                self.scene = GAMEOVER_SCENE
                            self.add_scores()
                            self.generate_new_block()

                if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                    if self.y > -1:
                        self.move = Move(self.x, self.y, self.orientation, self.t, self.board)
                        self.x = self.move.move_left()
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)

                if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                    if self.y > -1:
                        self.move = Move(self.x, self.y, self.orientation, self.t, self.board)
                        self.x = self.move.move_right()
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)

                if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                    if self.y > -1:
                        self.move = Move(self.x, self.y, self.orientation, self.t, self.board)
                        self.y = self.move.move_down()
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)
                         
                        if pyxel.frame_count % self.lock_delay == 0:
                            if self.b.detect_collision(self.x, self.y, self.t.mino, self.orientation):
                                self.b.fix_block(self.x, self.y, self.t.mino, self.orientation)
                                self.b.grid = deepcopy(self.b.board)
                                if self.check_game_over():
                                    self.is_gameover = True
                                    self.state = "stopped"
                                    self.scene = GAMEOVER_SCENE
                                self.add_scores()
                                self.generate_new_block( )

                if pyxel.btn(pyxel.KEY_SPACE):
                    if self.y > -1:
                        self.move = Move(self.x, self.y, self.orientation, self.t, self.board)
                        self.y = self.move.hard_drop()
                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)
                        pyxel.playm(2, loop=False)
                        if pyxel.frame_count % self.lock_delay == 0:
                            if self.b.detect_collision(self.x, self.y, self.t.mino, self.orientation):
                                self.b.fix_block(self.x, self.y, self.t.mino, self.orientation)
                                self.b.grid = deepcopy(self.b.board)
                                if self.check_game_over():
                                    self.is_gameover = True
                                    self.state = "stopped"
                                    self.scene = GAMEOVER_SCENE
                                self.add_scores()
                                self.generate_new_block()

                if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                    if self.y > -1:
                        self.move = Move(self.x, self.y, self.orientation, self.t, self.board)
                        self.orientation = self.move.rotate_right()
                        self.rotated = True

                        if not self.move.can_rotate(self.t, self.x, self.y, self.orientation):
                            wallkicks = self.t.wallkicks[:4]
                            for x, y in wallkicks[self.orientation]:
                                if self.move.can_rotate(self.t, self.x + x, self.y + y, self.orientation):
                                    self.x += x
                                    self.y += y
                                    self.rotated = True
                                    break
                            else:
                                self.orientation -= 1 if self.orientation > 0 else -3
                                self.rotated = False

                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)

                if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                    if self.y > -1:
                        self.move = Move(self.x, self.y, self.orientation, self.t, self.board)
                        self.orientation = self.move.rotate_left()
                        self.rotated = True
                        if not self.move.can_rotate(self.t, self.x, self.y, self.orientation):
                            wallkicks = self.t.wallkicks[4:]
                            for x, y in wallkicks[self.orientation]:
                                if self.move.can_rotate(self.t, self.x + x, self.y + y, self.orientation):
                                    self.x += x
                                    self.y += y
                                    self.rotated = True
                                    break
                            else:
                                self.orientation += 1 if self.orientation < 3 else -3
                                self.rotated = False

                        self.b.grid = deepcopy(self.b.board)
                        self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)

                # if pyxel.btnp(pyxel.KEY_C, 10, 2):
                #     if self.hold_mino == None:
                #         self.hold_mino = self.t.mino
                #         self.t.mino = self.next.mino
                #         self.next = Tetromino(BAG[random.randint(0, 6)])
                #         self.next_block = self.next.block
                #     else:
                #         self.hold_mino, self.t.mino = self.t.mino, self.hold_mino
                #     self.x = self.t.x
                #     self.y = self.t.y
                #     self.orientation = self.t.current_orientation
                #     self.hold = True
                #     self.b.drop_block(self.x, self.y, self.t.mino, self.orientation)
                #     self.b.grid = deepcopy(self.b.board)

    def draw(self):
        pyxel.cls(0)
        if self.scene == TITLE_SCENE:
            self.draw_title_screen()

            if self.select_randomizer:
                self.draw_select_randomizer()
            
            if self.select_speed:
                self.draw_select_speed()    
            # print(f"x: {pyxel.mouse_x}, y: {pyxel.mouse_y}")
            # print(self.randomizer)

        elif self.scene == GAME_SCENE:
            if self.set_up:
                self.setup()
            self.b.draw_next(self.next.mino)
            # if self.hold:
            #     self.b.draw_hold(self.hold_mino)
            self.b.draw_board()
            self.draw_grid()
            self.draw_borders()
            if self.s.spin_type:
                self.show_spin_type(self.s.spin_type, self.last_mino, self.last_x, self.last_y)
                if pyxel.frame_count % 480 == 0:
                    self.s.spin_type = ""
            
            if self.s.score_type:
                self.show_score_type(self.s.score_type)
                if pyxel.frame_count % 480  == 0:
                    self.s.score_type = ""
            
            if self.levelup:
                self.show_level_up(self.levelup)
                if pyxel.frame_count % 480 == 0:
                    self.levelup = ""

            self.text()
        elif self.scene == GAMEOVER_SCENE:
            self.draw_game_over_screen()

        if self.state == "paused":
            pyxel.cls(0)
            pyxel.text(WINDOWWIDTH // 2 - 20, WINDOWHEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 9)

    def draw_game_over_screen(self):
        pyxel.cls(0)
        pyxel.text(WINDOWWIDTH // 2 - 20, WINDOWHEIGHT // 2 - 12, "GAME OVER", pyxel.frame_count % 5)

    def draw_title_screen(self):
        pyxel.cls(0)
        pyxel.text(WINDOWWIDTH // 2 - 28, WINDOWHEIGHT // 2 - 50, "PYTHON TETRIS", 8)
        speed = pyxel.text(WINDOWWIDTH // 2 - 26, WINDOWHEIGHT // 2 - 25, "SELECT SPEED", 10)
        randomizer = pyxel.text(WINDOWWIDTH // 2 - 36, WINDOWHEIGHT // 2, "SELECT RANDOMIZER", 10)
        enter = pyxel.text(WINDOWWIDTH // 2 - 61, WINDOWHEIGHT // 2 + 25, "CLICK HERE/PRESS ENTER TO START", 6)

        if 98 <= pyxel.mouse_x <= 150 and 99 <= pyxel.mouse_y <= 109:
            speed = pyxel.text(WINDOWWIDTH // 2 - 26, WINDOWHEIGHT // 2 - 25, "SELECT SPEED", pyxel.frame_count % 10)

        if 88 <= pyxel.mouse_x <= 156 and 124 <= pyxel.mouse_y <= 134:
            randomizer = pyxel.text(WINDOWWIDTH // 2 - 36, WINDOWHEIGHT // 2, "SELECT RANDOMIZER", pyxel.frame_count % 10)

        if pyxel.frame_count % 15 == 0:
            enter = pyxel.text(WINDOWWIDTH // 2 - 61, WINDOWHEIGHT // 2 + 20, "CLICK HERE/PRESS ENTER TO START", 0)

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 16, 16)
    
    def draw_select_speed(self):
        pyxel.cls(0)

        pyxel.text(WINDOWWIDTH // 2 - 18, WINDOWHEIGHT // 2 - 40, "SET SPEED", 10)
        pyxel.text(WINDOWWIDTH // 2 - 3, WINDOWHEIGHT * 0.50, str(self.fall_speed), 6)
        select = pyxel.text(WINDOWWIDTH // 2 - 12, WINDOWHEIGHT // 2 + 40, "SELECT", 10)
        left_arrow = pyxel.blt(WINDOWWIDTH * 0.25, WINDOWHEIGHT * 0.50 - 8, 0, 0, 24, 10, 16)
        right_arrow = pyxel.blt(WINDOWWIDTH * 0.75 - 10, WINDOWHEIGHT * 0.50 - 8, 0, 22, 24, 10, 16)

        if 114 <= pyxel.mouse_x <= 139 and 165 <= pyxel.mouse_y <= 173:
            select = pyxel.text(WINDOWWIDTH // 2 - 12, WINDOWHEIGHT // 2 + 40, "SELECT", pyxel.frame_count % 10)


        if 63 <= pyxel.mouse_x <= 73 and 118 <= pyxel.mouse_y <= 134:
            left_arrow = pyxel.blt(WINDOWWIDTH * 0.25, WINDOWHEIGHT * 0.50 - 8, 0, 0, 48, 10, 16)

        if 182 <= pyxel.mouse_x <= 192 and 118 <= pyxel.mouse_y <= 134:
            right_arrow = pyxel.blt(WINDOWWIDTH * 0.75 - 10, WINDOWHEIGHT * 0.50 - 8, 0, 22, 48, 10, 16)

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 16, 16)    
        
    def draw_select_randomizer(self):
        pyxel.cls(0)
        t1985 = pyxel.text(WINDOWWIDTH // 2 - 20, WINDOWHEIGHT * 0.20, "TETRIS 1985", 10)
        tnin = pyxel.text(WINDOWWIDTH // 2 - 28, WINDOWHEIGHT * 0.40, "TETRIS NINTENDO", 10)
        tgm = pyxel.text(WINDOWWIDTH // 2 - 36, WINDOWHEIGHT * 0.60, "TETRIS GRAND MASTER", 10)
        tw = pyxel.text(WINDOWWIDTH // 2 - 25, WINDOWHEIGHT * 0.80, "TETRIS WORLDS", 10)

        if 106 <= pyxel.mouse_x <= 152 and 49 <= pyxel.mouse_y <= 55:
            t1985 = None
            pyxel.text(WINDOWWIDTH // 2 - 20, WINDOWHEIGHT * 0.20, "TETRIS 1985", pyxel.frame_count % 10)

        if 98 <= pyxel.mouse_x <= 159 and 100 <= pyxel.mouse_y <= 108:
            tnin = None
            pyxel.text(WINDOWWIDTH // 2 - 28, WINDOWHEIGHT * 0.40, "TETRIS NINTENDO", pyxel.frame_count % 10)

        if 92 <= pyxel.mouse_x <= 167 and 150 <= pyxel.mouse_y <= 158:
            tgm = None
            pyxel.text(WINDOWWIDTH // 2 - 36, WINDOWHEIGHT * 0.60, "TETRIS GRAND MASTER", pyxel.frame_count % 10)

        if 100 <= pyxel.mouse_x <= 154 and 201 <= pyxel.mouse_y <= 208:
            tw = None
            pyxel.text(WINDOWWIDTH // 2 - 25, WINDOWHEIGHT * 0.80, "TETRIS WORLDS", pyxel.frame_count % 10)

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 16, 16)

    def draw_borders(self):
        pyxel.rectb(4, 8, (BOARDWIDTH * GRID_SIZE) + 1, (19 * GRID_SIZE) + 1, 5)
        # pyxel.rectb((WINDOWWIDTH / 2) + 59, 16, 54, 48, 5)
        pyxel.rectb(WINDOWWIDTH / 2 , 16, 54, 48, 5)

    def draw_grid(self):
        for row in range(10):
            pyxel.line(4 + (GRID_SIZE * row), 8, 4 + (GRID_SIZE * row), (19 * GRID_SIZE) + 8, 13)
            pyxel.line(4, 8 + (GRID_SIZE * row), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * row), 13)
            pyxel.line(4, 8 + (GRID_SIZE * (row + 10)), 4 + (BOARDWIDTH * 12), 8 + (GRID_SIZE * (row + 10)), 13)

    def tetris_setting(self):
        bag = BAG
        while True:
            yield Tetromino(bag[random.randint(0, 6)])

    def nintendo_setting(self):
        bag = BAG
        history = None
        
        while True:
            mino = bag[random.randint(0, 6)]
            if mino == history:
                mino = bag[random.randint(0, 6)]
            history = mino
            yield Tetromino(mino)

    def tgm3_setting(self):
        pieces = [0, 1, 2, 3, 4, 5, 6]
        order = []

        pool = pieces * 5

        # First piece special conditions
        first = [3, 4, 5, 6][random.randint(0, 3)]
        yield first
        history = [2, 1, 2, first]

        while True:
            for i in range(6):
                rand = random.randint(0, 34)
                mino = pool[rand]
                if mino not in history or i == 5:
                    break
                
                if order:
                    pool[rand] = order[0]
            if mino in order:
                order.insert(1, order.index(mino))
                order = order[1:]
            order.append(mino)
            pool[rand] = order[0]

            history.pop(0)
            history.append(mino)
            yield mino
    
    def tetris_worlds_setting(self):
        bag = [Tetromino(0), Tetromino(1), Tetromino(2), Tetromino(3), Tetromino(4), Tetromino(5), Tetromino(6)]
        random.shuffle(bag)
        return bag

    def generate_new_block(self):
        if self.t.index == 5:
            self.last_mino = self.t
            self.last_x = self.x
            self.last_y = self.y
        self.orientation = self.t.current_orientation
        if self.randomizer["tetris 1985"]:
            self.bag = self.tetris_setting()
            self.x = self.t.x
            self.y = self.t.y
            self.t = self.next
            self.next = next(self.bag)
        elif self.randomizer["tetris nintendo"]:
            self.bag = self.nintendo_setting()
            self.x = self.t.x
            self.y = self.t.y
            self.t = self.next
            self.next = next(self.bag)
        elif self.randomizer["tetris grand master"]:
            self.bag = self.tgm3_setting()
            self.x = self.t.x
            self.y = self.t.y
            self.t = self.next
            self.next = Tetromino(next(self.bag))
        elif self.randomizer["tetris worlds"]:
            if len(self.bag) == 0:
                self.bag = self.tetris_worlds_setting()
                self.x = self.t.x
                self.y = self.t.y
                self.t = self.next
                self.next = self.bag.pop()
            else:   
                self.x = self.t.x
                self.y = self.t.y
                self.t = self.next
                self.next = self.bag.pop()

    def add_scores(self):
        if self.b.clear_lines():
            self.cleared = True
            pyxel.playm(0, loop=False)
        
        if self.cleared:
            self.combos += 1 if self.b.consecutive_clears > 0 else 0
            self.score += self.s.points(self.b.cleared_lines, self.b.consecutive_clears, self.x, self.y, self.t.mino, self.orientation, self.b.grid, self.rotated)
            self.lines += self.b.cleared_lines
            if self.b.cleared_lines == 4:
                pyxel.playm(3, loop=False)

            if self.s.can_level_up(self.lines, self.level):
                self.level += 1
                self.fall_speed += 1
                self.levelup = f"LEVEL {self.level}!"
                pyxel.playm(6, loop=False)

        elif self.s.check_t_spins(self.x, self.y, self.t.mino, self.orientation, self.b.grid, self.rotated): 
            self.score += self.s.points(0, self.b.consecutive_clears, self.x, self.y, self.t.mino, self.orientation, self.b.grid, self.rotated)
            self.spins += self.s.spins
            if self.s.spin_type:   
                pyxel.playm(5, loop=False)

        self.rotated = False
        self.cleared = False
    
    def check_game_over(self):
        return self.b.detect_collision(self.x, self.y, self.t.mino, self.orientation) if self.y < 0 else False

    def show_spin_type(self, text, mino, x, y):
        if mino != None:
            for row in range(4):
                for col in range(4):
                    if row == mino.mino["centre"][1] and col == mino.mino["centre"][0]:
                        pyxel.text(col * GRID_SIZE + (x * GRID_SIZE), row * GRID_SIZE + (y * GRID_SIZE), text, 7)
                        break
    
    def show_score_type(self, text):
        if text == "COMBO!":
            pyxel.text(WINDOWWIDTH / 2 + 50, 100, text, pyxel.frame_count % 7)
        else:
            pyxel.text(WINDOWWIDTH / 2 + 50, 90, text, pyxel.frame_count % 7)
    
    def show_level_up(self, text):
        pyxel.text(WINDOWWIDTH / 2 + 50, 80, text, pyxel.frame_count % 7)

    def text(self):
        pyxel.FONT_HEIGHT = 12
        pyxel.FONT_WIDTH = 10
        # pyxel.text(WINDOWWIDTH / 2 + 1, 9, "HOLD: ", 10)
        pyxel.text(WINDOWWIDTH / 2 + 1, 9, "NEXT: ", 10)
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