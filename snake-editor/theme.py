#!/usr/bin/env python

# theme.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import curses
import xml.etree.ElementTree as ET
import kano.profile as kp

app_dir = kp.get_app_data_dir('make-snake')
custom_file = app_dir + '/custom_theme'
colors_map = {}
theme = {
    "colors": {
        "default": (curses.COLOR_WHITE, curses.COLOR_BLACK),
        "bg": (curses.COLOR_WHITE, curses.COLOR_WHITE),
        "snake": (curses.COLOR_RED, curses.COLOR_GREEN),
        "apple": (curses.COLOR_RED, curses.COLOR_RED),
        "border": (curses.COLOR_WHITE, curses.COLOR_YELLOW),
        "lives": (curses.COLOR_RED, curses.COLOR_RED),
        "menu": (curses.COLOR_WHITE, curses.COLOR_BLACK),
        "Black": (curses.COLOR_WHITE, curses.COLOR_BLACK),
        "Red": (curses.COLOR_WHITE, curses.COLOR_RED),
        "Green": (curses.COLOR_WHITE, curses.COLOR_GREEN),
        "Yellow": (curses.COLOR_WHITE, curses.COLOR_YELLOW),
        "Blue": (curses.COLOR_WHITE, curses.COLOR_BLUE),
        "Magenta": (curses.COLOR_WHITE, curses.COLOR_MAGENTA),
        "Cyan": (curses.COLOR_WHITE, curses.COLOR_CYAN),
        "White": (curses.COLOR_WHITE, curses.COLOR_WHITE),

    },
    "tiles": {
    }
}


def init():
    global theme, colors_map

    load_custom_theme()
    colors_map = get_colors_map()


def get_color(key):
    return curses.color_pair(colors_map.get(key, 0))


def get_tile(key):
    return theme['tiles'].get(key, ' ')


def get_colors_map():
    out = {}

    i = 1
    for col in theme['colors'].iteritems():
        curses.init_pair(i, col[1][0], col[1][1])
        out[col[0]] = i
        i += 1

    return out


# Category: bg, snake, apple, border, lives
# Parameter: background, font
def set_color_theme(category, parameter, value):
    try:
        with open(custom_file):
            # Parse XML
            tree = ET.parse(custom_file)
            root = tree.getroot()
            idx = 1
            if (category == 'Background'):
                idx = 0
            elif (category == 'Snake'):
                idx = 1
            elif (category == 'Apples'):
                idx = 2
            elif (category == 'Border'):
                idx = 3
            elif (category == 'Lives'):
                idx = 4
            root[0][idx].set(parameter, value)
            tree.write(custom_file)
    except IOError:
        pass


# Category: bg, snake-body, apple, border-h, border-v, border-c, lives
def set_tiles_theme(category, value):
    try:
        with open(custom_file):
            # Parse XML
            tree = ET.parse(custom_file)
            root = tree.getroot()
            idx = 0
            if (category == 'Background symbol'):
                idx = 0
            elif (category == 'Snake body'):
                idx = 1
            elif (category == 'Apple symbol'):
                idx = 2
            elif (category == 'Horizontal symbol'):
                idx = 3
            elif (category == 'Vertical symbol'):
                idx = 4
            elif (category == 'Corner symbol'):
                idx = 5
            elif (category == 'Lives symbol'):
                idx = 6
            root[1][idx].text = value
            tree.write(custom_file)
    except IOError:
        pass


def load_custom_theme():

    try:
        with open(custom_file):
            # Parse XML
            tree = ET.parse(custom_file)
            root = tree.getroot()
            # Colors
            theme['colors']['bg'] = (get_curses_color(root[0][0].attrib.get('font')),
                                     get_curses_color(root[0][0].attrib.get('background')))
            theme['colors']['snake'] = (get_curses_color(root[0][1].attrib.get('font')),
                                        get_curses_color(root[0][1].attrib.get('background')))
            theme['colors']['apple'] = (get_curses_color(root[0][2].attrib.get('font')),
                                        get_curses_color(root[0][2].attrib.get('background')))
            theme['colors']['border'] = (get_curses_color(root[0][3].attrib.get('font')),
                                         get_curses_color(root[0][3].attrib.get('background')))
            theme['colors']['lives'] = (get_curses_color(root[0][4].attrib.get('font')),
                                        get_curses_color(root[0][4].attrib.get('background')))
            # Tiles
            theme['tiles']['bg'] = root[1][0].text
            theme['tiles']['snake-body'] = root[1][1].text
            theme['tiles']['apple'] = root[1][2].text
            theme['tiles']['border-h'] = root[1][3].text
            theme['tiles']['border-v'] = root[1][4].text
            theme['tiles']['border-c'] = root[1][5].text
            theme['tiles']['lives'] = root[1][6].text

    except IOError:
        pass


def get_curses_color(string):
    if string == 'Black':
        return curses.COLOR_BLACK
    elif string == 'Red':
        return curses.COLOR_RED
    elif string == 'Green':
        return curses.COLOR_GREEN
    elif string == 'Yellow':
        return curses.COLOR_YELLOW
    elif string == 'Blue':
        return curses.COLOR_BLUE
    elif string == 'Magenta':
        return curses.COLOR_MAGENTA
    elif string == 'Cyan':
        return curses.COLOR_CYAN
    else:
        return curses.COLOR_WHITE
