
# __main__.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import graphics
import theme
import gameloop
import game
import parser
import stage
import os
import gamestate as gs


def exit():
    graphics.exit()
    gs.save_state()


def run():
    try:
        # Resize the window
        os.system('xdotool windowsize $(xdotool getactivewindow) 1024 709')

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

run()
