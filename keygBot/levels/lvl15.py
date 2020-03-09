from utils import press_sequence
import time


def lvl15():
    moves= ['w', 'e', 'r', 't', 't', 't', 't',]
    moves_gray = ["r", "t"]
    moves_after_gray = ['f', 'd', 's', 'a' ]

    press_sequence(moves)
    press_sequence(moves_gray * 7, sleep=0.2)
    press_sequence(moves_after_gray, sleep=0.2)