import cv2
import time

from output_fxns import get_window_info, get_full_screen
from input_fxns import click_on, print_coord

if __name__ == "__main__":

    window_info = get_window_info()

    # make sure MTGA resolution is 1920x1080 and full screen
    window_info['width_fullscreen'] = 1920
    window_info['height_fullscreen'] = 1080



    # print_coord()

    time.sleep(1)
    click_on('PLAY_GAME')
    time.sleep(1)
    click_on('PLAY_GAME')
    time.sleep(1)
    click_on('PLAY_GAME')

    time.sleep(15)

    click_on('PLAY_FIRST')

    time.sleep(5)
    
    click_on('KEEP_HAND')

    while (True):
        time.sleep(1)
        click_on('PASS')

