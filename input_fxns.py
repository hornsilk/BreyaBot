
from pynput import mouse, keyboard

mouse = mouse.Controller()
kboard = keyboard.Controller()

def click_on(x,y):
    mouse.position = (x, y)
    with kboard.pressed(keyboard.Key.shift):
        kboard.press(keyboard.Key.space)

def print_coord():
    print(mouse.position)
