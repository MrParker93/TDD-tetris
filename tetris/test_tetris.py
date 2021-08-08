import pyxel
import pytest
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
        assert board == (120, 180)

    def test_board_background_colour_is_black(self):
        """
        GIVEN the applicaion background colour
        WHEN the application is running
        THEN check the correct background is displayed
        """
        tetris = Tetris()
        background_colour = pyxel.COLOR_BLACK
        assert background_colour == 0

    


if __name__ == "__main__":
    pytest.main()
