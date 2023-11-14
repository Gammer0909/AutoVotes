import pyautogui
import keyboard
import time

while keyboard.is_pressed('q') == False:
    print(pyautogui.position())
    time.sleep(1)