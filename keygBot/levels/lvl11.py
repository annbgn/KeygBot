from utils import press_sequence
import time


def lvl11():
    moves = ["s"]
    dialog = ["{SPACE}"] * 35
    moves_after_dialog = ["z", "x", "c"]

    press_sequence(moves)
    time.sleep(1)
    press_sequence(dialog, sleep=2)
    press_sequence(moves_after_dialog)
