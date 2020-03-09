from utils import press_sequence
import time
import ctypes
import datetime
import time

from numpy import *
from PIL import ImageGrab, ImageOps
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

GAMEPATH = r"D:/Steam/steamapps/common/NO THING/no_thing.exe"

SCREENSIZE = (
    ctypes.windll.user32.GetSystemMetrics(0),
    ctypes.windll.user32.GetSystemMetrics(1),
)


def lvl18():
    # naming: celllocation_from_herolocation
    # from_up
    for _ in range(100):

        up_from_up = ImageGrab.grab(bbox=(970, 290, 980, 340))
        right_from_up = ImageGrab.grab(bbox=(1460, 625, 1510, 635))
        down_from_up = ImageGrab.grab(bbox=(970, 940, 980, 990))
        left_from_up = ImageGrab.grab(bbox=(410, 625, 460, 635))

        up_from_up_array = array(up_from_up.getcolors())
        right_from_up_array = array(right_from_up.getcolors())
        down_from_up_array = array(down_from_up.getcolors())
        left_from_up_array = array(left_from_up.getcolors())

        uu = up_from_up_array#.sum()
        ru = right_from_up_array#.sum()
        du = down_from_up_array#.sum()
        lu = left_from_up_array#.sum()

        print('uu = {}\nru = {}\ndu = {}\nlu = {}'.format(uu, ru, du, lu))
        time.sleep(0.5)

# NOTES
'''
i cant get why we always grab [[500 (255, 255, 255)]]
does it mean white?
why when making a screen with win+prtsc but not win+alt+prtsc we get a white image
is it caused by the same reason?
how to avoid this?
'''