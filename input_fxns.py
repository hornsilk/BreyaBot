
from pynput import mouse, keyboard

location_dict = {
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
    mouse.position = (x, y)
    with kboard.pressed(keyboard.Key.shift):
        kboard.press(keyboard.Key.space)
        
def click_on(item):
    try:
        (x,y) = location_dict[item]
    except FileNotFoundError as e:
        print('unknown item', item)

    click(x,y)
    print(f'{item}: clicked')

def print_coord():
    print(mouse.position)
