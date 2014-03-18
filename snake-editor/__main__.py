#!/usr/bin/python

# __main__.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#


import graphics
import theme
import gameloop
import stage


def exit():
    graphics.exit()


def run():
    try:
        # Init the editor
        stage.init()
        graphics.init()
        theme.init()

        # Start the editor
        gameloop.start()

    except KeyboardInterrupt:
        exit()

run()
