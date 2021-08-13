from constants import BLOCKS
import pyxel
import random
import constants

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


shape = (
    ("O", "X", "O"),
    ("X", "X", "X"),
    ("O", "O", "O")
)

# print(shape[0])
# print(shape[1])
# print(shape[2])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# face_right = tuple(zip(*shape[::-1]))
# print(face_right[0])
# print(face_right[1])
# print(face_right[2])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# face_down = tuple(zip(*face_right[::-1]))
# print(face_down[0])
# print(face_down[1])
# print(face_down[2])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# face_left = tuple(zip(*shape[::1]))
# print(face_left[0])
# print(face_left[1])
# print(face_left[2])

print(random.choice("a" "b"))
