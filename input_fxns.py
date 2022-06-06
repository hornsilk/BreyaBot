
from pynput import mouse, keyboard

import time
from numpy import random

CLICK_LOCATION_DICT = {
    'PLAY_GAME': (1390, 800),
    'PLAY_FIRST': (888, 502),
    'KEEP_HAND':(900, 695),
    'LEFTMOST_HAND': (412, 806),
    'DECK': (177, 773),
    'PASS': (1422, 758),
    'OPPONENT': (765, 82),
    'CENTER': (720, 400),
    'DIALOG_DONE': (720, 700),
    'RIGHT_EDGE': (1534, 466),
}


mouse = mouse.Controller()
kboard = keyboard.Controller()

def click(x,y):
    time.sleep(abs(random.normal(0.1)))
    mouse.position = (x, y)
    time.sleep(abs(random.normal(0.1)))
    with kboard.pressed(keyboard.Key.shift):
        kboard.press(keyboard.Key.space)

def click_down(x,y):
    time.sleep(abs(random.normal(0.1)))
    mouse.position = (x, y)
    time.sleep(abs(random.normal(0.1)))
    with kboard.pressed(keyboard.Key.shift):
        kboard.press(',')

def click_up(x,y):
    time.sleep(abs(random.normal(0.1)))
    mouse.position = (x, y)
    time.sleep(abs(random.normal(0.1)))
    with kboard.pressed(keyboard.Key.shift):
        kboard.press('.')

def click_on(item):
    try:
        (x,y) = CLICK_LOCATION_DICT[item]
    except FileNotFoundError as e:
        print('unknown item', item)

    click(x,y)
    print(f'BreyaBot: {item} clicked')

def move_card(x1, y1, x2, y2):
    click_down(x1,y1)
    click_up(x2,y2)
    print(f'BreyaBot: moved card from ({int(x1)},{int(y1)}) -> ({int(x2)},{int(y2)})')


def print_coord():
    print(mouse.position)

def playCardAt(window_info, card_tl_corner):
    x1 = card_tl_corner[0]
    y1 = card_tl_corner[1]

    if x1 > 700:
        x1 -= random.randint(70,120)
    elif x1 < 500:
        x1 -= random.randint(40,100)
        y1 -= random.randint(10,50)

    x_center = window_info['width'] / 2
    y_center = window_info['height'] / 2

    move_card(x1, y1, x_center, y_center)
