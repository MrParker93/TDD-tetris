import pyxel
import random
import numpy as np


class Board:
    WIDTH = 10
    HEIGHT = 20

    def __init__(self):
        self.board = np.zeros((Board.WIDTH * Board.HEIGHT)).reshape(Board.HEIGHT, Board.WIDTH)
        self.block = TetriminoGenerator().generate()
        
