from utils import press_sequence


def lvl29():
    moves = ["a", "w", "3", "4", "e", "r", "r", "r", "s"]
    press_sequence(moves)
    moves_gray = ["x", "s"]
    press_sequence(moves_gray * 15, sleep=0.2)
    moves_after = ["e", "r", "5", "6", "y"]
    press_sequence(moves_after)
