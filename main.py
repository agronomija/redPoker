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
from capture_picture import capture_card, capture_dealer_coin, capture_suit, capture_table, capture_money, beep_beep
from dealing_with_csv import cards_csv, suits_csv, dealer_csv, number_of_coordinates, money_csv
import winsound
from find_card import last_call_cards, last_call_suits

time.sleep(3)
print('zdaj')

method = eval('cv.TM_SQDIFF_NORMED') #comparison method
while True:
    key_pressed = keyboard.read_key()
    if key_pressed == 'p':
        beep_beep()
        beep_beep()
        beep_beep()
        #takes screen shot of the table, than reads image with cv,
        # than convertes it in gray color and saves it in directory
        capture_table() #takes screnshot of full screen...

        #same as table screenshot, only that here takes a screenshot of a
        # region of the same picture (takes a screenshot of a card)
        capture_card(16,501,59,59) #screenshot my left card and saves it as 'current_card.png'
                #### X,  y, W, H
        current_card = cv.imread('current_card.png')


        if not os.listdir('dealer_coin'): #screenshot of my dealer_button
            #function saves screenshot of a dealer button to dealer_coin directory
            capture_dealer_coin(1000, 501, 200, 200) #takes shot of dealer coin and saves it only when dealer_coin directory is empty

        if not os.listdir('persons_money'): #screenshot of my some persons money
            #function saves screenshot of a someones money to 'persons-money' directory
            capture_money(1000, 501, 200, 30) #takes shot of dealer coin and saves it only when dealer_coin director


        #checking if there are 4 images in suits directory already. if not, starts the process..
        if len(os.listdir('suits')) != 4:
            capture_suit(16,501,30,30)
            #takes smaller screenshot area, only to capture suit of the card


            if not os.listdir('suits'):
                print('SUITS: direktorij je prazen, zato shranimo nek.png vanj')
                current_suit = cv.imread('current_suit.png')
                lenum = random_name()
                cv.imwrite(f'suits/{lenum}.png', current_suit)

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
                if images_the_same(f'cards/{image}', 'current_card.png'):
                    print('CARDS: slika se ujema z neko sliko v direktoriju, zato prekinemo zanko')
                    break

            #if there was no match while looping and comparing template image to images in directory, that means, there
            #is not a picture that is the same to template photo, so, we add image to cards directory
            else:
                print('CARDS: slika se ne ujema z nobeno sliko v direktoriju cards, zato jo shranimo vanj')
                lenum = random_name() #gives random name in string
                current_card = cv.imread(f'current_card.png')
                cv.imwrite(f'cards/{lenum}.png', current_card)

        #od tukaj moras premaknit nazaj
        #loop that checks every table till now, and compares cards, suits and coin with image of table, and search for match in it
        #if found, it saves coordinates
        for table in os.listdir('tables'): #for every table image in 'tables' directory
            img_table = cv.imread(f'tables/{table}')

            if number_of_coordinates('coordinates_of_images/coordinates_of_cards.csv') <= 7:
                print('coor cards')
                for card in os.listdir('cards'):
                    temp_card = cv.imread(f'cards/{card}')
                    threshold = .99
                    res = cv.matchTemplate(img_table, temp_card, cv.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

                    if max_val >= threshold:
                        print(f'max val: {max_val}')
                        print(max_loc) #top left coordinates of found image
                        cards_csv(max_loc)

            if number_of_coordinates('coordinates_of_images/coordinates_of_suits.csv') <= 7:
                print('coor suit')
                for suit in os.listdir('suits'):
                    temp_suit = cv.imread(f'suits/{suit}')
                    threshold = .99
                    res = cv.matchTemplate(img_table, temp_suit, cv.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

                    if max_val >= threshold:
                        print(f'max val: {max_val}')
                        print(max_loc)  # top left coordinates of found image
                        suits_csv(max_loc)

            if number_of_coordinates('coordinates_of_images/coordinates_of_dealer.csv') <= 9:
                print('coor dealer')
                #checks for dealer_coin position on current table
                temp_dealer_coin = cv.imread(f'dealer_coin/dealer_coin.png')
                threshold = .99
                res = cv.matchTemplate(img_table, temp_dealer_coin, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

                if max_val >= threshold:
                    print(f'max val: {max_val}')
                    print(max_loc)  # top left coordinates of found image
                    dealer_csv(max_loc)


            if number_of_coordinates('coordinates_of_images/coordinates_of_money.csv') <= 9: #if there is not yet 10 positions of money in dir 'coor_...
                print('coor money')
                #checks for all money positions on current table
                temp_money = cv.imread(f'persons_money/money.png')
                #threshold = .85
                #res = cv.matchTemplate(img_table, temp_dealer_coin, cv.TM_CCOEFF_NORMED)
                #min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                """
                if max_val >= threshold:
                    print(f'max val: {max_val}')
                    print(max_loc)  # top left coordinates of found image
                    money_csv(max_loc)  #saves new coordinates to 'coordinates_pf_money.csv'
                """
                res = cv.matchTemplate(img_table, temp_money, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                threshold = 0.99
                #loc = np.where(res >= threshold)
                """
                for pt in zip(*loc[::-1]):
                    print('lokacija: ', pt)
                    money_csv(pt)
                """
                if max_val >= threshold:
                    print(f'max val: {max_val}')
                    print(max_loc)  # top left coordinates of found image
                    money_csv(max_loc)


        print(time.process_time())
        cards_in_cards = number_of_files('cards')

        print(f'There are {number_of_files("cards")} cards in cards directory')
        # when cards directory reaches lenght of 52, while loop breaks
        if number_of_files('cards') >= 52:
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            print('There are 52 cards in directory already...')
            break

        else:
            last_call_cards()
            if len(os.listdir('suits')) != 4:
                last_call_suits()
        print(time.process_time())

    else:
        continue













    """
    print(f'There are {number_of_files("cards")} cards in cards directory')
    # when cards directory reaches lenght of 52, while loop breaks
    coor_cards = 'coordinates_of_images/coordinates_of_cards.csv'
    coor_suits = 'coordinates_of_images/coordinates_of_suits.csv'
    coor_dealer = 'coordinates_of_images/coordinates_of_dealer.csv'
    coor_money = 'coordinates_of_images/coordinates_of_money.csv'
    if number_of_files('cards') == 52 and number_of_files('suits') == 4 and number_of_coordinates(coor_cards) == 7 \
            and number_of_coordinates(coor_money) == 10 and number_of_coordinates(coor_suits) == 7 \
            and number_of_coordinates(coor_dealer) == 10:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        print('There are 52 cards in directory already...')
        break
        """












