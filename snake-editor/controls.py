
# controls.py
#
# Controls menu navigation via keys
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
import os
import re
import curses
import __main__
import graphics
import gameloop
import menus
import theme

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
theme_name = 'custom_theme'
tile = ''


def redraw_board():
    gameloop.init()
    theme.update()  # This is going to create the new theme if it doesnt exist


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
            theme_name = theme_name.replace(" ", "_")  # Replaces spaces
            theme_name = re.sub(r'[^a-zA-Z0-9_ ]', r'', theme_name)  # Remove special characters
            theme_name = theme_name[:20]  # Trim to 20 characters
            # Crate new theme
            redraw_board()
            menus.update_naming()
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
                #pass the saved name from the theme
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
            elif currentMenu[currentIdx][1] == "delete":
                delete_theme()
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
                # Prevent Delete of custom_theme
                if currentMenu == menus.editMain and currentIdx == 2 and theme_name == theme.CUSTOM_THEME:
                    return
                prevIndex = currentIdx
                title = currentMenu[currentIdx][0]
                menu_stack.append([currentMenu[currentIdx][1],
                                   title])
                if (currentMenu == menus.board or currentMenu == menus.elements):
                    currentCategory = title
                currentMenu = currentMenu[currentIdx][1]
                currentIdx = 0
                # Preview colors
                if currentMenu == menus.colors:
                    set_color()

        elif key == keys['Q']:
            __main__.exit()
            exit()


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

    try:
        os.remove(theme.theme_file)
        theme_name = theme.CUSTOM_THEME
        redraw_board()
        menus.update_naming()
        menu_stack = [[menus.main, '']]
        currentMenu = menus.main
        currentIdx = 0
    except OSError:
        currentMenu = menus.main


def navigate_back():
    global menu_stack, currentIdx, currentMenu

    if (len(menu_stack) == 1):
        __main__.exit()
        exit()
    menu_stack.pop()
    cur = menu_stack[len(menu_stack) - 1]
    currentMenu = cur[0]
    currentIdx = 0


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
