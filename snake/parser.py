
from optparse import OptionParser

options = None


def init():
    global options

    parser = OptionParser()

    parser.add_option("-s", "--size",
                      action="store", dest="size", default='m',
                      help="Game size (s | m | l)")

    parser.add_option("-f", "--fullscreen",
                      action="store_true", dest="fullscreen", default=False,
                      help="Play fullscreen")

    parser.add_option("-t", "--theme",
                      action="store", dest="theme", default='minimal',
                      help="Game theme (classic | minimal | jungle | 80s)")

    parser.add_option("-m", "--ModeTutorial",
                      action="store_true", dest="tutorial", default=False,
                      help="Close game after game over")

    (options, args) = parser.parse_args()
