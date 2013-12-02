
# parser.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

from optparse import OptionParser

options = None


def init():
    global options

    parser = OptionParser()

    parser.add_option("-b", "--board",
                      action="store", dest="board", default='l',
                      help="Board size (s | m | l)")

    parser.add_option("-s", "--speed",
                      action="store", dest="speed", default='m',
                      help="Game speed (s | m | f)")

    parser.add_option("-f", "--fullscreen",
                      action="store_true", dest="fullscreen", default=False,
                      help="Play fullscreen")

    parser.add_option("-t", "--theme",
                      action="store", dest="theme", default='minimal',
                      help="Game theme (classic | minimal | jungle | 80s)")

    parser.add_option("-m", "--ModeTutorial",
                      action="store_true", dest="tutorial", default=False,
                      help="Closes game after game over")

    (options, args) = parser.parse_args()
