import pyxel
import random
import constants
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
        self.board = Board()
        self.piece = Pieces(self.current_piece)
        self.direction = None
        self.rotation = None

    def update(self):
        if pyxel.btn(pyxel.KEY_Q) or self.is_gameover == True:
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_P):
            if self.game_state == "running":
                self.game_state = "paused"
            else:
                self.game_state = "running"
        
        if self.game_state == "running":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()

            if pyxel.frame_count % FALL_SPEED == 0:
                self.piece.block_falling()
                self.check_for_collisions(  )

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                self.direction = "DOWN"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_LEFT, 10, 2):
                self.direction = "LEFT"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_RIGHT, 10, 2):
                self.direction = "RIGHT"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_SPACE, 10, 2):
                self.direction = "SPACE"
                self.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_Z, 10, 2):
                self.rotation = "ACW"
                rotated_piece = self.rotate_anticlockwise(self.current_piece)
                self.current_piece = rotated_piece

            elif pyxel.btnp(pyxel.KEY_X, 10, 2):
                self.rotation = "CW"
                rotated_piece = self.rotate_clockwise(self.current_piece)
                self.current_piece = rotated_piece

    def draw(self):
        pyxel.cls(0)
        self.board.draw_border()
        self.board.draw_block()
        self.piece.draw_block()
        self.Text.show_text(self)

        if self.game_state == "paused":
            pyxel.text(50, 100, "PAUSED", pyxel.frame_count % 16)
            
    def rotate_clockwise(self, current_piece):
        current_piece = list(zip(*current_piece[::-1]))
        return current_piece
        
    def rotate_anticlockwise(self, current_piece):
        rotate_once = self.rotate_clockwise(current_piece)
        rotate_twice = self.rotate_clockwise(rotate_once)
        anticlockwise_piece = self.rotate_clockwise(rotate_twice)
        current_piece = anticlockwise_piece
        print(current_piece)
        return current_piece

    def move_block(self, direction):
        if direction == None:
            return
        
        if direction == "DOWN":
            for row in reversed(range(0, 22)):
                if row < 21:
                        self.piece.board[row] = self.piece.board[row - 1]
    
    def check_for_collisions(self):
        for row in range(22):
            for index, col in enumerate (range(10)):
                try:
                    if self.piece.board[row][col] != 0 and self.board.board[row + 1][col] != 0:
                        self.add_block_to_board()
                        new_piece = self.generate_block()
                        self.current_piece = new_piece
                        return True
                    
                    elif self.piece.board
                except IndexError as e:
                    pass
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
                [0, 24, 0],
                [0, 24, 0],
                [0, 24, 24],
            ],

            # J block
            [
                [0, 72, 0],
                [0, 72, 0],
                [72, 72, 0],
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
        
    def draw_border(self):
        # Main area for gameplay
        pyxel.rectb(4, 8, 10 * 8, 22 * 7.8, 5)

        # Show next block
        pyxel.rectb(87, 16, 30, 48, 5)

    def draw_block(self):
        for row in range(22):
            for col in range(10):
                if self.board[row][col] != 0:
                    pyxel.blt(col * 8, row * 8, 0, 0,
                            self.board[row][col], 8, 8)


class Pieces(Board):
    def __init__(self, piece):
        super().__init__()
        self.piece = piece
        self.insert_block_in_board()

    def block_falling(self):
        for row in reversed(range(0, 22)):
            self.board[row] = self.board[row - 1]

        self.board[0] = [0 for x in range(10)]

    def insert_block_in_board(self):
        for each_row in self.piece:
            for index, section in enumerate(each_row):
                self.board[index].pop()
                self.board[index].insert(3, section)


if __name__ == "__main__":
    Tetris()
