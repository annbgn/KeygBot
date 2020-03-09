from utils import press_sequence
import time


def lvl33():
    moves = ["w", "a", "z", "x", "s", "d", "d", "s"]
    press_sequence(moves, sleep=0.5)
    press_sequence(["x"], sleep=2)
    moves_after_button_clicked = ["c", "x", "z", "a", "w", "e", "r", "d"]  # , 'd', 'f']
    press_sequence(moves_after_button_clicked, sleep=0.5)
    time.sleep(3.3)
    press_sequence(["d", "f"])
