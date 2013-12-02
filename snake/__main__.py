
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


def exit():
    graphics.exit()


def run():
    try:
        parser.init()
        stage.init()
        graphics.init()
        theme.init()
        game.reset()
        gameloop.start()

    except KeyboardInterrupt:
        exit()

run()
