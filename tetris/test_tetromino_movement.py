import pytest 
from board import Board
from movement import Move
from tetromino import Tetromino


class TestTetrominoMovement:
    @pytest.fixture
    def board(self):
        board = Board(10, 6)
        yield board

    @pytest.fixture
    def move(self, board):
        move = Move(board.current_position)
        yield move

    def test_T_tetromino_can_move_left(self, board, move):
        board.block = Tetromino(5).block
        board.current_position = move.move_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_can_move_right(self, board, move):
        board.block = Tetromino(5).block
        board.current_position = move.move_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 6, 6, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_can_move_down(self, board, move):
        board.block = Tetromino(5).block
        board.current_position = move.move_down()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_left_boundary_of_the_board(self, board, move):
        board.block = Tetromino(5).block
        for _ in range(10):
            board.current_position = move.move_left()
            if board.detect_collision():
                board.current_position = move.move_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                              [6, 6, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_right_boundary_of_the_board(self, board, move):
        board.block = Tetromino(5).block
        for _ in range(10):
            board.current_position = move.move_right()
            if board.detect_collision():
                board.current_position = move.move_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
                              [0, 0, 0, 0, 0, 0, 0, 6, 6, 6],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_bottom_of_the_board(self, board, move):
        board.block = Tetromino(5).block
        for _ in range(5):
            board.current_position = move.move_down()
            if board.detect_collision():
                board.current_position = (board.current_position[0], board.current_position[1] - 1)
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0]]
        board.falling()
        assert board.is_falling() == False

    def test_T_tetromino_cannot_move_left_through_another_block(self, board, move):
        board.block = Tetromino(5).block
        for _ in range(5):
            board.current_position = move.move_down()
            if board.detect_collision():
                board.current_position = (board.current_position[0], board.current_position[1] - 1)
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

        board.block = Tetromino(5).block
        print(f"curr_pos: {board.current_position}")
        if _ in range(10):
            board.current_position = move.move_right()
            if board.detect_collision():
                board.current_position = move.move_left()
        # for _ in range(3):
        #     board.current_position = move.move_down()
        # board.current_position = move.move_left()
        # if board.detect_collision():
        #     board.current_position = move.move_right()
        # print(f"curr_pos: {board.current_position}")
        board.drop_block()
        print(f"curr_pos: {board.current_position}")
        # assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 6, 0, 0],
                              [0, 0, 0, 0, 0, 6, 6, 6, 6, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0]]
        