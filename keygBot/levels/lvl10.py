from utils import press_sequence
import time


def lvl10():
    moves = ["w"]
    dialog_STAR = ["{SPACE}"] * 8
    moves_after_STAR = ["q", "a", "z", "z", "x", "c", "d"]
    dialog_PAUSE = ["{SPACE}"] * 3
    moves_after_PAUSE = ["c", "f"]
    dialog_TIME = ["{SPACE}"] * 4
    moves_after_TIME = ["c", "v", "b"]
    dialog_ETERNITY = ["{SPACE}"] * 3
    moves_after_ETERNITY = ["v", "g", "t", "y", "u", "j", "i"]
    dialog_PLAY = ["{SPACE}"] * 5
    moves_after_PLAY = ["j", "k", "l"]
    dialog_EQUAL = ["{SPACE}"] * 3
    moves_after_EQUAL = ["k", "j", "m"]
    dialog_SHARP = ["{SPACE}"] * 4
    moves_after_SHARP = ["j", "k", ","]

    press_sequence(moves)
    time.sleep(2)
    press_sequence(dialog_STAR, sleep=1.5)
    press_sequence(moves_after_STAR)
    time.sleep(2)
    press_sequence(dialog_PAUSE, sleep=1.5)
    press_sequence(moves_after_PAUSE)
    time.sleep(2)
    press_sequence(dialog_TIME, sleep=1.5)
    press_sequence(moves_after_TIME)
    time.sleep(2)
    press_sequence(dialog_ETERNITY, sleep=1.5)
    press_sequence(moves_after_ETERNITY)
    time.sleep(2)
    press_sequence(dialog_PLAY, sleep=1.5)
    press_sequence(moves_after_PLAY)
    time.sleep(2)
    press_sequence(dialog_EQUAL, sleep=1.5)
    press_sequence(moves_after_EQUAL)
    time.sleep(2)
    press_sequence(dialog_SHARP, sleep=1.5)
    press_sequence(moves_after_SHARP)
