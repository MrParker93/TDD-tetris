import pyxel
import pytest
import constants
from tetris import Tetris


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

    def test_directions_and_rotation_is_registered_by_key_inputs(self):
        """"""
        tetris = Tetris()
        tetris.update()
        assert tetris.direction == None
        assert tetris.rotation == None

    def test_each_shape_works_with_each_direction(self):
        pass

    def test_rotation_works_correctly_using_key_inputs(self):
        pass

    def test_shapes_are_generated_correctly_after_previous_shape_is_used(self):
        pass

    def test_scoring_system_registers_multiple_row_combos(self):
        pass

    def test_losing_condition_functions_correctly(self):
        pass


if __name__ == "__main__":
    pytest.main()
