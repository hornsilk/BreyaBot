
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
}


mouse = mouse.Controller()
kboard = keyboard.Controller()

def click(x,y):
    time.sleep(abs(random.normal(0.1)))
    mouse.position = (x, y)
    time.sleep(abs(random.normal(0.5)))
    with kboard.pressed(keyboard.Key.shift):
        kboard.press(keyboard.Key.space)

def click_down(x,y):
    time.sleep(abs(random.normal(0.1)))
    mouse.position = (x, y)
    time.sleep(abs(random.normal(0.5)))
    with kboard.pressed(keyboard.Key.shift):
        kboard.press(',')

def click_up(x,y):
    time.sleep(abs(random.normal(0.1)))
    mouse.position = (x, y)
    time.sleep(abs(random.normal(0.5)))
    with kboard.pressed(keyboard.Key.shift):
        kboard.press('.')

def click_on(item):
    try:
        (x,y) = CLICK_LOCATION_DICT[item]
    except FileNotFoundError as e:
        print('unknown item', item)

    click(x,y)
    print(f'MTGA_BOT: {item} clicked')

def print_coord():
    print(mouse.position)
