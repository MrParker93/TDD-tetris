from grid import Grid
from coordinates import Coordinates

class Boards(Grid, Coordinates):
    @classmethod
    def get_all_coordinates(cls, board):
        coords = []
        for row in board.rows():
            for col in board.cols():
                coords.append(Coordinates(row, col))
        return coords

    @classmethod
    def 