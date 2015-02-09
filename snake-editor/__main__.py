#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import graphics
import theme
import gameloop
import sys

from kano.utils import is_gui


def exit():
    """Attempts to tidy up the graphics.
    Finally it calls sys.exit(), since sys is already imported
    """
    graphics.exit()
    sys.exit()


def run():
    try:
        # Init the editor
        graphics.init()
        theme.init()

        # Start the editor
        gameloop.start()

    except KeyboardInterrupt:
        exit()

if not is_gui():
    sys.exit("make-snake requires an X session")

run()
