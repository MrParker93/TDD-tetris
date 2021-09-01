import time
import pyxel
import random
import pprint

FALL_SPEED = 10
CURRENT_PIECE = None

class Tetris:
    def __init__(self):
        pyxel.init(120, 220, caption="Tetris", fps=50)
        self.reset()
        pyxel.load("assets/shapes.pyxres")
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.level = 0
        self.score = 0
        self.lines = 0
        self.combos = 0
        self.is_gameover = False
        self.game_state = "running"
        self.current_piece = self.generate_block()
        self.next_piece = self.generate_block()
        self.board = Board()
        self.piece = Pieces(self.current_piece, self.next_piece)
        self.direction = None
        self.rotation = None

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_P):
            if self.game_state == "running" and not self.is_gameover:
                self.game_state = "paused"
            else:
                self.game_state = "running"
        
        if self.game_state == "running" or self.game_state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()

        if self.game_state == "running":

            if pyxel.frame_count % FALL_SPEED == 0:
                self.piece.block_falling()
                self.check_vertical_collisions()

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                self.direction = "DOWN"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                self.direction = "LEFT"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                self.direction = "RIGHT"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_SPACE, 10, 2):
                self.direction = "SPACE"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.rotation = "ACW"
                rotated_piece = self.rotate_anticlockwise(self.current_piece)
                self.current_piece = rotated_piece

            elif pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.rotation = "CW"
                rotated_piece = self.rotate_clockwise(self.current_piece)
                self.current_piece = rotated_piece

    def draw(self):
        pyxel.cls(0)
        self.board.draw_border()
        self.board.draw_next_block()
        self.board.draw_block()
        self.piece.draw_block()
        self.piece.draw_next_block()
        self.Text.show_text(self)

        if self.game_state == "paused":
            pyxel.text(50, 100, "PAUSED", pyxel.frame_count % 16)
        
        if self.is_gameover:
            self.game_state = "stopped"
            pyxel.cls(0)
            pyxel.text(45, 95, "GAMEOVER", pyxel.frame_count % 16)
            pyxel.text(45, 110, "Score: ", 6)
            pyxel.text(75, 110, str(self.score), 10)
            pyxel.text(45, 120, "Level: ", 6)
            pyxel.text(75, 120, str(self.level), 10)
            pyxel.text(45, 130, "Combos: ", 6)
            pyxel.text(75, 130, str(self.combos), 10)
            pyxel.text(45, 140, "Lines: ", 6)
            pyxel.text(75, 140, str(self.lines), 10)

            pyxel.text(12, 196, "Q: ", 10)
            pyxel.text(24, 196, "QUIT", 6)
            pyxel.text(66, 196, "R: ", 10)
            pyxel.text(78, 196, "RESTART", 6)

    def rotate_clockwise(self, current_piece):
        current_piece = list(zip(*current_piece[::-1]))
        
        for i, row in enumerate(range(22)):
            if i < 10:
                if self.piece.board[row][i] != 0:
                    if self.piece.board[row][i] == 8:
                        pass

                    elif self.piece.board[row][i] == 88:
                        for ind, section in enumerate(current_piece):
                            self.piece.board[row][i - 2: i + 1] = section
                            print(section)

                    else:
                        for ind, section in enumerate(current_piece):
                            self.piece.board[row][i - 1: i + 1] = section
                            print(section)
        
        return current_piece

    def rotate_anticlockwise(self, current_piece):
        rotate_once = self.rotate_clockwise(current_piece)
        rotate_twice = self.rotate_clockwise(rotate_once)
        anticlockwise_piece = self.rotate_clockwise(rotate_twice)
        current_piece = anticlockwise_piece
        return current_piece

    def move_block(self, direction):
        if direction == None:
            return
        
        if direction == "DOWN":
            for row in reversed(range(22)):
                if not self.check_vertical_collisions():
                    if 1 < row < 22:
                        self.piece.board[row] = self.piece.board[row - 1]

        if direction == "RIGHT":
            for row in range(22):
                for col in reversed(range(9)):
                    if not self.check_horizontal_collisions(row, col, direction):
                        tmp = self.piece.board[row][col]
                        self.piece.board[row][col] = 0
                        self.piece.board[row][col + 1] += tmp
        
        if direction == "LEFT":
            for row in range(22):
                for col in range(10):
                    if not self.check_horizontal_collisions(row, col, direction):
                        tmp = self.piece.board[row][col]
                        self.piece.board[row][col] = 0
                        self.piece.board[row][col - 1] += tmp
        

    def check_vertical_collisions(self):
        for row in range(22):
            for col in range(10):
                if self.piece.board[row][col] != 0 and self.board.board[1][col] != 0:
                    self.is_gameover = True

                if self.piece.board[row][col] != 0 and self.board.board[row + 1][col] != 0:
                    self.add_block_to_board()
                    self.current_piece = self.next_piece
                    self.next_piece = self.generate_block()
                    self.piece = Pieces(self.current_piece, self.next_piece)
                    return True
                    
                elif self.piece.board[21][col] != 0 and self.board.board[21][col] == 0:
                    self.add_block_to_board()
                    self.current_piece = self.next_piece
                    self.next_piece = self.generate_block()
                    self.piece = Pieces(self.current_piece, self.next_piece)
                    return True

        return False

    def check_horizontal_collisions(self, row, col, direction):
        if direction == "RIGHT":
            if self.piece.board[row][9] != 0:
                return True

            elif self.piece.board[row][col] != 0 and self.board.board[row][col + 1] != 0:
                return True
                    
        elif direction == "LEFT":
            if self.piece.board[row][1] != 0:
                return True

            elif self.piece.board[row][col] != 0 and self.board.board[row][col - 1] != 0:
                return True

        return False

    def add_block_to_board(self):
        for row in range(22):
            for col in range(10):
                if self.piece.board[row][col] != 0:
                    self.board.board[row][col] = self.piece.board[row][col]
        
    def generate_block(self):
        block = random.choice([_ for _ in range(7)])

        blocks = [
            # O block
            [
                [8, 8],
                [8, 8]
            ],

            # I block
            [
                [0, 0, 0, 0],
                [88, 88, 88, 88],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],

            # S block
            [
                [0, 192, 192],
                [192, 192, 0],
                [0, 0, 0],
            ],

            # Z block
            [
                [160, 160, 0],
                [0, 160, 160],
                [0, 0, 0]
            ],

            # L block
            [
                [0, 0, 24],
                [24, 24, 24],
                [0, 0, 0],
            ],

            # J block
            [
                [72, 72, 72],
                [0, 0, 72],
                [0, 0, 0],
            ],

            # T block
            [
                [0, 128, 0],
                [128, 128, 128],
                [0, 0, 0]
            ]
        ]

        return blocks[block]


    class Text:
        def __init__(self):
            super().__init__()
            
        def show_text(self):
            pyxel.text(87, 8, "NEXT: ", 10)
            pyxel.text(87, 72, "LEVEL", 10)
            pyxel.text(87, 80, str(self.level), 6)
            pyxel.text(87, 96, "SCORE", 10)
            pyxel.text(87, 104, str(self.score), 6)
            pyxel.text(87, 120, "LINES", 10)
            pyxel.text(87, 128, str(self.lines), 6)
            pyxel.text(87, 146, "COMBOS", 10)
            pyxel.text(87, 154, str(self.combos), 6)
            pyxel.text(4, 196, "Q: ", 10)
            pyxel.text(12, 196, "QUIT", 6)
            pyxel.text(40, 196, "P: ", 10)
            pyxel.text(48, 196, "PAUSE", 6)
            pyxel.text(76, 196, "R: ", 10)
            pyxel.text(84, 196, "RESTART", 6)


