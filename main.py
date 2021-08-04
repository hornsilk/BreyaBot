import time

from output_fxns import get_window_info, get_game_state, locate_leftmost_playable_card
from input_fxns import click_on, playCardAt

if __name__ == "__main__":

    # setup
    window_info = get_window_info()

    # game loop
    while (True):
        time.sleep(0.1)
        print('------------------------------------------------------------------')
        state = get_game_state(window_info)
        if state is not None:
            print(state)

        if state == 'PRIORITY':
            isPlayableCard, leftmost_card_pt = locate_leftmost_playable_card(window_info)
        
            if isPlayableCard:
                playCardAt(window_info, leftmost_card_pt) 
            else:
                click_on('PASS')
                click_on('OPPONENT')

        elif state == 'BLOCKING':
            click_on('PASS')

        elif state == 'ENDOFGAME':
            click_on('CENTER')

        elif state == 'HOMESCREEN':
            click_on('PLAY_GAME')

        elif state == 'MULLIGAN':
            click_on('KEEP_HAND')

        elif state == 'LOADSCREEN':
            click_on('CENTER')

        elif state == 'INACTIVE':
            time.sleep(0.5)



