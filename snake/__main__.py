#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import graphics
import theme
import gameloop
import game
import parser
import stage
import sys

import gamestate as gs
import kano.utils as ku


def exit():
    graphics.exit()
    gs.save_state()


def run():
    try:
        # Init the game
        parser.init()
        stage.init()
        graphics.init()
        theme.init()
        game.reset()
        gs.load_state()

        # Start the game
        gameloop.start()

    except KeyboardInterrupt:
        exit()

if not ku.is_gui():
    sys.exit("make-snake requires an X session")

run()
