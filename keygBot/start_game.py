import ctypes

import time

from pywinauto.application import Application
from pywinauto.keyboard import send_keys

from levels import lvl1, lvl2, lvl3,lvl4, lvl5, lvl6, lvl7, lvl8, lvl9, lvl10, lvl11, lvl12, lvl13, lvl14, lvl15, lvl16, lvl17, lvl18, lvl22, lvl23, lvl24, lvl25, lvl26, lvl27, lvl28, lvl29, lvl30, lvl31, lvl32, lvl33

GAMEPATH = r"D:/Steam/steamapps/common/keyg/keyg.exe"

SCREENSIZE = (
    ctypes.windll.user32.GetSystemMetrics(0),
    ctypes.windll.user32.GetSystemMetrics(1),
)
# print(SCREENSIZE)


def start_app():
    app = Application(backend="uia").start(GAMEPATH)
    time.sleep(3)


def start_game():
    send_keys("{ENTER}")
    time.sleep(2)


def exit_game():
    #time.sleep(15)
    send_keys("{ESC}")
    for i in range(4):
        send_keys("{DOWN}")
        time.sleep(0.5)
    send_keys("{ENTER}")

def record_screen():
    send_keys('{VK_MENU down}{VK_RWIN down}R{VK_MENU up}{VK_RWIN up}')


def main():
    start_app()
    start_game()
    time.sleep(3)

    record_screen()
    """
    lvl1.lvl1()
    time.sleep(2)
    lvl2.lvl2()
    time.sleep(2)
    lvl3.lvl3()
    time.sleep(2)
    lvl4.lvl4()
    time.sleep(2)
    lvl5.lvl5()
    time.sleep(2)
    lvl6.lvl6()
    time.sleep(2)
    lvl7.lvl7()
    time.sleep(2)
    lvl8.lvl8()
    time.sleep(2)
    lvl9.lvl9()
    time.sleep(2)
    lvl10.lvl10()
    time.sleep(2)
    lvl11.lvl11()
    time.sleep(2)
    lvl12.lvl12()
    time.sleep(2)
    lvl13.lvl13()
    time.sleep(2)
    lvl14.lvl14()
    time.sleep(2)
    lvl15.lvl15()
    time.sleep(2)
    lvl16.lvl16()
    time.sleep(2)
    lvl17.lvl17()
    time.sleep(2)
    """

    lvl18.lvl18()
    time.sleep(2)


    '''
    lvl22.lvl22()
    time.sleep(1)
    lvl23.lvl23()
    time.sleep(1)
    lvl24.lvl24()
    time.sleep(1)
    lvl25.lvl25()
    time.sleep(1)
    lvl26.lvl26()
    time.sleep(1)
    lvl27.lvl27()
    time.sleep(1)
    lvl28.lvl28()
    time.sleep(1)
    lvl29.lvl29()
    time.sleep(1)
    lvl30.lvl30()
    time.sleep(1)
    lvl31.lvl31()
    time.sleep(1)
    lvl32.lvl32()
    time.sleep(1)
    '''

    # lvl33.lvl33()

    record_screen()

    # exit_game()


