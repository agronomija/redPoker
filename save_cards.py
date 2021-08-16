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
        card_screenshot = pt.screenshot(f'current_card.png', region=(16, 501, 59, 59))
        gray_card_screenshot_read = cv.imread(f'current_card.png')
        gray_card_screenshot = cv.cvtColor(gray_card_screenshot_read, cv.COLOR_BGR2GRAY)
        cv.imwrite('current_card.png', gray_card_screenshot)

        current_card = cv.imread('current_card.png')


        #newnewnewnew
        #checking if there are 4 images in suits directory already. if not, starts the process..
        if len(os.listdir('suits')) != 4:
            #takes smaller screenshot area, only to capture suit of the card
            suit_screenshot = pt.screenshot(f'current_suit.png', region=(16, 501, 30, 30))
            gray_suit_screenshot_read = cv.imread(f'current_suit.png')
            gray_suit_screenshot = cv.cvtColor(gray_suit_screenshot_read, cv.COLOR_BGR2GRAY)
            cv.imwrite('current_suit.png', gray_suit_screenshot)

            if not os.listdir('suits'):
                print('SUITS: direktorij je prazen, zato shranimo nek.png vanj')
                current = cv.imread('current_suit.png')
                lenum = random_name()
                cv.imwrite(f'suits/{lenum}.png', current)

            else:
                print('ker SUITS direktorij ni prazen gremo pregledovat ali se katera slika ujame z našo trenutno')
                for im in os.listdir('suits'):
                    #image = cv.imread(f'suits/{im}')
                    #current = cv.imread('current_suit.png')

                    if images_the_same(f'suits/{im}', 'current_suit.png'):
                        print('ker smo ujeli ujemajočo sliko, zaključimo zanko, saj to sliko že imamo v direktoriju')
                        print(im)
                        print('sliki sta enaki')
                        break
                else:
                    print('ker se slika ni ujemala z nobeno sliko iz direktorija SUITS, jo bomo shranili vanj')
                    current = cv.imread('current_suit.png')
                    lenum = random_name()
                    cv.imwrite(f'suits/{lenum}.png', current)
                #endnewendnew


        #if directory has no image files, then program automatically adds current template (current_card)
        if number_of_files('cards') == 0:
            print('SHRANIM SLIKO v CARDS, ker je ta direktorij prazen')
            cv.imwrite(f'cards/firstone.png', current_card)

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
                    print('CARDS: slika se ujema z neko sliko v direktoriju, zato prekinemo zanko')
                    break #if two photos are identical the for loop is broken becouse we know that there is already the
                    #picture of that card in cards directory


            #if there was no match while looping and comparing template image to images in directory, that means, there
            #is not a picture that is the same to template photo, so, we add image to cards directory
            else:  #newnew
                print('CARDS: slika se ne ujema z nobeno sliko v direktoriju cards, zato jo shranimo vanj')
                lenum = random_name() #gives random name in string
                #num = naked_suit() + 1
                cv.imwrite(f'cards/{lenum}.png', gray_card_screenshot)

            #when cards directory reaches lenght of 52, while loop breaks
        if number_of_files('cards') == 52:
            print('There are 52 cards in directory already...')
            break

        print('---------------------smo pred ZADNJO ZANKO:------------------------')
        for im in os.listdir('cards'):

            temp = cv.imread(f'cards/{im}')
            img = cv.imread(f'current_table.png')
            res = cv.matchTemplate(img, temp, cv.TM_CCOEFF_NORMED) #max_loc for that method
            threshold = 0.99
            #loc = np.where(res >= threshold)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            if max_val >= threshold: #if found
                print('ZADNJA ZANKA: našli smo enako sliko')
                print(f'trenutna karta: current_table.png : karta iz os.listdir(cards) {im}')
                print(f'min_val: {min_val}, max_val: {max_val}, min_loc: {min_loc}, max_loc: {max_loc}')
                print('našli smo max_val == treshold, zato zapišemo koordinate v file')
                with open('coordinates_of_images/coordinates_of_cards.csv', 'a', newline='') as f:
                    tup = max_loc
                    writer = csv.writer(f)
                    writer.writerow(tup)
            else:
                print('ZADNJA ZANKA: ni bilo zadetka')
                print(f'min_val: {min_val}, max_val: {max_val}, min_loc: {min_loc}, max_loc: {max_loc}')


            #print('-' * 50)

        print('---------------KONEC TRENUTNEGA WHILE LOOPA--------------------------------------')
        print('')


















    #image = cv.imread()




