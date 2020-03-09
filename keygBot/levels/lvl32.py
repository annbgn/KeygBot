from utils import press_sequence


def lvl32():
    # moves = ['w', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'o', 'i', 'u', 'y', 't', 'r', 'r', 'f', 'd', 'd', 'f', 't', 'y', 'u', 'i', 'o', 'p']
    moves = [
        "w",
        "e",
        "r",
        "f",
        "d",
        "d",
        "f",
        "r",
        "e",
        "e",
        "r",
        "f",
        "v",
        "b",
        "b",
        "h",
        "u",
        "u",
        "y",
        "t",
        "t",
        "y",
        "u",
        "i",
        "o",
        "p",
    ]
    press_sequence(moves, sleep=0.5)
