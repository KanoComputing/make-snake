#!/usr/bin/env python

# parser.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import sys
from kano.utils import run_cmd
from argparse import ArgumentParser

args = None


def init():
    global args

    parser = ArgumentParser()

    parser.add_argument("-b", "--board",
                        action="store", dest="board", default='l',
                        choices=['s', 'm', 'l'],
                        help="Board size (s | m | l)")

    parser.add_argument("-s", "--speed",
                        action="store", dest="speed", default='m',
                        choices=['s', 'm', 'f'],
                        help="Game speed (s | m | f)")

    parser.add_argument("-l", "--lives",
                        action="store", dest="lives", default="1",
                        help="Number of lives (1 | 2 | 3 | 4 | 5 )")

    parser.add_argument("-t", "--theme",
                        action="store", dest="theme", default='minimal',
                        choices=['classic', 'minimal', 'jungle', '80s', 'custom'],
                        help="Game theme (classic | minimal | jungle | 80s | custom)")

    parser.add_argument("-e", "--editor",
                        action="store_true", dest="editor", default=False,
                        help="Enter editor mode")

    parser.add_argument("-m", "--ModeTutorial",
                        action="store_true", dest="tutorial", default=False,
                        help="Closes game after game over")

    # the argument parser prints a message when an incorrect argument was given then exits
    # this will cause the screen to be cleared immediately, so we catch the exit
    try:
        args = parser.parse_args()
    except SystemExit:
        message, _, _ = run_cmd('colour_echo "    Press {{1 ENTER }} to try again."')
        print "\n    " + message
        command_prompt, _, _ = run_cmd('colour echo "    {{0>}} "')
        raw_input(command_prompt)
        sys.exit(0)
