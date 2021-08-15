import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np

method = eval('cv.TM_SQDIFF_NORMED')


def coordinates_of_image(template, image): #cv
    """
    Func returns left top coordinates where image matched with template image
    :param template: path of template image
    :param image: path of image
    :return: tuple of coordinates where picture is located (left top corner?)
    """
    image = cv.imread(image)
    temp = cv.imread(template)
    res = cv.matchTemplate(image, temp, method)  # at this method we take min_loc
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    return min_loc, max_loc


def get_coor(image): #pyautogui
    """

    :param image: path of template image
    :return: coordinates
    """
    image = pt.locateOnScreen('cards/suit1.png')
    return

#print(coordinates_of_image('cards/suit0.png', 'current_table.png'))


def naked_suit():  #returns number of the title image
    if len(os.listdir('cards')) == 0:
        return 0
    last_one = os.listdir('cards')[-1]
    #print(last_one)
    first_part = last_one.split('.')[0]
    #print(first_part)
    number = ''
    #print(number)
    for i in last_one:
        if i.isnumeric():
            number += i
    return int(number)




def number_of_files(directory):
    return len(os.listdir(f'{directory}'))


#time.sleep(3)
#print(get_coor('cards/suit1.png'))
#print(pt.locateOnScreen('cards/suit1.png'))

def images_the_same(image1, image2):
    im1 = cv.imread(f'{image1}')
    im2 = cv.imread(f'{image2}')

    difference = cv.subtract(im1, im2)
    b, g, r = cv.split(difference)

    if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
        return True
    return False

#print(images_the_same('cards/suit1.png', 'cards/suit1.png'))
#print(time.process_time())


#print(coordinates_of_image('cards/suit2.png', 'current_table.png'))
#print(time.process_time())
