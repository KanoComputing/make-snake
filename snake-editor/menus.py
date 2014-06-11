
# menus.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#


colors = [["Black", None], ["Red", None], ["Green", None], ["Yellow", None],
          ["Blue", None], ["Magenta", None], ["Cyan", None], ["White", None]]

# Elements
snake = [["Background colour", colors], ["Snake body", "symbols"],
         ["Symbol colour", colors], ["Back", None]]
lives = [["Background colour", colors], ["Lives symbol", "symbols"],
         ["Symbol colour", colors], ["Back", None]]
apple = [["Background colour", colors], ["Apple symbol", "symbols"],
         ["Symbol colour", colors], ["Back", None]]
# Board
border = [["Background colour", colors], ["Corner symbol", "symbols"],
          ["Horizontal symbol", "symbols"], ["Vertical symbol", "symbols"],
          ["Symbol colour", colors], ["Back", None]]
background = [["Background colour", colors], ["Background symbol", "symbols"],
              ["Symbol colour", colors], ["Back", None]]
# Main
elements = [["Snake", snake], ["Lives", lives], ["Apples", apple],
            ["Back", None]]
board = [["Background", background], ["Border", border], ["Back", 0]]

main = [["Board", board], ["Elements", elements], ["Exit", None]]
