import pyxel
from grid import Grid
from rotatable import Rotatable

class Piece(Grid, Rotatable):
    def __init__(self, shape=None, size=3):
        self.shape = shape
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]

    def rotate_right(self):
        return self.rotate(self.shape)
    
    def rotate_left(self):
        rotate = self.rotate(self.shape)
        rotate_again = self.rotate(rotate)
        return self.rotate(rotate_again)

    def create_piece(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if row <= int(len(self.board) / 2) and col <= int(len(self.board[row]) / 2):
                    self.board[row][col] = 2
            for i, _ in enumerate(range(row, int(len(self.board) / 2))):
                self.board[row][i] = 0
        return self.board

    def rotate(self, shape):
        return list(map(list, zip(*shape[::-1])))