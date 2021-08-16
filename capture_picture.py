import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np
from coordinates import naked_suit, number_of_files, images_the_same, coordinates_of_image, random_name
from random import randint, choice
import csv

#this module takes care of getting screenshot images of template images of dealer button, card, suits. Also

def capture_card(x, y, w, h):
    card_screenshot = pt.screenshot(f'card_capture.png', region=(x, y, w, h))
    gray_card_screenshot_read = cv.imread(f'card_capture.png')
    gray_card_screenshot = cv.cvtColor(gray_card_screenshot_read, cv.COLOR_BGR2GRAY)
    cv.imwrite('card_capture.png', gray_card_screenshot)


def capture_suit(x, y, w, h):
    suit_screenshot = pt.screenshot(f'suit_capture.png', region=(x, y, w, h))
    gray_suit_screenshot_read = cv.imread(f'suit_capture.png')
    gray_suit_screenshot = cv.cvtColor(gray_suit_screenshot_read, cv.COLOR_BGR2GRAY)
    cv.imwrite('suit_capture.png', gray_suit_screenshot)


def capture_dealer_coin(x,y,w,h):
    suit_screenshot = pt.screenshot(f'dealer_button.png', region=(x, y, w, h))
    gray_suit_screenshot_read = cv.imread(f'dealer_button.png')
    gray_suit_screenshot = cv.cvtColor(gray_suit_screenshot_read, cv.COLOR_BGR2GRAY)
    cv.imwrite('dealer_button.png', gray_suit_screenshot)


def mouse_coordinates(): #to approximatly get coordinates of some object on the table
    return pt.position()


while True: #when you get coordinates, you calculate w and h from it, and then put all 4 numbers in upper functions to

    key_pressed = keyboard.read_key()
    if key_pressed == 'c':
        #capture_card(16,501,20,100)
        #capture_suit(16,501,30,30)
        #capture_dealer_coin(16,501,100,20)
        print(mouse_coordinates())
        time.sleep(0.4)








