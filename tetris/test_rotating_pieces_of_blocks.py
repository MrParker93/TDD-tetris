from piece import Piece


p = Piece()
class TestRotatingPieces:
    def test_3_by_3_board_exists(self):
        """"""
        p.size = 3
        assert len(p.board) == 3
        assert len(p.board[0]) == 3

    def test_the_number_of_blocks_in_the_current_piece(self):
        """"""
        assert p.size == 3
                                
    def test_piece_exists_on_3_by_3_board(self):
        """"""
        assert p.create_piece() == [[0, 2, 0],
                                    [2, 2, 0],
                                    [0, 0, 0]]
    
    def test_piece_can_be_rotated_to_the_right(self):
        """"""
        p.shape = p.create_piece()
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
        p = Piece(None,5)
        assert len(p.board) == 5
        assert len(p.board[0]) == 5
    
    def test_piece_exists_on_5_by_5_board(self):
        """"""
        
        p = Piece(None,5)
        assert p.create_piece() == [[0, 0, 2, 0, 0],
                                    [0, 2, 2, 0, 0],
                                    [2, 2, 2, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]
    
    def test_piece_can_be_rotated_to_the_right_on_5_by_5_board(self):
        """"""
        
        p = Piece(None,5)
        p.shape = p.create_piece()
        assert p.rotate_right() == [[0, 0, 2, 0, 0],
                                    [0, 0, 2, 2, 0],
                                    [0, 0, 2, 2, 2],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]
                                    
    def test_piece_can_be_rotated_to_the_right_on_5_by_5_board(self):
        """"""
        
        p = Piece(None,5)
        p.shape = p.create_piece()
        assert p.rotate_left() == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [2, 2, 2, 0, 0],
                                   [0, 2, 2, 0, 0],
                                   [0, 0, 2, 0, 0]]