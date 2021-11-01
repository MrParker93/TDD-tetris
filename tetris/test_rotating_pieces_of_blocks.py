import pytest 
from piece import Piece

p = Piece(3)
class TestRotatingPieces:
    def test_piece_exists_on_3_by_3_board(self):
        """"""
        assert p.create_piece() == [[0, 2, 0],
                                    [0, 2, 0],
                                    [0, 0, 0]]
                                
    def test_piece_can_be_rotated_to_the_right(self):
        """"""
        assert p.rotate_right() == [[0, 0, 0],
                                    [0, 2, 2],
                                    [0, 0, 0]]
       
    def test_piece_can_be_rotated_to_the_left(self):
        """"""
        assert p.rotate_left() == [[0, 0, 0],
                                   [2, 2, 0],
                                   [0, 0, 0]]