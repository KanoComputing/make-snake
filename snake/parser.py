#!/usr/bin/env python

# parser.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Contributors: https://github.com/alexaverill
#

import utils
from kano.utils import run_cmd, run_bg
from argparse import ArgumentParser

args = None


class SnakeArgumentParser(ArgumentParser):

    # @Override
    def format_usage(self):
        usage_text = super(SnakeArgumentParser, self).format_usage()
        formated_usage = '\n'

        for line in usage_text.splitlines():
            formated_usage += '    ' + line + '\n'
        return formated_usage

    # @Override
    def format_help(self):
        help_text = super(SnakeArgumentParser, self).format_help()
        formated_help = '\n'

        for line in help_text.splitlines():
            formated_help += '    ' + line + '\n'
        return formated_help

    # @Override
    def error(self, message):
        self.print_usage()
        coloured_error, _, _ = run_cmd('colour_echo "{{8 x }} {{7 error: }}"')
        print "\n    " + coloured_error.strip('\n') + message + '\n'

        run_bg('echo "    `colour_echo "' + _('Press {{1 ENTER }} to try again.') + '"`"')
        raw_input()
        self.exit(2)


def init():
    global args

    parser = SnakeArgumentParser(prog='python snake')

    parser.add_argument("-b", "--board",
                        action="store", dest="board", default='l',
                        choices=['s', 'm', 'l'],
                        help=_("Board size (s | m | l)"))

    parser.add_argument("-s", "--speed",
                        action="store", dest="speed", default='m',
                        choices=['s', 'm', 'f'],
                        help=_("Game speed (s | m | f)"))

    parser.add_argument("-l", "--lives",
                        action="store", dest="lives", default=1, type=int,
                        help=_("Number of lives (1 | 2 | 3 | 4 | 5 )"))

    parser.add_argument("-t", "--theme",
                        action="store", dest="theme", default='minimal',
                        help=_("Game themes (classic | minimal | jungle | 80s ) + custom themes"))

    parser.add_argument("-p", "--print",
                        action="store_true", dest="print_themes", default=False,
                        help=_("Print all available themes"))

    parser.add_argument("-e", "--editor",
                        action="store_true", dest="editor", default=False,
                        help=_("Enter editor mode"))

    parser.add_argument("-m", "--modeTutorial",
                        action="store_true", dest="tutorial", default=False,
                        help=_("Closes game after game over"))

    parser.add_argument("-r", "--reset",
                        action="store_true", dest="reset", default=False,
                        help=_("Resets the game to challenge 1"))

    parser.add_argument("--share",
                        action="store_true", dest="share", default=False,
                        help=_("Share your favourite theme with the world"))

    args = parser.parse_args()

    # Check for share argument
    if (args.share):
        utils.share_theme()

    # Check for valid theme
    if (args.theme and args.theme != 'minimal'):
        utils.check_valid_theme(args.theme)

    # Check for --print argument
    if (args.print_themes):
        utils.print_themes()

    # Check for reset argument
    if (args.reset):
        utils.reset_game()
