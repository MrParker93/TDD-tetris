from constants import *


class Scores:
    def __init__(self):
        self.score = SCORE
        self.level = LEVEL
        self.lines = LINES
        self.combos = COMBOS
        self.spins = SPINS
        self.fall_speed = FALL_SPEED
    
    def points(self, cleared_lines):
        if cleared_lines != None:
            self.lines += cleared_lines
            if self.check_combo_count(self.combos):
                multiplier = (cleared_lines * self.level) + (50 * self.level)
                self.score += POINTS[str(cleared_lines)] * (self.level + 1) + multiplier
            else:
                self.score += POINTS[str(cleared_lines)] * (self.level + 1)
        return self.score

    def check_combo_count(self, combo_count):
        if combo_count > 0:
            self.combos += combo_count
            return True
        return False

    def can_level_up(self):
        return self.lines > self.level * 5