from piece import Piece


class TestRotatingPieces:
    # def test_the_number_of_blocks_in_the_current_piece(self):
    #     """"""
    #     assert p.size == 3
                                
    def test_a_3_by_3_piece_exists(self):
        """"""
        p = Piece([[0, 2, 0],
                   [2, 2, 0],
                   [0, 0, 0]])

        assert p.block == [[0, 2, 0],
                           [2, 2, 0],
                           [0, 0, 0]]
    
    def test_piece_can_be_rotated_to_the_right(self):
        """"""
        p = Piece([[0, 2, 0],
                   [2, 2, 0],
                   [0, 0, 0]])

        assert p.rotate_right().block == [[0, 2, 0],
                                          [0, 2, 2],
                                          [0, 0, 0]]
       
    def test_piece_can_be_rotated_to_the_left(self):
        """"""
        p = Piece([[0, 2, 0],
                   [2, 2, 0],
                   [0, 0, 0]])
                   
        assert p.rotate_left().block == [[0, 0, 0],
                                         [2, 2, 0],
                                         [0, 2, 0]]
    
    def test_a_5_by_5_piece_exists(self):
        """"""
        
        p = Piece([[0, 0, 2, 0, 0],
                   [0, 2, 2, 0, 0],
                   [2, 2, 2, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]])

        assert p.block == [[0, 0, 2, 0, 0],
                           [0, 2, 2, 0, 0],
                           [2, 2, 2, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]]
    
    def test_piece_can_be_rotated_to_the_right_on_5_by_5_board(self):
        """"""
        
        p = Piece([[0, 0, 2, 0, 0],
                   [0, 2, 2, 0, 0],
                   [2, 2, 2, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]])

        assert p.rotate_right().block == [[0, 0, 2, 0, 0],
                                          [0, 0, 2, 2, 0],
                                          [0, 0, 2, 2, 2],
                                          [0, 0, 0, 0, 0],
                                          [0, 0, 0, 0, 0]]
                                    
    def test_piece_can_be_rotated_to_the_left_on_5_by_5_board(self):
        """"""
        
        p = Piece([[0, 0, 2, 0, 0],
                   [0, 2, 2, 0, 0],
                   [2, 2, 2, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]])
                   
        assert p.rotate_left().block == [[0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0],
                                         [2, 2, 2, 0, 0],
                                         [0, 2, 2, 0, 0],
                                         [0, 0, 2, 0, 0]]