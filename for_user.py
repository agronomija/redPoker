import keyboard
import pyautogui as pt

if __name__ == '__main__':
    while True:
        if keyboard.read_key() == 'p':
            top_left = pt.position()