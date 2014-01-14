
# controls.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

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
}
menu_stack = [[menus.main, '']]
currentIdx = 0
currentMenu = menus.main
currentCategory = None
prevIndex = 0
symbolMode = False
tile = ''


def update():
    global tile, currentIdx, currentMenu, currentCategory, prevIndex, symbolMode

    key = graphics.screen.getch()

    if key > 0:
        if symbolMode:
            tile = ''
            while key != keys['ENTER']:
                if key > 0 and key != keys['ENTER']:
                    tile += curses.keyname(key)
                    # Redraw
                    theme.init()
                    gameloop.init()
                    graphics.drawCurrentMenu()
                key = graphics.screen.getch()
            if tile == '':
                tile = '  '
            category = currentMenu[currentIdx][0]
            theme.set_tiles_theme(category, tile[:2])
            tile = ''
            # Redraw the board
            theme.init()
            gameloop.init()
            symbolMode = False
            return
        if key == keys['DOWN']:
            currentIdx = (currentIdx + 1) % len(currentMenu)
            # Preview colors
            if currentMenu == menus.colors:
                set_color()
            return

        elif key == keys['UP']:
            currentIdx = (currentIdx - 1) % len(currentMenu)
            # Preview colors
            if currentMenu == menus.colors:
                set_color()
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
                '''
                tile = ''
                key = ''
                while key != keys['ENTER']:
                    key = graphics.screen.getch()
                    if key > 0 and key != keys['ENTER']:
                        tile += curses.keyname(key)
                if tile == '':
                    tile = '  '
                category = currentMenu[currentIdx][0]
                theme.set_tiles_theme(category, tile[:2])
                navigate_back()
                # Redraw the board
                theme.init()
                gameloop.init()
                '''
                symbolMode = True
                return
            # Submenu
            else:
                prevIndex = currentIdx
                title = currentMenu[currentIdx][0]
                menu_stack.append([currentMenu[currentIdx][1],
                                   title])
                if(currentMenu == menus.board or
                   currentMenu == menus.elements):
                    currentCategory = title
                currentMenu = currentMenu[currentIdx][1]
                currentIdx = 0
                # Preview colors
                if currentMenu == menus.colors:
                    set_color()

        elif key == keys['Q']:
            __main__.exit()
            exit()


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
    global currentIdx, currentMenu

    if (prevIndex == 0):
        parameter = 'background'
    elif (prevIndex == 1):
        parameter = 'font'
    theme.set_color_theme(currentCategory, parameter,
                          menus.colors[currentIdx][0])
    # Redraw the board
    theme.init()
    gameloop.init()
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
