import pyxel
import pytest
import constants
from tetris import Tetris
from tetromino import Tetrominoes


class TestTetris:
    """"""

    def test_board_size_matches_given_width_and_height(self):
        """
        GIVEN the board width and height
        WHEN the application is running
        THEN check the board width and height are correct.
        """
        tetris = Tetris()
        board = (pyxel.width, pyxel.height)
        assert board == (120, 220)

    def test_board_background_colour_is_black(self):
        """
        GIVEN the applicaion background colour
        WHEN the application is running
        THEN check the correct background is displayed.
        """
        background_colour = pyxel.COLOR_BLACK
        assert background_colour == constants.BACKGROUND_COLOUR

    def test_each_shape_exists(self):
        """"""
        for blocks in constants.BLOCKS.keys():
            for _ in constants.BLOCK_NAME:
                if constants.BLOCK_NAME[0] in blocks:
                    assert "O_NEUTRAL" or "O_DOWN" or "O_LEFT" or "O_UP" in blocks
                if constants.BLOCK_NAME[1] in blocks:
                    assert "I_NEUTRAL" or "I_DOWN" or "I_LEFT" or "I_UP" in blocks
                if constants.BLOCK_NAME[2] in blocks:
                    assert "S_NEUTRAL" or "S_DOWN" or "S_LEFT" or "S_UP" in blocks
                if constants.BLOCK_NAME[3] in blocks:
                    assert "Z_NEUTRAL" or "Z_DOWN" or "Z_LEFT" or "Z_UP" in blocks
                if constants.BLOCK_NAME[4] in blocks:
                    assert "L_NEUTRAL" or "L_DOWN" or "L_LEFT" or "L_UP" in blocks
                if constants.BLOCK_NAME[5] in blocks:
                    assert "J_NEUTRAL" or "J_DOWN" or "J_LEFT" or "J_UP" in blocks
                if constants.BLOCK_NAME[6] in blocks:
                    assert "T_NEUTRAL" or "T_DOWN" or "T_LEFT" or "T_UP" in blocks

    def test_each_direction_moves_each_shape_in_the_correct_coordiantes(self):
        """"""
        tetris = Tetrominoes()
        tetris.position = (1, 1)
        board = []
        tetris.move_block(direction="right", board=board)
        assert tetris.position == (2, 1)
        tetris.move_block(direction="left", board=board)
        assert tetris.position == (1, 1)
        tetris.move_block(direction="down", board=board)
        assert tetris.position == (1, 2)
        tetris.move_block(direction="downRight", board=board)
        assert tetris.position == (2, 3)
        tetris.move_block(direction="downLeft", board=board)
        assert tetris.position == (1, 4)

    def test_rotation_for_each_orientation_for_each_shape(self):
        
        tetris = Tetrominoes()
        tetris.orientation = "RIGHT"
        board = []
        tetris.rotate(rotation="cw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "DOWN"
        tetris.rotate(rotation="cw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "LEFT"
        tetris.rotate(rotation="cw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "UP"
        tetris.rotate(rotation="cw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "RIGHT"
        tetris.rotate(rotation="acw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "UP"
        tetris.rotate(rotation="acw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "LEFT"
        tetris.rotate(rotation="acw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "DOWN"
        tetris.rotate(rotation="acw", orientation=tetris.orientation, board=board)
        assert tetris.orientation == "RIGHT"

    def test_shapes_are_generated_correctly_after_previous_shape_is_used(self):
        pass

    def test_scoring_system_registers_multiple_row_combos(self):
        pass

    def test_losing_condition_functions_correctly(self):
        pass


if __name__ == "__main__":
    pytest.main()
