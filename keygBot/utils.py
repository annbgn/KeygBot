import time
from typing import Sequence

from pywinauto.keyboard import send_keys
import random

def restart_game():
    pass

# todo important to
def check_failure():
    pass


def press_sequence(moves: Sequence, sleep: float = 0.3):
    for i in moves:
        send_keys(i, vk_packet=False)
        # print(i)
        time.sleep(sleep)

def press_random(moves: Sequence, sleep: float=0.3):
    '''
    here i have to press a rendom button from a "moves" list while lvl is not passed
    todo check failure
    todo check win
    '''
    pass
