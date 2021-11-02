from piece import Piece

p = Piece(3, 3)
class TestRotatingPieces:
    def test_3_by_3_board_exists(self):
        """"""
        assert len(p.board) == 3
        assert len(p.board[0]) == 3

    def test_the_number_of_blocks_in_the_current_piece(self):
        """"""
        assert p.blocks == 3
                                
    def test_piece_exists_on_3_by_3_board(self):
        """"""
        assert p.create_piece() == [[0, 2, 0],
                                    [2, 2, 0],
                                    [0, 0, 0]]
    
    def test_piece_can_be_rotated_to_the_right(self):
        """"""
        assert p.rotate_right() == [[0, 2, 0],
                                    [0, 2, 2],
                                    [0, 0, 0]]
       
    def test_piece_can_be_rotated_to_the_left(self):
        """"""
        assert p.rotate_left() == [[0, 0, 0],
                                   [2, 2, 0],
                                   [0, 2, 0]]
    
    def test_5_by_5_board_exists(self):
        """"""
        p = Piece(5, 5)
        assert len(p.board) == 5
        assert len(p.board[0]) == 5
    
    def test_piece_exists_on_5_by_5_board(self):
        """"""
        p = Piece(5, 5)
        assert p.create_piece() == [[0, 0, 2, 0, 0],
                                    [0, 2, 2, 0, 0],
                                    [2, 2, 2, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]
    
    def test_piece_can_be_rotated_to_the_right_on_5_by_5_board(self):
        """"""
        p = Piece(5, 5)
        p.create_piece()
        assert p.rotate_right() == [[0, 0, 2, 0, 0],
                                    [0, 0, 2, 2, 0],
                                    [0, 0, 2, 2, 2],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]
                                    
    def test_piece_can_be_rotated_to_the_right_on_5_by_5_board(self):
        """"""
        p = Piece(5, 5)
        p.create_piece()
        assert p.rotate_left() == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [2, 2, 2, 0, 0],
                                   [0, 2, 2, 0, 0],
                                   [0, 0, 2, 0, 0]]