from utils import press_sequence
import time


def lvl5():
    moves_before_dialog = ["a", "s", "d", "f", "g", "h", "j"]
    dialog = ["{SPACE}"] * 11
    moves_after_dialog = [
        "j",
        "h",
        "g",
        "g",
        "f",
        "f",
        "d",
        "s",
        "a",
        "a",
        "q",
        "w",
        "e",
        "r",
        "t",
        "y",
        "u",
        "i",
    ]
    moves_after_second_dialog = ["i", "u", "y", "t", "r", "e", "w", "q"]

    press_sequence(moves_before_dialog)
    press_sequence(dialog, sleep=1)
    press_sequence(moves_after_dialog)
    time.sleep(2)
    press_sequence(dialog, sleep=1)
    press_sequence(moves_after_second_dialog)
