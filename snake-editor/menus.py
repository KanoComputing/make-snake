
# menus.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import os

THEMES_DIR = os.path.expanduser('~/Snake-content')

# List of themes
naming = []

colors = [["Black", None], ["Red", None], ["Green", None], ["Yellow", None],
          ["Blue", None], ["Magenta", None], ["Cyan", None], ["White", None]]

# Elements
snake = [["Background colour", colors], ["Snake body", "symbols"], ["Symbol colour", colors], ["Back", None]]
lives = [["Background colour", colors], ["Lives symbol", "symbols"], ["Symbol colour", colors], ["Back", None]]
apple = [["Background colour", colors], ["Apple symbol", "symbols"], ["Symbol colour", colors], ["Back", None]]
# Board
border = [["Background colour", colors], ["Corner symbol", "symbols"], ["Horizontal symbol", "symbols"],
          ["Vertical symbol", "symbols"], ["Corner symbol", "symbols"], ["Back", None]]
background = [["Background colour", colors], ["Symbol colour", colors], ["Background symbol", "symbols"],
              ["Back", None]]

# Edit Menu
elements = [["Snake", snake], ["Lives", lives], ["Apples", apple], ["Back", None]]
board = [["Background", background], ["Border", border], ["Back", 0]]
delete = [["Do you really want to delete this theme?", "yep"], ["Yes", "delete"], ["No", 0]]

editMain = [["Board", board], ["Elements", elements], ["Delete Theme", delete], ["Back", 0]]

# New theme
newName = [["Choose a Name", "name"], ["Back", 0]]

# Main
main = [["New Theme", newName], ["Saved Themes", naming], ["Exit", None]]


def update_naming():
    global naming

    themes = os.listdir(THEMES_DIR)
    # clear list
    naming[:] = []
    for t in themes:
        naming.append([t, "existing"])
    naming.append(["Back", 0])
    return
