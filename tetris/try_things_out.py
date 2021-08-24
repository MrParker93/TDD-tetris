import pyxel
import random
import constants

FALL_SPEED = 10


class Tetris:
    def __init__(self):
        pyxel.init(120, 220, caption="Tetris", fps=50)
        self.reset()
        pyxel.load("assets/shapes.pyxres")
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.piece = Pieces()
        self.board = Board()
        self.level = 0
        self.score = 0
        self.lines = 0
        self.combos = 0
        self.is_gameover = False
        self.game_state = "running"
        self.direction = None

    def update(self):
        if pyxel.btn(pyxel.KEY_Q) or self.is_gameover == True:
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_P, 5, 2):
            if self.game_state == "running":
                self.game_state = "paused"
            else:
                self.game_state = "running"

        if self.game_state == "running":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()

            if pyxel.frame_count % FALL_SPEED == 0:
                self.piece.block_falling()

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                self.direction = "DOWN"
                self.piece.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_LEFT, 10, 2):
                self.direction = "LEFT"
                self.piece.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_RIGHT, 10, 2):
                self.direction = "RIGHT"
                self.piece.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_SPACE, 10, 2):
                self.direction = "SPACE"
                self.piece.move_block(self.direction)

            elif pyxel.btnp(pyxel.KEY_Z, 10, 2):
                self.direction = "R_LEFT"

            elif pyxel.btnp(pyxel.KEY_X, 10, 2):
                self.direction = "R_RIGHT"

    def draw(self):
        pyxel.cls(0)
        self.board.draw_border()
        self.board.draw_block()
        self.piece.draw_block()
        self.Text.show_text(self)

        if self.game_state == "paused":
            pyxel.text(50, 100, "PAUSED", pyxel.frame_count % 16)

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
        pyxel.rectb(4, 8, 10 * 8, 22 * 8, 5)

        # Show next block
        pyxel.rectb(87, 16, 30, 48, 5)

    def draw_block(self):
        for row in range(22):
            for col in range(10):
                if self.board[row][col] != 0:
                    pyxel.blt(col * 8, row * 8, 0, 0,
                              self.board[row][col], 8, 8)


class Pieces(Board):
    def __init__(self):
        super().__init__()
        self.generate_block()

    def block_falling(self):
        for row in reversed(range(0, 22)):
            self.board[row] = self.board[row - 1]

        self.board[0] = [0 for x in range(10)]

    def generate_block(self):
        block = random.choice(
            [val for val in constants.PYXRES_VALUES.values()])

        if block == 8:  # O Block
            self.board[0][5] = 8
            self.board[0][4] = 8
            self.board[1][5] = 8
            self.board[1][4] = 8

        elif block == 24:  # L Block
            self.board[0][5] = 24
            self.board[1][5] = 24
            self.board[2][5] = 24
            self.board[2][6] = 24

        elif block == 72:  # J Block
            self.board[0][6] = 72
            self.board[0][5] = 72
            self.board[1][5] = 72
            self.board[2][5] = 72

        elif block == 88:  # I Block
            self.board[0][5] = 88
            self.board[1][5] = 88
            self.board[2][5] = 88
            self.board[3][5] = 88

        elif block == 128:  # T Block
            self.board[0][5] = 128
            self.board[1][5] = 128
            self.board[1][6] = 128
            self.board[2][5] = 128

        elif block == 160:  # Z Block
            self.board[0][5] = 160
            self.board[1][5] = 160
            self.board[1][4] = 160
            self.board[2][4] = 160

        else:  # S Block
            self.board[0][5] = 192
            self.board[1][5] = 192
            self.board[1][6] = 192
            self.board[2][6] = 192

    def move_block(self, direction):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    if direction == "RIGHT":
                        self.board[row][col] = self.board[row][col + 1]

                    if direction == "LEFT":
                        self.board[row][col] = self.board[row][col - 1]

                    if direction == "DOWN":
                        self.board[row][col] = self.board[col + 1]

        # blocks = [
        #     # O block
        #     [
        #         [8, 8],
        #         [8, 8]
        #     ],

        #     # I block
        #     [
        #         [0, 0, 0, 0],
        #         [88, 88, 88, 88],
        #         [0, 0, 0, 0],
        #         [0, 0, 0, 0]
        #     ],

        #     # S block
        #     [
        #         [0, 192, 192],
        #         [192, 192, 0],
        #         [0, 0, 0],
        #     ],

        #     # Z block
        #     [
        #         [160, 160, 0],
        #         [0, 160, 160],
        #         [0, 0, 0]
        #     ],

        #     # L block
        #     [
        #         [24, 0, 0],
        #         [24, 0, 0],
        #         [24, 24, 0],
        #     ],

        #     # J block
        #     [
        #         [0, 72, 0],
        #         [0, 72, 0],
        #         [72, 72, 0],
        #     ],

        #     # T block
        #     [
        #         [0, 128, 0],
        #         [128, 128, 128],
        #         [0, 0, 0]
        #     ]
        # ]

        # return blocks[block]


if __name__ == "__main__":
    Tetris()
