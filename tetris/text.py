import pyxel

class Text:
    def __init__(self, level, score, lines, combos):
        self.level = level
        self.score = score
        self.lines = lines
        self.combos = combos

    def show(self):
        pyxel.text(186 * 0.75, 8, "NEXT: ", 10)
        pyxel.text(186 * 0.75, 72, "LEVEL", 10)
        pyxel.text(186 * 0.75, 80, str(self.level), 6)
        pyxel.text(186 * 0.75, 96, "SCORE", 10)
        pyxel.text(186 * 0.75, 104, str(self.score), 6)
        pyxel.text(186 * 0.75, 120, "LINES", 10)
        pyxel.text(186 * 0.75, 128, str(self.lines), 6)
        pyxel.text(186 * 0.75, 146, "COMBOS", 10)
        pyxel.text(186 * 0.75, 154, str(self.combos), 6)
        pyxel.text(4, 204, "Q: ", 10)
        pyxel.text(14, 204, "QUIT", 6)
        pyxel.text(186 * 0.40, 204, "P: ", 10)
        pyxel.text((186 * 0.40) + 10, 204, "PAUSE", 6)
        pyxel.text(186 * 0.75, 204, "R: ", 10)
        pyxel.text((186 * 0.75) + 10, 204, "RESTART", 6)