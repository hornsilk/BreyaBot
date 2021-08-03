from test_fxns import get_window_info, get_full_screen
import cv2

WINDOW_SUBSTRING = 'MTGA'


if __name__ == "__main__":

    window_info = get_window_info()

    
    # make sure MTGA resolution is 1024 x 576
    print(window_info)
    
    full_screen = get_full_screen(window_info)
    cv2.imwrite('./test.png', full_screen)    
