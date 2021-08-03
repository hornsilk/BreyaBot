from test_fxns import get_window_info, get_full_screen
import cv2

WINDOW_SUBSTRING = 'MTGA'


if __name__ == "__main__":

    window_info = get_window_info()

    # make sure MTGA resolution is 1920x1080 and full screen
    window_info['width'] = 1920
    window_info['height'] = 1080
    
    full_screen = get_full_screen(window_info)
    cv2.imwrite('./test.png', full_screen)    
