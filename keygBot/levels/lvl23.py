from utils import press_sequence


def lvl23():
    moves_before_dialog = ["s", "d", "f"]
    skip_dialog = ["{SPACE}"] * 24
    moves_after_dialog = ["g", "h", "j"]
    press_sequence(moves_before_dialog + skip_dialog + moves_after_dialog)
