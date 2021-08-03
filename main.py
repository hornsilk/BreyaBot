import cv2
import time

from output_fxns import get_window_info, get_full_screen
from input_fxns import click_on

if __name__ == "__main__":
    time.sleep(2)

    window_info = get_window_info()
    print(window_info)

    # make sure MTGA resolution is 1920x1080 and full screen
    window_info['width_fullscreen'] = 1920
    window_info['height_fullscreen'] = 1080
    
    full_screen = get_full_screen(window_info)
    cv2.imwrite('./test.png', full_screen)    

    print('click test')
    click_on(window_info['width']/2, window_info['height']/2)
