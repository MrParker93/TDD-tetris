import pyxel
import pytest
from tetris import App
from tetrimino import (Tetrimino, TetriminoO, TetriminoI,
                        TetriminoS, TetriminoZ, TetriminoL, TetriminoJ, TetriminoT)


class TestTetris:
    """"""

    def test_board_size_matches_given_width_and_height(self):
        """
        GIVEN the board width and height
        WHEN the application is running
        THEN check the board width and height are correct.
        """
        app = App
        app_width = app.WIDTH
        app_height = app.HEIGHT
        assert app_width == 180
        assert app_height == 220

    def test_board_background_colour_is_black(self):
        """
        GIVEN the application background colour
        WHEN the application is running
        THEN check the correct background is displayed.
        """
        pass

    def test_each_tetrimino_exists(self):
        """"""
        block_O = TetriminoO().block
        block_I = TetriminoI().block
        block_Z = TetriminoZ().block
        block_S = TetriminoS().block
        block_L = TetriminoL().block
        block_J = TetriminoJ().block
        block_T = TetriminoT().block
        assert block_O == [[5,5], [5,5]]
        assert block_I == [[0, 6, 0 ,0], [0, 6, 0 ,0], [0, 6, 0 ,0], [0, 6, 0 ,0]]
        assert block_Z == [[8, 8, 0], [0, 8, 8], [0, 0, 0]]
        assert block_S == [[0 ,10, 10], [10, 10, 0], [0, 0, 0]]
        assert block_L == [[0, 1, 0], [0, 1, 0], [0, 1, 1]]
        assert block_J == [[0, 2, 2], [0, 2, 0], [0, 2, 0]]
        assert block_T == [[0, 9, 0], [0, 9, 9], [0, 9, 0]]

    def test_each_direction_moves_each_shape_in_the_correct_coordiantes(self):
        """"""
        pass

    def test_rotation_for_each_orientation_for_each_shape(self):
        """"""
        tetrimino = Tetrimino()
        rotation = tetrimino.rotation
        orientation = tetrimino.orientation
        t = TetriminoT()
        t_block = t.block
        rotate_block = tetrimino.rotate_block(t_block)
        if rotate_block:
            rotation = 1
            orientation += rotation % 4
            assert orientation == 2
            assert rotate_block == [[0, 0, 0], [9, 9, 9], [0, 9, 0]]


    def test_shapes_are_generated_correctly_after_previous_shape_is_used(self):
        pass

    def test_score_is_updated_after_every_clear(self):
        pass

    def test_level_is_updated_after_reaching_certain_score(self):
        pass

    def test_lines_are_updated_after_evert_clear(self):
        pass

    def test_combos_are_updated_after_three_consecutive_clears(self):
        pass

    def test_losing_condition_functions_correctly(self):
        pass


if __name__ == "__main__":
    pytest.main()
