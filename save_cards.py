import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np
from coordinates import naked_suit, number_of_files, images_the_same
#print((3,3,3) == (2,2,2))
#print(cv.imread('cards/suit0.png'))
#print(cv.imread('cards/suit0.png').shape == cv.imread('current_card.png').shape)
#print('-' * 50)
#print(cv.imread('current_card.png').shape)
time.sleep(3)
print('zdaj')



method = eval('cv.TM_SQDIFF_NORMED') #comparison method

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
        card_screenshot = pt.screenshot(f'current_card.png', region=(850, 440, 59, 59))
        gray_card_screenshot_read = cv.imread(f'current_card.png')
        gray_card_screenshot = cv.cvtColor(gray_card_screenshot_read, cv.COLOR_BGR2GRAY)
        cv.imwrite('current_card.png', gray_card_screenshot)

        current_card = cv.imread('current_card.png')

        #if directory has no image files, then program automatically adds current template (current_card)
        if number_of_files('cards') == 0:
            cv.imwrite(f'cards/suit1.png', current_card)

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
                    #print('-' * 50)
                    #table_image = cv.imread('current_table.png')
                    #res = cv.matchTemplate(im, table_image, method)  # at this method we take min_loc
                    #min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

                    #print(f'min_val: {min_val}, max_val: {max_val}, min_loc: {min_loc}, max_loc: {max_loc}')
                    #print('-' * 50)
                    #print('Images are the same')

                    break #if two photos are identical the for loop is broken becouse we know that there is already the
                    #picture of that card in cards directory


            #if there was no match while looping and comparing template image to images in directory, that means, there
            #is not a picture that is the same to template photo, so, we add image to cards directory
            else:
                num = naked_suit() + 1
                cv.imwrite(f'cards/suit{num}.png', gray_card_screenshot)

            #when cards directory reaches lenght of 52, while loop breaks
            if number_of_files('cards') == 52:
                print('There are 52 cards in directory already...')
                break




            for im in os.listdir('cards'):
                if images_the_same(f'cards/{im}', 'current_card.png'):

                    print('sliki sta enaki')
                else:
                    print('sliki sta razlicni')
            print(time.process_time())


















    #image = cv.imread()




