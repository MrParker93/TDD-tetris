import pytest
from board import Board


class TestFallingBlocks:
    @pytest.fixture
    def board(self):
        board = Board(3, 3)
        yield board
    
    def test_board_class_is_type_Board(self, board):
        assert type(board) == Board
    
    def test_board_exists_and_is_empty(self, board):
        assert len(board.grid) == 3
        assert len(board.grid[0]) == 3
        assert board.grid == [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
    
    def test_no_block_is_currently_falling(self, board):
        assert board.is_falling() == False
        assert board.grid == [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
                            
    def test_block_generates_to_the_top_middle_of_the_board(self, board):
        board.generate_block(1)
        board.drop_block()
        board.is_falling()
        assert board.is_falling() == True
        assert board.grid == [[0, 1, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
    
    def test_block_fall_one_row_each_time_falling_is_called(self, board):
        board.generate_block(1)
        board.falling()
        board.drop_block()
        board.is_falling()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 1, 0],
                              [0, 0, 0]]
                               
    def test_only_one_block_can_be_falling_at_a_time(self, board):
        board.generate_block(1)
        board.falling()
        board.drop_block()
        board.is_falling()
        before = board.grid
        assert board.is_falling() == True
        with pytest.raises(Exception):
            assert board.generate_block(2) == "Block already falling"
        assert board.grid == before
    
    def test_block_continues_falling_when_it_reaches_the_last_row(self, board):
        board.generate_block(1)
        board.falling()
        board.falling()
        board.drop_block()
        board.is_falling()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 0, 0],
                              [0, 1, 0]]
        assert board.is_falling() == True
    
    def test_block_stops_falling_when_it_hits_the_bottom_of_the_board(self, board):
        board.generate_block(1)
        board.falling()
        board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 0, 0],
                              [0, 1, 0]]
        board.falling()
        assert board.grid == board.board
        assert board.is_falling() == False

    def test_new_block_generates_to_the_top_middle_on_updated_board(self, board):
        board.generate_block(1)
        board.falling()
        board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 0, 0],
                              [0, 1, 0]]
        board.falling()
        assert board.grid == board.board
        assert board.is_falling() == False
        board.generate_block(2)
        assert board.is_falling() == True
        board.drop_block()
        assert board.grid == [[0, 2, 0],
                              [0, 0, 0],
                              [0, 1, 0]]

    def test_block_continues_falling_when_it_lands_on_another_block(self, board):
        board.generate_block(1)
        board.falling()
        board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 0, 0],
                              [0, 1, 0]]
        board.falling()
        assert board.grid == board.board
        assert board.is_falling() == False
        board.generate_block(2)
        board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 2, 0],
                              [0, 1, 0]]
        assert board.is_falling() == True
    
    def test_block_stops_falling_when_it_hits_another_block(self, board):
        board.generate_block(1)
        board.falling()
        board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 0, 0],
                              [0, 1, 0]]
        board.falling()
        assert board.grid == board.board
        assert board.is_falling() == False
        board.generate_block(2)
        board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0],
                              [0, 2, 0],
                              [0, 1, 0]]
        board.falling()
        assert board.is_falling() == False
        