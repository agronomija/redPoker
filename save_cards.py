import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np


count = 0
while True:
    key_pressed = keyboard.read_key()
    if key_pressed == 'p':
        #takes screen shot of the table, than reads image trough cv,
        # than convertes it in gray color and than saves it in directory
        table_screenshot = pt.screenshot('current_table.png')

        table_image = cv.imread('current_table.png')
        gray_table_screenshot = cv.cvtColor(table_image, cv.COLOR_BGR2GRAY)
        cv.imwrite('current_table.png', gray_table_screenshot)

        #same as table screenshot, only that here takes a screenshot of a
        # region of the same picture (takes a screenshot of a card)
        card_screenshot = pt.screenshot(f'cards/current_card.png', region=(16, 501, 59, 59))
        gray_card_screenshot_read = cv.imread(f'cards/current_card.png')
        gray_card_screenshot = cv.cvtColor(gray_card_screenshot_read, cv.COLOR_BGR2GRAY)


        #if 'se ne ujema z nobeno karto':
        cv.imwrite(f'cards/suit{count}.png', gray_card_screenshot)
        count += 1




    #image = cv.imread()




