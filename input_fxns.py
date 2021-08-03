
from pynput.mouse import Button, Controller
import time

mouse = Controller()

def click_on(x,y):
    mouse.position = (x, y)

    time.sleep(1)
    mouse.click(Button.left, 1)