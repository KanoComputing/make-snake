
# stage.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import console
import math


def init():
    global size, width, height, padding, boundaries, chosen_theme

    available_size = (width, height) = console.getTerminalSize()
    chosen_size = (20, 15)

    # Calculate width
    if chosen_size[0] > available_size[0] / 2:
        width = available_size[0] / 2
    else:
        width = chosen_size[0]
    # Calculate height
    if chosen_size[1] > available_size[1]:
        height = available_size[1]
    else:
        height = chosen_size[1]

    size = (width, height)

    padding_x = int(math.floor(available_size[0] - width) / 4)
    padding_y = int(math.floor(available_size[1] - height) / 2)

    padding = (padding_y, padding_x, padding_y, padding_x)

    boundaries = {
        "bottom": int(math.floor(height / 2)),
        "left": int(math.floor(-width / 2)),
        "right": int(math.floor(width / 2)),
        "top": int(math.floor(-height / 2)),
    }
