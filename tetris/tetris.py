import enum
import pyxel
import random
from functions import colours

#####################################
# SET GLOBAL VARIABLE GAME SETTINGS #
#####################################

SCREEN_WIDTH = 120
SCREEN_HEIGHT = 180

BACKGROUND_COLOUR = pyxel.COLOR_BLACK
BORDER_COLOUR = pyxel.COLOR_NAVY


# Direction shapes are facing
class Direction(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


# Shapes class draws the shape and handles various shapes depending on rotation


class Shape:
    """Shape class designs each shape needed for Tetris."""

    def __init__(self, x, y, l_shape=False, t_shape=False, o_shape=False, i_shape=False, z_shape=False, s_shape=False, l2_shape=False):
        self.x = x
        self.y = y

        # Width and height of the image drawn using PyxelEditor
        self.w = 8
        self.h = 8

        self.L_shape = l_shape
        self.T_shape = t_shape
        self.O_shape = o_shape
        self.I_shape = i_shape
        self.Z_shape = z_shape
        self.S_shape = s_shape
        self.L2_shape = l2_shape

    # Draw a single section of each shape to build them
    def draw(self):
        width = self.w
        height = self.h
        sprite_x = 0
        sprite_y = 0

        # Depending on the shape of the block, use a different colour
        if self.L_shape:
            sprite_x = 0
            sprite_y = 0

        if self.T_shape:
            sprite_x = 16
            sprite_y = 0

        if self.O_shape:
            sprite_x = 32
            sprite_y = 0

        if self.I_shape:
            sprite_x = 48
            sprite_y = 0

        if self.Z_shape:
            sprite_x = 0
            sprite_y = 16

        if self.S_shape:
            sprite_x = 16
            sprite_y = 16

        if self.L2_shape:
            sprite_x = 32
            sprite_y = 16

        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, width, height)


