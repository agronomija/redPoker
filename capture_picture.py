import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np
from coordinates import number_of_files, images_the_same, coordinates_of_image, random_name
from random import randint, choice
import csv

#this module takes care of getting screenshot images of template images of dealer button, card, suits. Also

def capture_table():
    """ func takes screenshot of all screen (red star poker should be opened full screen. then convertes image into
    gray color and saves it back again in 'current_table' an also saves the same picture in 'tables/random_name.png'
        :return: func takes full screenshot and saves one copy of it in 'current_table.png' and second copy to
        'tables/some_name.png'
    """

    table_screenshot = pt.screenshot('current_table.png')
    table_image = cv.imread('current_table.png')
    gray_table_screenshot = cv.cvtColor(table_image, cv.COLOR_BGR2GRAY)
    cv.imwrite('current_table.png', gray_table_screenshot)
    title = 'tables/' + random_name() + '.png'
    cv.imwrite(title, gray_table_screenshot)


def capture_card(x, y, w, h):
    """ func takes screenshot of part of the image from 'current_card.png'. The x,y,h and w are defined by us.


    :param x: top left x coordinate of captured part of image
    :param y: top left y coordinate of captured part of image
    :param w: width of captured part of image
    :param h: height of captured part of image
    :return: func takes a screenshot of part of an image and then saves it to 'card_capture.png'
    """
    card_screenshot = pt.screenshot(f'current_card.png', region=(x, y, w, h))
    gray_card_screenshot_read = cv.imread(f'current_card.png')
    gray_card_screenshot = cv.cvtColor(gray_card_screenshot_read, cv.COLOR_BGR2GRAY)
    cv.imwrite('current_card.png', gray_card_screenshot)


def capture_suit(x, y, w, h):
    """ func takes screenshot of part of the image from 'current_suit.png'. The x,y,h and w are defined by us.

        :param x: top left x coordinate of captured part of image
        :param y: top left y coordinate of captured part of image
        :param w: width of captured part of image
        :param h: height of captured part of image
        :return: func takes a screenshot of part of an image and then saves it to 'suit_capture.png'
        """
    #suit_screenshot = pt.screenshot(f'suit_capture.png', region=(x, y, w, h))
    #gray_suit_screenshot_read = cv.imread(f'suit_capture.png')
    #gray_suit_screenshot = cv.cvtColor(gray_suit_screenshot_read, cv.COLOR_BGR2GRAY)
    #cv.imwrite('suit_capture.png', gray_suit_screenshot)

    suit_screenshot = pt.screenshot(f'current_suit.png', region=(x, y, w, h))
    gray_suit_screenshot_read = cv.imread(f'current_suit.png')
    gray_suit_screenshot = cv.cvtColor(gray_suit_screenshot_read, cv.COLOR_BGR2GRAY)
    cv.imwrite('current_suit.png', gray_suit_screenshot)


def capture_dealer_coin(x,y,w,h):
    """ func takes screenshot of part of the image from f'dealer_coin/dealer_coin.png'.
    The x,y,h and w are defined by us.

            :param x: top left x coordinate of captured part of image
            :param y: top left y coordinate of captured part of image
            :param w: width of captured part of image
            :param h: height of captured part of image
            :return: func takes a screenshot of part of an image and then saves it to 'suit_capture.png'
    """
    card_screenshot = pt.screenshot(f'dealer_coin/dealer_coin.png', region=(x, y, w, h))
    gray_card_screenshot_read = cv.imread(f'dealer_coin/dealer_coin.png')
    gray_card_screenshot = cv.cvtColor(gray_card_screenshot_read, cv.COLOR_BGR2GRAY)
    cv.imwrite('dealer_coin/dealer_coin.png', gray_card_screenshot)


def capture_money(x, y, w, h):
    """ func takes screenshot of part of the image from f'dealer_coin/dealer_coin.png'.
    The x,y,h and w are defined by us.

            :param x: top left x coordinate of captured part of image
            :param y: top left y coordinate of captured part of image
            :param w: width of captured part of image
            :param h: height of captured part of image
            :return: func takes a screenshot of part of an image and then saves it to 'persons_money/money.png'
    """
    money_screenshot = pt.screenshot(f'persons_money/money.png', region=(x, y, w, h))
    gray_money_screenshot_read = cv.imread(f'persons_money/money.png')
    gray_money_screenshot = cv.cvtColor(gray_money_screenshot_read, cv.COLOR_BGR2GRAY)
    cv.imwrite(f'persons_money/money.png', gray_money_screenshot)




def mouse_coordinates(): #to approximatly get coordinates of some object on the table
    return pt.position()



if __name__ == '__main__':
    temp = cv.imread(f'card_capture.png')
    for im in os.listdir('tables'):

        img = cv.imread(f'tables/{im}')

        threshold = 0.99
        roi = img[500:600, 16: 100]
        res = cv.matchTemplate(roi, temp, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if max_val >= threshold:
            print(max_loc)

    print(time.process_time())
    while True:
        key = keyboard.read_key()
        if key == 'b':
            print(mouse_coordinates())
            time.sleep(0.2)



#1. first get coordinates of where you want to cut pictures.