class Board:
    def __init__(self):
        self.board = [[0] * 10 for _ in range(22)]
        self.next_piece_board = [[0] * 4 for _ in range(6)]
        
    def draw_border(self):
        # Main area for gameplay
        pyxel.rectb(4, 8, 10 * 8, 22 * 7.8, 5)

        # Show next block
        pyxel.rectb(87, 16, 30, 6 * 8, 5)

    def draw_block(self):
        for row in range(22):
            for col in range(10):
                if self.board[row][col] != 0:
                    pyxel.blt(col * 8, row * 8, 0, 0,
                            self.board[row][col], 8, 8)

    def draw_next_block(self):
        for row in range(6):
            for col in range(3):
                if self.next_piece_board[row][col] != 0:
                    if self.next_piece_board[row][col] == 8:
                        pyxel.blt((col * 8) + 95, (row * 8) + 40, 0, 0, self.next_piece_board[row][col], 8, 8)
                    elif self.next_piece_board[row][col] == 88:
                        pyxel.blt((col * 8) + 82, (row * 8) + 24, 0, 0, self.next_piece_board[row][col], 8, 8)
                    else:
                        pyxel.blt((col * 8) + 87, (row * 8) + 32, 0, 0, self.next_piece_board[row][col], 8, 8)
        

class Pieces(Board):
    def __init__(self, piece, next_piece):
        super().__init__()
        self.piece = piece
        self.next_piece = next_piece
        self.insert_block_in_board()
        self.insert_next_block()

    def block_falling(self):
        for row in reversed(range(0, 22)):
            self.board[row] = self.board[row - 1]
        self.board[0] = [0 for x in range(10)]

    def insert_block_in_board(self):
        for each_row in self.piece:
            for index, section in enumerate(each_row):
                self.board[index].pop()
                self.board[index].insert(3, section)
    
    def insert_next_block(self):
        for each_row in self.next_piece:
            for index, section in enumerate(each_row):
                self.next_piece_board[index].pop()
                self.next_piece_board[index].insert(0, section)

if __name__ == "__main__":
    Tetris()
