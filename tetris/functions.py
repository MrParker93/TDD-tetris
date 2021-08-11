import pyxel

game_text = {"score_label": "SCORE :", "quit_label": "Q :",
             "quit_string": "Quit", "restart_label": "R :", "restart_string": "Restart"}

# Set colours for each block
block_colours = [
    pyxel.COLOR_DARKBLUE,
    pyxel.COLOR_ORANGE,
    pyxel.COLOR_YELLOW,
    pyxel.COLOR_LIGHTBLUE,
    pyxel.COLOR_LIME,
    pyxel.COLOR_RED,
    pyxel.COLOR_PURPLE
]

# Colours each block shape


def colour_each_block(num):
    colours = {str(index): colours for index,
               colours in enumerate(block_colours, start=1)}
    if str(num) in colours.keys():
        return colours[str(num)]
