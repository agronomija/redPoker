import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np
from random import choice, randint
import csv

method = eval('cv.TM_SQDIFF_NORMED')

def coordinates_of_image(template, image): #opencv
    """
    Func returns left top coordinates where image matched with template image
    :param template: path of template image
    :param image: path of image
    :return: tuple of coordinates where picture is located (left top corner?)
    """
    method = eval('cv.TM_SQDIFF_NORMED')
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


def number_of_files(directory):
    """
    func counts number of files in some directory defined by us
    :param directory: path of some directory where files are in
    :return: number of files in directory
    """
    return len(os.listdir(f'{directory}'))


#time.sleep(3)
#print(get_coor('cards/suit1.png'))
#print(pt.locateOnScreen('cards/suit1.png'))

def images_the_same(image1, image2):
    """compares two images if they are identical

    :param image1: path of image1
    :param image2: path of image2
    :return: True if images are the same, False if images are not the same
    """

    """
    im1 = cv.imread(image1)
    im2 = cv.imread(image2)

    if im1.shape != im2.shape:
        return False

    difference = cv.subtract(im1, im2)
    b, g, r = cv.split(difference)

    if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
        return True
    return False
    """
    im1 = cv.imread(image1)
    im2 = cv.imread(image2)

    if im1.shape != im2.shape:
        return False

    difference = cv.absdiff(im1, im2)
    d = (difference == 0).all()
    return d


#print(images_the_same('cards/firstone.png', 'current_card.png'))
#print(time.process_time())


#print(coordinates_of_image('cards/suit2.png', 'current_table.png'))
#print(time.process_time())



def random_name():
    """

    :return: returns random combination of random number and three random lettters
    """
    num = randint(1, 1000)
    letter = choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'z'])
    return f'{num}{letter}'

#im1 = cv.imread('suits/806g.png')
#im2 = cv.imread('current_suit.png')

#if im1.shape == im2.shape:
    #rint('sliki sta istih dimenzij')
#else:
    #print('sliki nista istih dimenziji')

#print(images_the_same('suits/806g.png', 'current_table.png'))

"""
print('pizda')
im1 = cv.imread('current_card.png')
im2 = cv.imread('cards/firstone.png')

print(im1.shape)
print(im2.shape)
if im1.shape != im2.shape:
    print('sliki nista istih dimenzij')
else:
    print('sliki sta enakih dimenzij')

difference = cv.absdiff(im1, im2)
#b, g, r = cv.split(difference)
print((difference == 0).all())
#print(d.sum())
print(time.process_time())
"""


