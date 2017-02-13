#!/usr/bin/env python

# theme.py
#
# Copyright (C) 2013 - 2017 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Contributors: https://github.com/alexaverill
#

import curses
import xml.etree.ElementTree as ET
import os
import shutil
import sys
import __main__
import controls
import menus

from kano.utils import ensure_dir

CUSTOM_THEME = 'custom-theme.xml'
THEMES_DIR = os.path.expanduser('~/Snake-content')

theme_file = THEMES_DIR + '/' + CUSTOM_THEME
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
        _("Black"): (curses.COLOR_WHITE, curses.COLOR_BLACK),
        _("Red"): (curses.COLOR_WHITE, curses.COLOR_RED),
        _("Green"): (curses.COLOR_WHITE, curses.COLOR_GREEN),
        _("Yellow"): (curses.COLOR_WHITE, curses.COLOR_YELLOW),
        _("Blue"): (curses.COLOR_WHITE, curses.COLOR_BLUE),
        _("Magenta"): (curses.COLOR_WHITE, curses.COLOR_MAGENTA),
        _("Cyan"): (curses.COLOR_WHITE, curses.COLOR_CYAN),
        _("White"): (curses.COLOR_WHITE, curses.COLOR_WHITE),

    },
    "tiles": {
    }
}


def init():
    # Copy custom-theme from /usr/share if necessary
    if not os.path.exists(theme_file):
        src_file = '/usr/share/make-snake/%s' % CUSTOM_THEME
        if not os.path.exists(src_file):
            sys.exit('Error: custom-theme.xml missing from home and /usr/share/make-snake')
        ensure_dir(THEMES_DIR)
        shutil.copyfile(src_file, theme_file)
    load_theme()
    menus.update_naming()


def update():
    # Remove possible extension
    name = controls.theme_name
    if name.endswith('.xml'):
        name = os.path.splitext(name)[0]
    # Ignore 'Back'
    if name != _('Back') and name != 'webload':
        # refreshes the name before writing to the file
        update_name()
        # create file
        if not os.path.exists(theme_file):
            src_file = '/usr/share/make-snake/%s' % CUSTOM_THEME
            shutil.copyfile(src_file, theme_file)
        load_theme()


def update_name():
    global theme_file

    # Check if the file exists in Webload
    webload_file = THEMES_DIR + '/webload/' + controls.theme_name + '.xml'
    if os.path.exists(webload_file):
        theme_file = webload_file
        return
    theme_file = THEMES_DIR + '/' + controls.theme_name + '.xml'


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
        with open(theme_file):
            # Parse XML
            tree = ET.parse(theme_file)
            root = tree.getroot()
            idx = 1
            if (category == _('Background')):
                idx = 0
            elif (category == _('Snake')):
                idx = 1
            elif (category == _('Apples')):
                idx = 2
            elif (category == _('Border')):
                idx = 3
            elif (category == _('Lives')):
                idx = 4
            root[0][idx].set(parameter, value)
            tree.write(theme_file)
    except IOError:
        pass


# Category: bg, snake-body, apple, border-h, border-v, border-c, lives
def set_tiles_theme(category, value):
    try:
        with open(theme_file):
            # Parse XML
            tree = ET.parse(theme_file)
            root = tree.getroot()
            idx = 0
            if (category == _('Background symbol')):
                idx = 0
            elif (category == _('Snake body')):
                idx = 1
            elif (category == _('Apple symbol')):
                idx = 2
            elif (category == _('Horizontal symbol')):
                idx = 3
            elif (category == _('Vertical symbol')):
                idx = 4
            elif (category == _('Corner symbol')):
                idx = 5
            elif (category == _('Lives symbol')):
                idx = 6
            root[1][idx].text = value
            tree.write(theme_file)
    except IOError:
        pass


def load_theme():
    global colors_map

    try:
        with open(theme_file):
            # Parse XML
            tree = ET.parse(theme_file)
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

            colors_map = get_colors_map()

    except IOError:
        __main__.exit()


def get_curses_color(string):
    if string == N_('Black'):
        return curses.COLOR_BLACK
    elif string == N_('Red'):
        return curses.COLOR_RED
    elif string == N_('Green'):
        return curses.COLOR_GREEN
    elif string == N_('Yellow'):
        return curses.COLOR_YELLOW
    elif string == N_('Blue'):
        return curses.COLOR_BLUE
    elif string == N_('Magenta'):
        return curses.COLOR_MAGENTA
    elif string == N_('Cyan'):
        return curses.COLOR_CYAN
    else:
        return curses.COLOR_WHITE
