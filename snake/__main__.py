#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import os
import graphics
import theme
import gameloop
import game
import parser
import stage
import sys

import gamestate as gs
from kano.utils import is_gui


def exit(save_state=True):
    try:
        graphics.exit()
    except:
        pass
    if save_state:
        gs.save_state()


def run():
    try:
        # Init the game
        parser.init()
        # Check for editor
        if (parser.args.editor):
            os.system("/usr/share/make-snake/snake-editor/__main__.py")
            sys.exit(0)
        graphics.init()
        theme.init()
        stage.init()
        game.reset()
        gs.load_state()

        # Start the game
        gameloop.start()

    except KeyboardInterrupt:
        exit()

if not is_gui():
    sys.exit("make-snake requires an X session")

run()
