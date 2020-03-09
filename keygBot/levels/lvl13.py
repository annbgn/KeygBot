from utils import press_sequence
import time


def lvl13():
    moves = [
        "a",
        "z",
    ]
    moves2 = ["s", "s", "z", "a", "w", "e", "w", "a", "z", "x"]

    press_sequence(moves)
    time.sleep(1.5)
    press_sequence(moves2)
    time.sleep(1.5)
    press_sequence(["s"])
    time.sleep(1.25 * 3)
    press_sequence(["d"])
    # time.sleep(3+1.5)
    # press_sequence(["d"])
