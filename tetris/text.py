import pyxel
from constants import *

class Text:
    def show_text(self):
        pyxel.text(87, 8, "NEXT: ", 10)
        pyxel.text(87, 72, "LEVEL", 10)
        pyxel.text(87, 80, str(STARTING_LEVEL), 6)
        pyxel.text(87, 96, "SCORE", 10)
        pyxel.text(87, 104, str(SCORE), 6)
        pyxel.text(87, 120, "LINES", 10)
        pyxel.text(87, 128, str(LINES), 6)
        pyxel.text(87, 146, "COMBOS", 10)
        pyxel.text(87, 154, str(COMBOS), 6)
        pyxel.text(4, 196, "Q: ", 10)
        pyxel.text(12, 196, "QUIT", 6)
        pyxel.text(40, 196, "P: ", 10)
        pyxel.text(48, 196, "PAUSE", 6)
        pyxel.text(76, 196, "R: ", 10)
        pyxel.text(84, 196, "RESTART", 6)