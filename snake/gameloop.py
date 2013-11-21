
import time
import graphics
import game
import config
import controls
import parser

last_update = None
playing = False
state = 0
speed = 0


def update():
    game.update()
    graphics.update()


def step():
    global last_update, speed

    cur_time = time.time()

    if last_update:
        elapsed = cur_time - last_update
    else:
        elapsed = 0

    if not elapsed or elapsed > speed:

        if not elapsed:
            until_next = speed
        else:
            until_next = elapsed - speed
            time.sleep(until_next)

        update()
        last_update = time.time()


def start():
    global playing, state

    playing = True

    init()
    while playing:
        controls.update()
        if state == 0:
            step()
        elif state == 1:
            graphics.drawGameOver()


def stop():
    global playing, frame, last_update

    playing = False


def init():
    global state, speed

    game.init()
    graphics.drawGame()
    state = 0
    speed = config.game_speed[parser.options.speed]


def reset():
    game.reset()
    graphics.drawGame()
