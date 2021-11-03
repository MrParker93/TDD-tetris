import pyxel
from piece import Piece
from rotatable import Rotatable

class Mino(Rotatable):
    def __init__(self):
        super().__init__()
        self.rotation = []
        self.current_rotation = 0

    def rotate_right(self):
        return 
class MinoO(Mino):
    def __init__(self):
        super().__init__()
        self.shape = [[1, 1, 0],
                      [1, 1, 0],
                      [0, 0, 0]]
        self.rotation = 1
        self.current_rotation = 0

class MinoS(Mino):
    def __init__(self):
        super().__init__()
        self.shape = [[0, 1, 1],
                      [1, 1, 0],
                      [0, 0, 0]]
        self.rotation = 2
        self.current_rotation = 0

class MinoZ(Mino):
    def __init__(self):
        super().__init__()
        self.shape = [[1, 1, 0],
                      [0, 1, 1],
                      [0, 0, 0]]
        self.rotation = 2
        self.current_rotation = 0

class MinoJ(Mino):
    def __init__(self):
        super().__init__()
        self.shape = [[0, 1, 0],
                      [0, 1, 0],
                      [1, 1, 0]]
        self.rotation = 4
        self.current_rotation = 0

class MinoL(Mino):
    def __init__(self):
        super().__init__()
        self.shape = [[0, 1, 0],
                      [0, 1, 0],
                      [0, 1, 1]]
        self.rotation = 4
        self.current_rotation = 0

class MinoT(Mino):
    def __init__(self):
        super().__init__()
        self.shape = [[0, 1, 0],
                      [1, 1, 1],
                      [0, 0, 0]]
        self.rotation = 4
        self.current_rotation = 0

class MinoI(Mino):
    def __init__(self):
        super().__init__()
        self.shape = [[0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]
        self.rotation = 2
        self.current_rotation = 1

m = Mino()