import cv2
import time
import winsound
from waiting import wait

from output_fxns import get_window_info, get_full_screen, onHomeMenu, onKeepHand, locate_leftmost_playable_card, hasPriority
from input_fxns import click_on, print_coord, playCardAt

if __name__ == "__main__":

    window_info = get_window_info()

    wait(lambda: onHomeMenu(window_info), timeout_seconds=120, waiting_for='MTGA_BOT: waiting for home menu')
    while(onHomeMenu(window_info)):
        click_on('PLAY_GAME')

    wait(lambda: onKeepHand(window_info), timeout_seconds=120, waiting_for='MTGA_BOT: waiting for keep hand')
    click_on('KEEP_HAND')

    while (True):
        time.sleep(1)
        if hasPriority(window_info):
            winsound.Beep(440,500)
            isPlayableCard, leftmost_card_pt = locate_leftmost_playable_card(window_info)
        
            if isPlayableCard:
                playCardAt(window_info, leftmost_card_pt) 
            else:
                click_on('PASS')
        else:
            winsound.Beep(300,500)



        # img = get_full_screen(window_info)


