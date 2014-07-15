#!/usr/bin/env python

# game-loop.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import os
import time
import graphics
import game
import __main__
import config
import controls
import parser

last_update = None
playing = False
state = 0
speed = 0


def update():
    game.update()
    graphics.update()
    controls.clear()


def step():
    global last_update, speed

    cur_time = time.time()

    if last_update:
        elapsed = cur_time - last_update
    else:
        elapsed = 0

    if not elapsed or elapsed > speed:

        if not elapsed:
            until_next = speed
        else:
            until_next = elapsed - speed
            time.sleep(until_next)

        update()
        last_update = time.time()


def start():
    global playing, state
    playing = True
    # Launch editor mode
    if (parser.args.editor):
        os.system("/usr/share/make-snake/snake-editor/__main__.py")
        __main__.exit()
        exit()

    while playing:
        controls.update()
        if state == 1:
            step()
        elif state == 0:
            graphics.drawInitGame()
        elif state == 2:
            graphics.drawGameOver()


def stop():
    global playing, frame, last_update

    playing = False


def init():
    global state, speed, last_update

    # set the initial time for the first update with the current time
    last_update = time.time()

    game.score = 0
    game.reset()
    graphics.drawGame()
    state = 1
    try:
        speed = config.game_speed[parser.args.speed]
    except:
        speed = config.game_speed['m']

    try:
        livesIn = int(parser.args.lives)
    except:
        livesIn = 1

    if livesIn >= 1 and livesIn <= 5:
        game.lives = livesIn
        game.livesMax = livesIn
    elif livesIn > 5:
        game.lives = 5
        game.livesMax = 5
    else:
        game.lives = 1
        game.livesMax = 1


def reset():
    game.reset()
    graphics.drawGame()