class Tetris:
    """Set up and run Tetris."""

    def __init__(self):
        """Initiate pyxel, set up game variables and run Tetris"""
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Tetris", fps=20)
        pyxel.load("assets/shapes.pyxres")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        """Resets score and starts a new game. Can reset manually using 'R' key."""
        self.direction = random.choice(
            [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP])
        self.lose = False
        self.score = str(0)

    #####################################
        # GAME LOGIC #
    #####################################

    def update(self):
        """
        Updates the logic of the game. Generates new shapes, checks for scoring/bonus/combo conditions and checks
        for losing conditions.
        """
        if not self.lose:
            self.rotate_shape()
            self.generate_shape()
            self.check_for_combos()
            self.check_for_loss()

        # Manually quit the game
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        # Manually reset the game
        if pyxel.btn(pyxel.KEY_R):
            self.reset()

    def generate_shape(self):
        """Generates random shapes after previous shape is used."""
        pass

    def rotate_shape(self):
        """Rotates shape clockwise depending on the current direction faced."""
        pass

    def check_for_combos(self):
        """
        Checks the game for consecutive clears, double, triple and tetris (4 row) clears and
        updates score accordingly.
        """
        pass

    def check_for_loss(self):
        """Checks the game for the losing condition."""
        pass

    #####################################
        # DRAW LOGIC #
    #####################################

    def draw(self):
        """Draw all shapes to be used for the game. Draw the border and scores and current level.
        """
        if not self.lose:

            pyxel.cls(BACKGROUND_COLOUR)
            pyxel.rectb(10, 5, 100, 140, BORDER_COLOUR)
            self.draw_shape(self.direction)
            self.draw_score_and_options()

            shape = [
                "L_shape",
                "T_shape",
                "O_shape",
                "I_shape",
                "Z_shape",
                "S_shape",
                "L2_shape"
            ]

            for shapes in self.shape:
                for key, value in shapes.items():
                    if "shape" in key:
                        for v in value:
                            v.draw()
        else:
            self.draw_lose()

    def draw_score_and_options(self):
        score_label = "SCORE :"
        score = self.score
        pyxel.text(30, 150, score_label, pyxel.COLOR_YELLOW)
        pyxel.text(75, 150, score, pyxel.COLOR_GRAY)

        quit_label = "Q :"
        quit_string = "Quit"
        pyxel.text(10, 165, quit_label, pyxel.COLOR_YELLOW)
        pyxel.text(30, 165, quit_string, pyxel.COLOR_GRAY)

        restart_label = "R :"
        restart_string = "Restart"
        pyxel.text(60, 165, restart_label, pyxel.COLOR_YELLOW)
        pyxel.text(80, 165, restart_string, pyxel.COLOR_GRAY)

    def draw_lose():
        pass

    def draw_shape(self, Direction):
        self.shape = []

        L_shape = T_shape = O_shape = I_shape = Z_shape = S_shape = L2_shape = True

        for x, y in enumerate(range(1)):

            if L_shape:
                if Direction == Direction.RIGHT:
                    self.shape.append({
                        "L_shape": [
                            Shape(x, y, l_shape=True),
                            Shape(x, y + 9, l_shape=True),
                            Shape(x, y + 18, l_shape=True),
                            Shape(x + 9, y + 18, l_shape=True)
                        ]
                    })

                if Direction == Direction.DOWN:
                    self.shape.append({
                        "L_shape": [
                            Shape(x, y, l_shape=True),
                            Shape(x + 9, y, l_shape=True),
                            Shape(x + 18, y, l_shape=True),
                            Shape(x, y + 9, l_shape=True)
                        ]
                    })

                if Direction == Direction.LEFT:
                    self.shape.append({
                        "L_shape": [
                            Shape(x, y, l_shape=True),
                            Shape(x + 9, y, l_shape=True),
                            Shape(x + 9, y + 9, l_shape=True),
                            Shape(x + 9, y + 18, l_shape=True)
                        ]
                    })

                if Direction == Direction.UP:
                    self.shape.append({
                        "L_shape": [
                            Shape(x, y + 9, l_shape=True),
                            Shape(x + 9, y + 9, l_shape=True),
                            Shape(x + 18, y + 9, l_shape=True),
                            Shape(x + 18, y, l_shape=True)
                        ]
                    })

            if T_shape:
                if Direction == Direction.RIGHT:
                    self.shape.append({
                        "T_shape": [
                            Shape(x, y, t_shape=True),
                            Shape(x, y + 9, t_shape=True),
                            Shape(x + 9, y + 9, t_shape=True),
                            Shape(x, y + 18, t_shape=True)
                        ]
                    })

                if Direction == Direction.DOWN:
                    self.shape.append({
                        "T_shape": [
                            Shape(x, y, t_shape=True),
                            Shape(x + 9, y, t_shape=True),
                            Shape(x + 18, y, t_shape=True),
                            Shape(x + 9, y + 9, t_shape=True)
                        ]
                    })

                if Direction == Direction.LEFT:
                    self.shape.append({
                        "T_shape": [
                            Shape(x, y + 9, t_shape=True),
                            Shape(x + 9, y + 9, t_shape=True),
                            Shape(x + 9, y + 18, t_shape=True),
                            Shape(x + 9, y, t_shape=True)
                        ]
                    })

                if Direction == Direction.UP:
                    self.shape.append({
                        "T_shape": [
                            Shape(x, y + 9, t_shape=True),
                            Shape(x + 9, y + 9, t_shape=True),
                            Shape(x + 18, y + 9, t_shape=True),
                            Shape(x + 9, y, t_shape=True)
                        ]
                    })

            if O_shape:
                if Direction:
                    self.shape.append({
                        "O_shape": [
                            Shape(x, y, o_shape=True),
                            Shape(x + 9, y, o_shape=True),
                            Shape(x, y + 9, o_shape=True),
                            Shape(x + 9, y + 9, o_shape=True)
                        ]
                    })

            if I_shape:
                if Direction == Direction.RIGHT or Direction == Direction.LEFT:
                    self.shape.append({
                        "I_shape": [
                            Shape(x, y, i_shape=True),
                            Shape(x, y + 9, i_shape=True),
                            Shape(x, y + 18, i_shape=True),
                            Shape(x, y + 27, i_shape=True)
                        ]
                    })

                if Direction == Direction.DOWN or Direction == Direction.UP:
                    self.shape.append({
                        "I_shape": [
                            Shape(x, y, i_shape=True),
                            Shape(x + 9, y, i_shape=True),
                            Shape(x + 18, y, i_shape=True),
                            Shape(x + 27, y, i_shape=True)
                        ]
                    })

            if Z_shape:
                if Direction == Direction.RIGHT or Direction == Direction.LEFT:
                    self.shape.append({
                        "Z_shape": [
                            Shape(x, y, z_shape=True),
                            Shape(x + 9, y, z_shape=True),
                            Shape(x + 9, y + 9, z_shape=True),
                            Shape(x + 18, y + 9, z_shape=True)
                        ]
                    })

                if Direction == Direction.DOWN or Direction == Direction.UP:
                    self.shape.append({
                        "Z_shape": [
                            Shape(x + 9, y, z_shape=True),
                            Shape(x + 9, y + 9, z_shape=True),
                            Shape(x, y + 9, z_shape=True),
                            Shape(x, y + 18, z_shape=True)
                        ]
                    })

            if S_shape:
                if Direction == Direction.RIGHT or Direction == Direction.LEFT:
                    self.shape.append({
                        "S_shape": [
                            Shape(x, y + 9, s_shape=True),
                            Shape(x + 9, y, s_shape=True),
                            Shape(x + 9, y + 9, s_shape=True),
                            Shape(x + 18, y, s_shape=True)
                        ]
                    })

                if Direction == Direction.DOWN or Direction == Direction.UP:
                    self.shape.append({
                        "S_shape": [
                            Shape(x, y, s_shape=True),
                            Shape(x + 9, y + 9, s_shape=True),
                            Shape(x, y + 9, s_shape=True),
                            Shape(x + 9, y + 18, s_shape=True)
                        ]
                    })

            if L2_shape:
                if Direction == Direction.RIGHT:
                    self.shape.append({
                        "L2_shape": [
                            Shape(x, y, l2_shape=True),
                            Shape(x + 9, y, l2_shape=True),
                            Shape(x, y + 9, l2_shape=True),
                            Shape(x, y + 18, l2_shape=True)
                        ]
                    })

                if Direction == Direction.DOWN:
                    self.shape.append({
                        "L2_shape": [
                            Shape(x, y, l2_shape=True),
                            Shape(x + 9, y, l2_shape=True),
                            Shape(x + 18, y, l2_shape=True),
                            Shape(x + 18, y + 9, l2_shape=True)
                        ]
                    })

                if Direction == Direction.LEFT:
                    self.shape.append({
                        "L2_shape": [
                            Shape(x, y + 18, l2_shape=True),
                            Shape(x + 9, y + 18, l2_shape=True),
                            Shape(x + 9, y + 9, l2_shape=True),
                            Shape(x + 9, y, l2_shape=True)
                        ]
                    })

                if Direction == Direction.UP:
                    self.shape.append({
                        "L2_shape": [
                            Shape(x + 18, y, l2_shape=True),
                            Shape(x + 18, y + 9, l2_shape=True),
                            Shape(x + 9, y + 9, l2_shape=True),
                            Shape(x, y + 9, l2_shape=True)
                        ]
                    })
        return self.shape

    @staticmethod
    def center_text(text, page_width, char_width=pyxel.FONT_WIDTH):
        """Helper function for calcuating the start x value for centered text."""

        text_width = len(text) * char_width
        return (page_width - text_width) // 2


Tetris()
