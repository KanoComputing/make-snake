#!/usr/bin/env python

# controls.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import __main__
import parser
import graphics
import game
import gameloop
from config import keys


def update():
    key = graphics.screen.getch()

    if key > 0:
        if key == keys['DOWN']:
            if game.direction[1] == -1:
                return

            game.direction = (0, 1)

        elif key == keys['LEFT']:
            if game.direction[0] == 1:
                return

            game.direction = (-1, 0)

        elif key == keys['RIGHT']:
            if game.direction[0] == -1:
                return

            game.direction = (1, 0)

        elif key == keys['UP']:
            if game.direction[1] == 1:
                return

            game.direction = (0, -1)

        elif key == keys['Q']:
            __main__.exit()
            exit()

        elif gameloop.state == 2 and key == keys['ENTER']:
            if parser.options.tutorial:
                __main__.exit()
                exit()
            else:
                gameloop.init()

        elif gameloop.state == 0 and key == keys['ENTER']:
            gameloop.init()
