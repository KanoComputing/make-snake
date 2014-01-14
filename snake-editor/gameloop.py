
# game-loop.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import graphics
import game
import controls


def start():
    init()

    while True:
        controls.update()
        graphics.drawCurrentMenu()


def init():
    game.init()
    graphics.drawGame()
    graphics.update()
