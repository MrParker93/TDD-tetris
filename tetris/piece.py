import pyxel
import random

class Piece:
    def __init__(self, blocks, board_size) -> None:
        self.block = []
        self.blocks = blocks
        self.board = [[0] * board_size for _ in range(board_size)]

    def rotate_right(self):
        return self.rotate(self.board)
    
    def rotate_left(self):
        rotate = self.rotate(self.board)
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

    def rotate(self, block):
        return list(map(list, zip(*block[::-1])))

p = Piece(4, 5)
p.create_piece()
print(*p.board,sep="\n")