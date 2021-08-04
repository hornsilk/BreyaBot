import cv2
import time

from waiting import wait

from output_fxns import get_window_info, get_full_screen

if __name__ == "__main__":

    window_info = get_window_info()

    # make sure MTGA resolution is 1920x1080 and full screen
    window_info['width_fullscreen'] = 1920
    window_info['height_fullscreen'] = 1080

    img = get_full_screen(window_info)

    cv2.imwrite('./test.png',img)