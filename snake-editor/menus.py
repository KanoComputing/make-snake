
# menus.py
#
# Copyright (C) 2013 - 2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Contributors: https://github.com/alexaverill
#

import os

THEMES_DIR = os.path.expanduser('~/Snake-content')

# List of themes
naming = []

colors = [[N_("Black"), None], [N_("Red"), None], [N_("Green"), None], [N_("Yellow"), None],
          [N_("Blue"), None], [N_("Magenta"), None], [N_("Cyan"), None], [N_("White"), None]]

# Elements
snake = [[_("Background colour"), colors],
         [_("Snake body"), "symbols"],
         [_("Symbol colour"), colors], [_("Back"), None]]
lives = [[_("Background colour"), colors],
         [_("Lives symbol"), "symbols"],
         [_("Symbol colour"), colors], [_("Back"), None]]
apple = [[_("Background colour"), colors],
         [_("Apple symbol"), "symbols"],
         [_("Symbol colour"), colors], [_("Back"), None]]
# Board
border = [[_("Background colour"), colors],
          [_("Horizontal symbol"), "symbols"],
          [_("Vertical symbol"), "symbols"],
          [_("Corner symbol"), "symbols"],
          [_("Symbol colour"), colors], [_("Back"), None]]
background = [[_("Background colour"), colors],
              [_("Symbol colour"), colors],
              [_("Background symbol"), "symbols"], [_("Back"), None]]

# Edit Menu
elements = [[_("Snake"), snake],
            [_("Lives"), lives],
            [_("Apples"), apple], [_("Back"), None]]
board = [[_("Background"), background],
         [_("Border"), border], [_("Back"), 0]]
delete = [[_("Do you really want to delete this theme?"), None],
          [_("Yes"), "delete"], [_("No"), 0]]

editMain = [[_("Board"), board], [_("Elements"), elements],
            [_("Delete Theme"), delete],
            [_("Take Screenshot"), "screenshot"], [_("Back"), 0]]

# New theme
newName = [[_("Choose a Name"), "name"], [_("Back"), 0]]

# Main
main = [[_("New Theme"), newName], [_("Saved Themes"), naming], [_("Exit"), None]]


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
    naming.append([_("Back"), 0])
    return
