
# game.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import stage
import math
import random

snake = []
apples = []
score = 5
lives = 3


def init():
    global snake, apples_count, apples

    snake = [(-4, 1), (-3, 1), (-3, 0), (-2, 0), (-1, 0), (0, 0)]

    apples_count = 3
    if len(apples) == 0:
        apples_count += int(math.floor(getGameArea() / 1000))

        for i in range(0, apples_count):
            spawnApple()


def getGameArea():
    w = math.fabs(stage.boundaries['right'] - stage.boundaries['left'])
    h = math.fabs(stage.boundaries['top'] - stage.boundaries['bottom'])

    return int(math.floor(w * h))


def spawnApple():
    if len(apples) >= getGameArea():
        return

    x = random.randrange(stage.boundaries['left'], stage.boundaries['right'])
    y = random.randrange(stage.boundaries['top'], stage.boundaries['bottom'])

    position_free = True

    for apple in apples:
        if apple[0] == x and apple[1] == y:
            position_free = False

    for part in snake:
        if part[0] == x and part[1] == y:
            position_free = False

    if position_free and not isOutOfBoundaries(x, y):
        apples.append((x, y))
    else:
        spawnApple()


def isOutOfBoundaries(x, y):
    if x < stage.boundaries['left'] or x > stage.boundaries['right'] - 1:
        return True

    elif y < stage.boundaries['top'] or y > stage.boundaries['bottom'] - 1:
        return True

    return False
