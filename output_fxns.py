import win32gui
from PIL import ImageGrab
import numpy as np
import cv2

from util_fxns import areImgsSimilar
from input_fxns import LOCATION_DICT

WINDOW_SUBSTRING = 'MTGA'

def get_window_info():
    # set window info
    window_info = {}
    win32gui.EnumWindows(set_window_coordinates, window_info)
    return window_info


# sets L2 window coordinates
def set_window_coordinates(hwnd, window_info):
    if win32gui.IsWindowVisible(hwnd):
        if WINDOW_SUBSTRING in win32gui.GetWindowText(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            window_info['x'] = x
            window_info['y'] = y
            window_info['width'] = w
            window_info['height'] = h
            window_info['name'] = win32gui.GetWindowText(hwnd)
            window_info['hwnd'] = hwnd
            win32gui.SetForegroundWindow(hwnd)


def get_full_screen(window_info):
    x1 = window_info['x'] 
    x2 = window_info['x'] + window_info['width_fullscreen'] 
    y1 = window_info['y'] 
    y2 = window_info['y'] + window_info['height_fullscreen'] 

    return get_screenshot(window_info, x1, y1, x2, y2)

def onKeepHand(window_info):
    (x1, y1) = LOCATION_DICT['KEEP_HAND_C1']
    (x2, y2) = LOCATION_DICT['KEEP_HAND_C2']
    img = get_screenshot(window_info, x1+200, y1+150, x2+250, y2+200)

    ref_img = cv2.imread('./ref_images/keep_hand.png')
    return areImgsSimilar(img, ref_img)

def onHomeMenu(window_info):
    (x1, y1) = LOCATION_DICT['HOME_MENU_C1']
    (x2, y2) = LOCATION_DICT['HOME_MENU_C2']
    img = get_screenshot(window_info, x1, y1, x2+100, y2+50)

    ref_img = cv2.imread('./ref_images/home.png')
    return areImgsSimilar(img, ref_img)

def get_screenshot(window_info, x1, y1, x2, y2):
    win32gui.SetForegroundWindow(window_info['hwnd'])

    box = (x1, y1, x2, y2)
    screen = ImageGrab.grab(box)
    img = np.array(screen.getdata(), dtype=float).reshape((screen.size[1], screen.size[0], 3))
    img_reversed = img.copy()
    img_reversed[:,:,0] = img[:,:,2]
    img_reversed[:,:,2] = img[:,:,0]

    return img_reversed
