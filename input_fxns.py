
from pynput import mouse, keyboard


LOCATION_DICT = {
    'PLAY_GAME': (1390, 800),
    'PLAY_FIRST': (888, 502),
    'KEEP_HAND':(900, 695),
    'LEFTMOST_HAND': (412, 806),
    'DECK': (177, 773),
    'PASS': (1422, 758),
    'HOME_MENU_C1': (71, 0),
    'HOME_MENU_C2': (218, 50),
    'KEEP_HAND_C1': (808, 684),
    'KEEP_HAND_C2': (1015, 722),
}


mouse = mouse.Controller()
kboard = keyboard.Controller()

def click(x,y):
    mouse.position = (x, y)
    with kboard.pressed(keyboard.Key.shift):
        kboard.press(keyboard.Key.space)
        
def click_on(item):
    try:
        (x,y) = LOCATION_DICT[item]
    except FileNotFoundError as e:
        print('unknown item', item)

    click(x,y)
    print(f'MTGA_BOT: {item} clicked')

def print_coord():
    print(mouse.position)
