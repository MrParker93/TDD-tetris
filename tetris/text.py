import pyxel

class Text:
    def __init__(self, level, score, lines, combos):
        self.level = level
        self.score = score
        self.lines = lines
        self.combos = combos

    def show(self):
        pyxel.text(140 * 0.66, 8, "NEXT: ", 10)
        pyxel.text(140 * 0.66, 72, "LEVEL", 10)
        pyxel.text(140 * 0.66, 80, str(self.level), 6)
        pyxel.text(140 * 0.66, 96, "SCORE", 10)
        pyxel.text(140 * 0.66, 104, str(self.score), 6)
        pyxel.text(140 * 0.66, 120, "LINES", 10)
        pyxel.text(140 * 0.66, 128, str(self.lines), 6)
        pyxel.text(140 * 0.66, 146, "COMBOS", 10)
        pyxel.text(140 * 0.66, 154, str(self.combos), 6)
        pyxel.text(4, 180, "Q: ", 10)
        pyxel.text(14, 180, "QUIT", 6)
        pyxel.text(140 * 0.33, 180, "P: ", 10)
        pyxel.text((140 * 0.33) + 10, 180, "PAUSE", 6)
        pyxel.text(140 * 0.66, 180, "R: ", 10)
        pyxel.text((140 * 0.66) + 10, 180, "RESTART", 6)