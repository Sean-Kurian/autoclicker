#!/usr/bin/env python3
import pyautogui
import random
import time
from pynput.keyboard import *

#  ======== settings ========
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.f3
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by Sean Kurian")
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            random.seed(time.time())
            pyautogui.PAUSE = 0.75 + 0.5*random.random()
    lis.stop()


if __name__ == "__main__":
    main()
