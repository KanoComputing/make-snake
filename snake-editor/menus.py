
# menus.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Contributors: https://github.com/alexaverill
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
delete = [["Do you really want to delete this theme?", None], ["Yes", "delete"], ["No", 0]]

editMain = [["Board", board], ["Elements", elements], ["Delete Theme", delete], ["Take Screenshot", "screenshot"],
            ["Back", 0]]

# New theme
newName = [["Choose a Name", "name"], ["Back", 0]]

# Main
main = [["New Theme", newName], ["Saved Themes", naming], ["Exit", None]]


def update_naming():
    global naming

    themes = os.listdir(THEMES_DIR)
    for t in themes:
        # Remove everything that is not xml
        if not t.endswith('.xml'):
            themes.remove(t)
    # clear list
    naming[:] = []
    for t in themes:
        # Remove .xml extension
        t = os.path.splitext(t)[0]
        naming.append([t, "existing"])

    # Internet themes
    shared_themes_dir = THEMES_DIR + '/webload'
    if os.path.isdir(shared_themes_dir):
        # remove folder name from list if it has been added
        try:
            themes.remove("webload")
        except:
            pass
        shared_themes = os.listdir(shared_themes_dir)
        # Add xmls in webload
        for s in shared_themes:
            if s.endswith('.xml'):
                # Remove .xml extension and add to list
                s = os.path.splitext(s)[0]
                naming.append([s, "existing"])
    naming.append(["Back", 0])
    return
