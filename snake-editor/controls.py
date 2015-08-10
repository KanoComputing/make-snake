
# controls.py
#
# Controls menu navigation via keys
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Contributors: https://github.com/alexaverill
#

import os
import re
import curses
import graphics
import gameloop
import menus
import theme
import __main__

keys = {
    'DOWN': 0x42,
    'LEFT': 0x44,
    'RIGHT': 0x43,
    'UP': 0x41,
    'Q': 0x71,
    'ENTER': 0x0a,
    'BACKSPACE': 0x7F,
}

menu_stack = [[menus.main, '']]
currentIdx = 0
currentMenu = menus.main
currentCategory = None
prevIndex = 0
symbolMode = False
nameMode = False
theme_name = 'custom-theme'
tile = ''


def redraw_board():
    gameloop.init()
    theme.update()  # This is going to create the new theme if it doesn't exist

    # Force the game to update
    graphics.drawGame()
    graphics.update()


def update():
    global tile, currentIdx, currentMenu, currentCategory, prevIndex, symbolMode, nameMode, theme_name, menu_stack

    key = graphics.screen.getch()

    if key > 0:
        ''' Symbol Mode '''
        if symbolMode:
            input_string(key)
            if tile == '':
                tile = '  '
            category = currentMenu[currentIdx][0]
            theme.set_tiles_theme(category, tile[:2])
            tile = ''
            redraw_board()
            symbolMode = False
            return

        ''' Enter Name for new theme '''
        if nameMode:
            input_string(key)
            theme_name = tile
            tile = ''
            # Sanitise name
            theme_name = theme_name.replace(" ", "-")  # Replaces spaces
            theme_name = re.sub(r'[^a-zA-Z0-9-]', r'', theme_name)  # Remove special characters
            theme_name = theme_name[:20]  # Trim to 20 characters
            # Crate new theme and refresh
            redraw_board()
            menus.update_naming()
            # Go back to main menu
            del menu_stack[:]
            menu_stack = [[menus.main, '']]
            menu_stack.append([menus.editMain, theme_name])
            currentMenu = menus.editMain
            currentIdx = 0
            nameMode = False
            return

        ''' Check KEYS '''
        if key == keys['DOWN']:
            currentIdx = (currentIdx + 1) % len(currentMenu)
            # Preview colors
            if currentMenu == menus.colors:
                set_color()
            elif currentMenu == menus.naming:
                # pass the saved name from the theme
                theme_name = currentMenu[currentIdx][0]
                redraw_board()
            return
        elif key == keys['UP']:
            currentIdx = (currentIdx - 1) % len(currentMenu)
            # Preview colors
            if currentMenu == menus.colors:
                set_color()
            elif currentMenu == menus.naming:
                # Pass the saved name from the theme
                theme_name = currentMenu[currentIdx][0]
                redraw_board()
            return
        elif key == keys['LEFT']:
            navigate_back()
            return
        elif key == keys['ENTER'] or key == keys['RIGHT']:
            # Back
            if (currentIdx == len(currentMenu) - 1):
                navigate_back()
                return
            # Color option
            elif currentMenu[currentIdx][1] is None:
                set_color()
                navigate_back()
                return
            # Tile option
            elif currentMenu[currentIdx][1] == "symbols":
                symbolMode = True
                return
            # Custom Name Mode
            elif currentMenu[currentIdx][1] == "name":
                nameMode = True
                return
            # Delete
            elif currentMenu[currentIdx][1] == "delete":
                delete_theme()
                return
            # Screenshot
            elif currentMenu[currentIdx][1] == "screenshot":
                take_screenshot()
                menus.editMain[3] = ["Take Screenshot [TAKEN]", "screenshot"]
                return
            # Modify existing theme
            elif currentMenu[currentIdx][1] == "existing":
                # pass the saved name from the theme
                theme_name = currentMenu[currentIdx][0]
                theme.update_name()
                redraw_board()
                graphics.update()
                title = currentMenu[currentIdx][0]
                menu_stack.append([menus.editMain, title])
                currentMenu = menus.editMain
                currentIdx = 0
                return
            # Submenu
            else:
                # Prevent Delete of custom-theme
                if currentMenu == menus.editMain and currentIdx == 2 and \
                   theme_name == os.path.splitext(theme.CUSTOM_THEME)[0]:
                    return
                prevIndex = currentIdx
                title = currentMenu[currentIdx][0]
                menu_stack.append([currentMenu[currentIdx][1], title])
                if (currentMenu == menus.board or currentMenu == menus.elements):
                    currentCategory = title
                currentMenu = currentMenu[currentIdx][1]
                currentIdx = 0
                # Preview colors
                if currentMenu == menus.colors:
                    set_color()
                # Redraw with first theme on the list
                if currentMenu == menus.naming:
                    theme_name = currentMenu[0][0]
                    redraw_board()

        elif key == keys['Q']:
            __main__.exit()


def input_string(key):
    global tile

    tile = ''
    while key != keys['ENTER']:
        if key > 0 and key != keys['ENTER']:
            if key == keys['BACKSPACE']:
                tile = tile[:-1]
            else:
                tile += curses.keyname(key)
            redraw_board()
            graphics.drawCurrentMenu()
        key = graphics.screen.getch()


def delete_theme():
    global currentIdx, currentMenu, theme_name, menu_stack

    # Load custom-theme, remove .xml extension
    theme_name = os.path.splitext(theme.CUSTOM_THEME)[0]
    # Remove .xml
    try:
        os.remove(theme.theme_file)
    except:
        pass
    # Remove .json
    json_file = os.path.splitext(theme.theme_file)[0] + '.json'
    try:
        os.remove(json_file)
    except:
        pass
    # Remove .png
    png_file = os.path.splitext(theme.theme_file)[0] + '.png'
    try:
        os.remove(png_file)
    except:
        pass
    # Go back to main menu
    del menu_stack[:]
    menu_stack = [[menus.main, '']]
    currentMenu = menus.main
    currentIdx = 0
    menus.update_naming()
    #
    redraw_board()
    graphics.drawCurrentMenu()


def take_screenshot():
    path = os.path.splitext(theme.theme_file)[0] + '.png'
    # Remove screenshot if exists
    if os.path.exists(path):
        os.remove(path)
    window_name = "Make Snake"
    # TODO: add parameter -cx,y,width,height depending on screen size
    # For 1920x1036: -c500,50,1000,800
    cmd = '/usr/bin/kano-screenshot -p %s -a %s &' % (path, window_name)
    os.system(cmd)


def navigate_back():
    global menu_stack, currentIdx, currentMenu, theme_name

    if (len(menu_stack) == 1):
        __main__.exit()
    menu_stack.pop()
    cur = menu_stack[len(menu_stack) - 1]
    currentMenu = cur[0]
    currentIdx = 0
    # Reset Screenshot title just in case
    if currentMenu == menus.editMain:
        menus.editMain[3] = ["Take Screenshot", "screenshot"]
    # Redraw with first theme on the list
    if currentMenu == menus.naming:
        theme_name = currentMenu[0][0]
        redraw_board()


def set_color():
    # Background colour is the first parameter in the menu
    if (prevIndex == 0):
        parameter = 'background'
    else:
        parameter = 'font'
    theme.set_color_theme(currentCategory, parameter, menus.colors[currentIdx][0])
    redraw_board()
    return


def get_menu_title():
    text = ['']
    dots = '.'
    for i in range(len(menu_stack) - 1):
        i += 1
        title = dots + menu_stack[i][1]
        title.strip()
        text.append(title)
        if i == 1:
            dots = ' .'
        else:
            dots = ' ' + dots
    return text
