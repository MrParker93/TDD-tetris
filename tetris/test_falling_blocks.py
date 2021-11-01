import pytest
from board import Board
from block import Block

b = Board()
class TestFallingBlocks:
    def test_board_exists_and_is_filled_with_zeros(self):
        """"""
        board = b.board
        assert len(board) == b.HEIGHT
        assert len(board[0]) == b.WIDTH
        assert b.board == [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    def test_no_block_is_falling(self):
        """"""
        assert b.is_falling() == False

    def test_a_block_starts_falling(self):
        """"""
        b.start_falling()
        assert b.block.col == int(len(b.board) / 2)

    def test_a_block_is_falling(self):
        """"""
        b.block = Block(0, 0, "I")
        assert b.is_falling() == True

    def test_the_block_starts_from_the_top_middle(self):
        """"""
        b.start_falling()
        assert b.generate_block_on_board() == [[0, "I", 0],
                                               [0, 0, 0],
                                               [0, 0, 0]]
        
    def test_the_block_moves_down_on_board(self):
        """"""
        b.falling()
        assert b.generate_block_on_board() == [[0, 0, 0],
                                               [0, "I", 0],
                                               [0, 0, 0]]

    def test_one_block_can_fall_at_a_time(self):
        """"""
        with pytest.raises(ValueError):
            b.generate_block()

    def test_the_block_falls_to_the_last_row(self):
        """"""
        b.falling()
        assert b.generate_block_on_board() == [[0, 0, 0],
                                               [0, 0, 0],
                                               [0, "I", 0]]

    def test_the_block_continues_to_fall_on_the_last_row(self):
        """"""
        assert b.is_falling() == True
        assert b.generate_block_on_board() == [[0, 0, 0],
                                               [0, 0, 0],
                                               [0, "I", 0]]
        assert b.is_falling() == True

    def test_the_block_continues_to_fall_and_stops_on_the_last_row(self):
        """"""
        assert b.is_falling() == True
        b.falling()
        assert b.board == [[0, 0, 0],
                           [0, 0, 0],
                           [0, "I", 0]]
        assert b.is_falling() == False

    def test_the_next_block_is_generated_after_the_previous_one_is_placed_on_the_board(self):
        """"""
        assert b.is_falling() == False
        b.generate_block()
        b.block = Block(0, 0, "J")
        b.start_falling()
        assert b.is_falling() == True
        assert b.generate_block_on_board() == [[0, "J", 0],
                                               [0, 0, 0],
                                               [0, "I", 0]]
    
    def test_the_new_block_continues_to_fall_to_the_last_row(self):
        """"""
        b.falling()
        assert b.generate_block_on_board() == [[0, 0, 0],
                                               [0, "J", 0],
                                               [0, "I", 0]]

    def test_the_block_stops_when_it_detects_another_block(self):
        """"""
        assert b.is_falling() == True
        b.falling()
        assert b.generate_block_on_board() == [[0, 0, 0],
                                               [0, "J", 0],
                                               [0, "I", 0]]
        assert b.board == [[0, 0, 0],
                           [0, "J", 0],
                           [0, "I", 0]]
                           
        assert b.is_falling() == False