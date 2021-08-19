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


# we are looking if some card from directory cards, matches with some saved table and if it did,
# we take out coordinates and save them to coordinates_of_dealer.csv
for im in os.listdir('cards'):
    for table in os.listdir('tables'):
        temp = cv.imread(f'cards/{im}')
        img = cv.imread(f'tables/{table}')
        threshold = 0.99
        res = cv.matchTemplate(img, temp, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        # we get all lines out of
        with open('coordinates_of_images/coordinates_of_cards.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            print(data)

        x = [max_loc[0], max_loc[1]]
        print(x)
        if max_val >= threshold and x not in data:
            print('ZADNJA ZANKA: našli smo enako sliko')
            print(f'trenutna karta: current_table.png : karta iz os.listdir(cards) {im}')
            print(f'min_val: {min_val}, max_val: {max_val}, min_loc: {min_loc}, max_loc: {max_loc}')
            print('našli smo max_val == treshold, zato zapišemo koordinate v file')
            with open('coordinates_of_images/coordinates_of_cards.csv', 'a', newline='') as f:
                tup = max_loc
                writer = csv.writer(f)
                writer.writerow(tup)

print('---------------KONEC TRENUTNEGA WHILE LOOPA--------------------------------------')
print('')