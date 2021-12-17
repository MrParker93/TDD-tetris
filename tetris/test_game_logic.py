import pytest
from board import Board
from movement import Move


class TestGameLogic:
    @pytest.fixture
    def board(self):
        board = Board(6, 6)
        yield board

    @pytest.fixture
    def long_board(self):
        long_board = Board(5, 10)
        yield long_board

    def test_the_game_logic_clears_a_single_line_when_a_block_lands_and_completes_a_line_and_adds_the_same_number_of_lines_cleared_to_beginning_of_the_board(self, board):
        board.generate_block(6)
        move = Move(board.block, board.board)
        for _ in range(6):
            board.block.x = move.move_left()
            board.block.y = move.move_down()
        assert board.is_falling() == True
        board.drop_block()
        board.falling()
        assert board.board == [[0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [7, 7, 7, 7, 0, 0]]

        assert board.is_falling() == False

        board.generate_block(0)
        move = Move(board.block, board.board)
        for _ in range(6):
            board.block.x = move.move_right()
            board.block.y = move.move_down()
        assert board.is_falling() == True
        board.drop_block()
        board.falling()
        assert board.grid == [[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 1],
                              [7, 7, 7, 7, 1, 1]]

        assert board.is_falling() == False
        assert board.board == [[0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 1]]
    
    def test_the_game_logic_clears_four_lines_when_a_block_completes_a_tetris_and_adds_four_lines_to_the_beginning_of_the_board(self, long_board):
        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 0]]
                                   
        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 0],
                                   [7, 7, 7, 7, 0]]

        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 0],
                                   [7, 7, 7, 7, 0],
                                   [7, 7, 7, 7, 0]]

        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 0],
                                   [7, 7, 7, 7, 0],
                                   [7, 7, 7, 7, 0],
                                   [7, 7, 7, 7, 0]]

        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        long_board.block.block = move.rotate_left()
        for _ in range(5):
            long_board.block.x = move.move_right()
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 7],
                                   [7, 7, 7, 7, 7],
                                   [7, 7, 7, 7, 7],
                                   [7, 7, 7, 7, 7]]
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.board == [[0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]

    def test_the_game_logic_clears_two_separate_lines_independently_and_drops_the_uncleared_lines_down_the_correct_distance(self, long_board):
        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 0]]

        long_board.generate_block(0)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 1, 1, 0, 0],
                                   [0, 1, 1, 0, 0],
                                   [7, 7, 7, 7, 0]]

        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 0],
                                   [0, 1, 1, 0, 0],
                                   [0, 1, 1, 0, 0],
                                   [7, 7, 7, 7, 0]]
                                   
        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        long_board.block.block = move.rotate_left()
        for _ in range(5):
            long_board.block.x = move.move_right()
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 7],
                                   [0, 1, 1, 0, 7],
                                   [0, 1, 1, 0, 7],
                                   [7, 7, 7, 7, 7]]

        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.board == [[0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 1, 1, 0, 7],
                                    [0, 1, 1, 0, 7]]

    
    def test_points_are_added_to_total_score_when_lines_cleared(self, long_board):
        long_board.generate_block(6)
        long_board.block.x = long_board.width // 2 - long_board.block.width // 2
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [7, 7, 7, 7, 0]]

        long_board.generate_block(3)
        long_board.block.x = (long_board.width // 2 - long_board.block.width // 2) - 1
        move = Move(long_board.block, long_board.board)
        for _ in range(10):
            long_board.block.y = move.move_down()
            long_board.block.x = move.move_right()
        long_board.drop_block()
        long_board.falling()
        assert long_board.is_falling() == False
        assert long_board.grid == [[0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 4, 4, 4],
                                   [7, 7, 7, 7, 4]]