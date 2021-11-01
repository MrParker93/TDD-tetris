import pyxel
import random

class Piece:
    def __init__(self, size) -> None:
        self.block = []
        self.size = size
        self.board = [[0] * size for _ in range(size)]

    def rotate_right(self):
        return self.rotate(self.board)
    
    def rotate_left(self):
        rotate = self.rotate(self.board)
        rotate_again = self.rotate(rotate)
        return self.rotate(rotate_again)

    def create_piece(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if row < self.size - 1 and col == int(len(self.board[row]) / 2):
                    self.board[row][col] = 2
        return self.board

    def rotate(self, block):
        return list(map(list, zip(*block[::-1])))


p = Piece(5)
print(*p.board, sep="\n")
print(*p.create_piece(), sep="\n")