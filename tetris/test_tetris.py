import pyxel
import pytest
from tetris import Tetris, Direction, Shape


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
        assert board == (120, 180)

    def test_board_background_colour_is_black(self):
        """
        GIVEN the applicaion background colour
        WHEN the application is running
        THEN check the correct background is displayed.
        """
        tetris = Tetris()
        background_colour = pyxel.COLOR_BLACK
        assert background_colour == 0

    def test_each_section_of_each_shape_exists(self):
        """
        GIVEN each type of section of each shape
        WHEN the application is running
        THEN check the shapes exist in the list.
        """
        tetris = Tetris()
        L_shape = tetris.draw_shape(Direction.RIGHT)[0] 
        T_shape = tetris.draw_shape(Direction.RIGHT)[1] 
        O_shape = tetris.draw_shape(Direction.RIGHT)[2] 
        I_shape = tetris.draw_shape(Direction.RIGHT)[3] 
        Z_shape = tetris.draw_shape(Direction.RIGHT)[4] 
        S_shape = tetris.draw_shape(Direction.RIGHT)[5] 
        J_shape = tetris.draw_shape(Direction.RIGHT)[6] 
        assert type(L_shape) == list
        assert type(T_shape) == list
        assert type(O_shape) == list
        assert type(I_shape) == list
        assert type(Z_shape) == list
        assert type(S_shape) == list
        assert type(J_shape) == list

    def test_each_shape_works_with_each_direction(self):
        tetris = Tetris()
        direction = [
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT,
            Direction.UP
        ]

        for i in direction:
            L_shape = tetris.draw_shape(i)[0]
            T_shape = tetris.draw_shape(i)[1]
            O_shape = tetris.draw_shape(i)[2]
            I_shape = tetris.draw_shape(i)[3]
            Z_shape = tetris.draw_shape(i)[4]
            S_shape = tetris.draw_shape(i)[5]
            J_shape = tetris.draw_shape(i)[6]
            assert len(L_shape) == 4
            assert len(T_shape) == 4
            assert len(O_shape) == 4
            assert len(I_shape) == 4
            assert len(Z_shape) == 4
            assert len(S_shape) == 4
            assert len(J_shape) == 4
            
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