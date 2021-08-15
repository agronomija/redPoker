import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np
#print((3,3,3) == (2,2,2))
#print(cv.imread('cards/suit0.png'))
#print(cv.imread('cards/suit0.png').shape == cv.imread('current_card.png').shape)
#print('-' * 50)
#print(cv.imread('current_card.png').shape)

def number_of_files(directory):
    return len(os.listdir(f'{directory}'))


method = eval('cv.TM_SQDIFF_NORMED') #comparison method
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
        card_screenshot = pt.screenshot(f'current_card.png', region=(16, 501, 59, 59))
        gray_card_screenshot_read = cv.imread(f'current_card.png')
        gray_card_screenshot = cv.cvtColor(gray_card_screenshot_read, cv.COLOR_BGR2GRAY)
        cv.imwrite('current_card.png', gray_card_screenshot)

        current_card = cv.imread('current_card.png')


        if number_of_files('cards') == 0:
            cv.imwrite(f'cards/suit{count}.png', current_card)
            count += 1


        else:
            #loops trough directory and compares images from directory to template,
            #if there is some same card in directory as tempplate one, then loop breaks, but if it loops till the end and
            #doestn match with any of the images, than it saves an image in cards directory.
            #when there is 52 cards in directory, the work is done
            for image in os.listdir('cards'):
                im = cv.imread(f'cards/{image}')

                #res = cv.matchTemplate(current_card, im, method)

                #if im.shape == current_card.shape:
                    #print("The images have same size and channels")

                difference = cv.subtract(im, current_card)
                b, g, r = cv.split(difference)
                #print(b)
                #print(g)
                #print(r)
                if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
                    print('-' * 50)
                    table_image = cv.imread('current_table.png')
                    res = cv.matchTemplate(im, table_image, method)  # at this method we take min_loc
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

                    print(f'min_val: {min_val}, max_val: {max_val}, min_loc: {min_loc}, max_loc: {max_loc}')
                    print('-' * 50)
                    break


            else:
                cv.imwrite(f'cards/suit{count}.png', gray_card_screenshot)
                count += 1


            if number_of_files('images') == 52:
                print('There are 52 cards in directory already...')
                break












    #image = cv.imread()




