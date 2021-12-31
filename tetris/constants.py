import pyxel

BOARDWIDTH = 10
BOARDHEIGHT = 30
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
print(f"font height: {pyxel.FONT_HEIGHT}, font width: {pyxel.FONT_WIDTH}")