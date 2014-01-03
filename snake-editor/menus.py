
# menus.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#


colors = [["Black", None], ["Red", None], ["Green", None], ["Yellow", None],
          ["Blue", None], ["Magenta", None], ["Cyan", None], ["White", None]]

# Elements
snake = [["background color", colors], ["symbol color", colors],
         ["Snake body", "symbols"], ["Back", None]]
lives = [["background color", colors], ["symbol color", colors],
         ["Lives", "symbols"], ["Back", None]]
apple = [["background color", colors], ["symbol color", colors],
         ["Apple", "symbols"], ["Back", None]]
# Board
border = [["background color", colors], ["symbol color", colors],
          ["Border horizontal", "symbols"], ["Border vertical", "symbols"],
          ["Border corner", "symbols"], ["Back", None]]
background = [["background color", colors], ["symbol color", colors],
              ["Background", "symbols"], ["Back", None]]
# Main
elements = [["Snake", snake], ["Lives", lives], ["Apples", apple],
            ["Back", None]]
board = [["Background", background], ["Border", border], ["Back", 0]]

main = [["Board", board], ["Elements", elements], ["Exit", None]]
