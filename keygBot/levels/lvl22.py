from utils import press_sequence


def lvl22():
    moves = (
        "w",
        "a",
        "z",
        "s",
        "e",
        "r",
        "t",  #
        "y",
        "u",
        "i",
        "k",
        "l",
        "p",
        "o",
        "i",
        "k",
        ",",
        "m",
        "m",  #
        #
        "N",
        "B",
        "{SPACE}",
        "B",
        "V",
        "B",
        "N",
        "{SPACE}",
        "B",
        "V",
        "C",
        "F",
        "G",
        "H",
        "J",
        "M",
        "N",
        "B",
        "{SPACE}",
        "V",
        "B",
        "N",
        "{SPACE}",
        "B",
        "{SPACE}",
        "V",
        "C",
        "F",
        "G",
        "H",
        "J",
        "M",
        "N",
        "{SPACE}",
    )
    press_sequence(moves)

    press_sequence(["{SPACE}"] * 3)
    moves_after_dialog = ("b", "n", "m", ",")
    press_sequence(moves_after_dialog)


# todo check for failure & retry
