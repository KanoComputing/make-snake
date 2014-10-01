
# graphics.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import stage
import game
import theme
import menus
import curses
import controls

screen = None
TitleXPos = -25
menuXPos = -10
menuYPos = 10
menuYInc = 2


def drawTile(x, y, tile='', color=None):
    color = color or theme.get_color('default')

    x = x * 2 + stage.padding[3] * 2 + stage.width / 2
    y += stage.padding[0] + stage.height / 2

    try:
        screen.addstr(y, x, tile, color)
        if (len(tile) < 2):
            screen.addstr(y, x + 1, tile, color)
    except:
        pass


def drawCurrentMenu():
    # Clean tiles
    for x in xrange(TitleXPos, -1 * TitleXPos):
        for y in xrange(menuYPos, 25):
            drawTile(x, y, '  ', theme.get_color('menu'))
    x = menuXPos
    idx = 0
    # Draw Menu
    # Title
    y = menuYPos - menuYInc
    auxX = TitleXPos
    for e in controls.get_menu_title():
        drawTile(TitleXPos, y, e, theme.get_color('menu'))
        if e != '' and e != '.Board' and e != '.Elements':
            drawTile(auxX, y - 1, "| ", theme.get_color('menu'))
            auxX += 1
        y += menuYInc
    y = menuYPos
    # Options
    for string in controls.currentMenu:
        # Color menu
        if controls.currentMenu == menus.colors:
            color = menus.colors[idx][0]
            if controls.currentIdx == idx:
                head = '> ['
            else:
                head = '  ['
            text = '    ] ' + string[0]
            drawTile(x, y, text, theme.get_color('menu'))
            drawTile(x, y, '    ', theme.get_color(color))
            drawTile(x, y, head, theme.get_color('menu'))
        # Symbol menu
        elif controls.symbolMode:
            if controls.currentIdx == idx:
                text = '> ' + string[0]
                if len(controls.tile) > 0:
                    text += ' : ' + controls.tile[0]
                    if len(controls.tile) > 1:
                        text += ' ' + controls.tile[1]
                        text += '   >> Press [ENTER]'
                    else:
                        text += ' _'
                else:
                    text += ' : _ _'
            else:
                text = '  ' + string[0]
            drawTile(x, y, text, theme.get_color('menu'))
        # Naming mode
        elif controls.nameMode:
            if controls.currentIdx == idx:
                text = '> ' + string[0]
                if len(controls.tile) > 0:
                    text += ' : ' + controls.tile
                else:
                    text += ' : '
            else:
                text = '  ' + string[0]
            drawTile(x, y, text, theme.get_color('menu'))
        # Rest
        else:
            if controls.currentIdx == idx:
                text = '> ' + string[0]
            else:
                text = '  ' + string[0]
            # Exception: show delete in red if theme is custom_theme
            if string[0] == 'Delete Theme' and controls.theme_name == theme.CUSTOM_THEME:
                colour = theme.get_color('Red')
            else:
                colour = theme.get_color('menu')
            drawTile(x, y, text, colour)
        y += menuYInc
        idx += 1


def drawScore():
    score_formatted = str(game.score).zfill(2)
    drawTile(
        (stage.width / 2) - 1,
        (-stage.height / 2) - 1,
        score_formatted,
        theme.get_color('border')
    )


def drawLives():
    posx = (-stage.width / 2) + 3
    for x in xrange(1, game.lives + 1):
        posx += 1
        drawTile(
            posx,
            (-stage.height / 2) - 1,
            theme.get_tile('lives'),
            theme.get_color('lives')
        )
        posx += 1
        drawTile(
            posx,
            (-stage.height / 2) - 1,
            theme.get_tile('border-h'),
            theme.get_color('border')
        )


def drawSnake():
    for part in game.snake:
        drawTile(
            part[0],
            part[1],
            theme.get_tile('snake-body'),
            theme.get_color('snake')
        )


def drawApples():
    for apple in game.apples:
        drawTile(
            apple[0],
            apple[1],
            theme.get_tile('apple'),
            theme.get_color('apple')
        )


def drawGame():
    for y in range(stage.boundaries['top'], stage.boundaries['bottom']):
        for x in range(stage.boundaries['left'], stage.boundaries['right']):
            drawTile(x, y, theme.get_tile('bg'), theme.get_color('bg'))
    drawBorders()
    drawText()


def drawBorders():
    tile_v = theme.get_tile('border-v')
    tile_h = theme.get_tile('border-h')
    tile_c = theme.get_tile('border-c')
    color = theme.get_color('border')

    x_left = stage.boundaries['left']
    x_right = stage.boundaries['right']

    y_top = stage.boundaries['top']
    y_bottom = stage.boundaries['bottom']

    for y in range(y_top, y_bottom):
        drawTile(x_left - 1, y, tile_v, color)
        drawTile(x_right, y, tile_v, color)

    for x in range(x_left, x_right):
        drawTile(x, y_top - 1, tile_h, color)
        drawTile(x, y_bottom, tile_h, color)

    drawTile(x_left - 1, y_top - 1, tile_c, color)
    drawTile(x_left - 1, y_bottom, tile_c, color)
    drawTile(x_right, y_top - 1, tile_c, color)
    drawTile(x_right, y_bottom, tile_c, color)


def drawText():
    color = theme.get_color('border')
    drawTile((stage.width / 2) - 4, (-stage.height / 2) - 1, "score:", color)
    drawTile((-stage.width / 2), (-stage.height / 2) - 1, "lives:", color)
    drawTile(-5, (stage.height / 2), " Press Q to quit ", color)


def drawHeader():
    header = []
    header.append(".-------------------------------------------------------------.")
    header.append("|  .---._____     ______     ______     ______     _____      |")
    header.append("| (  8  ____ \___/ ____ \___/ ____ \___/ ____ \___/ ____`=-   |")
    header.append("|  '---'    \_____/    \_____/    \_____/    \_____/          |")
    header.append("|   ____              _          _____    _ _ _               |")
    header.append("|  / ___| _ __   __ _| | _____  | ____|__| (_) |_ ___  _ __   |")
    header.append("|  \___ \| '_ \ / _` | |/ / _ \ |  _| / _` | | __/ _ \| '__|  |")
    header.append("|   ___) | | | | (_| |   <  __/ | |__| (_| | | || (_) | |     |")
    header.append("|  |____/|_| |_|\__,_|_|\_\___| |_____\__,_|_|\__\___/|_|     |")
    header.append("|                                                             |")
    header.append("'-------------------------------------------------------------'")
    x = (stage.width / 2) - 25
    y = (-stage.height / 2) - 15
    color = theme.get_color('menu')
    for e in header:
        drawTile(x, y, e, color)
        y += 1


def update():

    drawHeader()
    drawSnake()
    drawApples()
    drawScore()
    drawLives()


def init():
    global screen

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()
    screen.nodelay(1)


def exit():
    screen.clear()
    screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
