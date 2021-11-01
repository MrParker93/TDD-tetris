import pyxel
import random

class Piece:
    def __init__(self, size) -> None:
        self.block = []
        self.size = size
        self.board = [[0] * size for _ in range(size)]

    def rotate_right(self):
        return self.rotate(self.block)
    
    def rotate_left(self):
        rotate = self.rotate(self.block)
        rotate_again = self.rotate(rotate)
        return self.rotate(rotate_again)

    def create_piece(self):
        new_board =[]
        for row in range(len(self.board) - 1):
            new_board.append([])
            for _ in range(row, len(self.board) - 1):
                new_board[row].append(0)
            for col in range(row, -1, -1):
                new_board[row].append(2)
                pass
        return new_board

    def rotate(self, block):
        return list(map(list, zip(*block[::-1])))

p = Piece(3)
piece = p.create_piece()
print(p.board)
print(piece)