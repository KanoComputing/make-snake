#!/usr/bin/env python

# parser.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

from argparse import ArgumentParser

args = None


def init():
    global args

    parser = ArgumentParser()

    parser.add_argument("-b", "--board",
                        action="store", dest="board", default='l',
                        help="Board size (s | m | l)")

    parser.add_argument("-s", "--speed",
                        action="store", dest="speed", default='m',
                        help="Game speed (s | m | f)")

    parser.add_argument("-t", "--theme",
                        action="store", dest="theme", default='minimal',
                        help="Game theme (classic | minimal | jungle | 80s | custom)")

    parser.add_argument("-m", "--ModeTutorial",
                        action="store_true", dest="tutorial", default=False,
                        help="Closes game after game over")

    parser.add_argument("-e", "--editor",
                        action="store_true", dest="editor", default=False,
                        help="Enter editor mode")

    parser.add_argument("-l", "--lives",
                        action="store", dest="lives", default="1",
                        help="Number of lives (1 | 2 | 3 | 4 | 5 )")

    args = parser.parse_args()
