from utils import press_sequence


def lvl25():
    moves_before_dialog = ["x", "c", "v", "b"]
    skip_dialog = ["{SPACE}"]
    moves_inter_dialog = ["g", "h", "n", "j", "k", "i"]
    moves_inter_dialog2 = ["l", ","]
    moves_after_dialog = ["o", "p"]
    press_sequence(
        moves_before_dialog
        + skip_dialog * 7
        + moves_inter_dialog
        + skip_dialog * 3
        + moves_inter_dialog2
        + skip_dialog * 4
        + moves_after_dialog
    )
