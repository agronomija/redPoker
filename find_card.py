import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np
from coordinates import number_of_files, images_the_same, coordinates_of_image, random_name, list_of_coordinates, \
    coordinates_of_image_last_call, images_the_same_last_call
from random import randint, choice
import csv
from capture_picture import capture_card, capture_dealer_coin, capture_suit, capture_table, capture_money
from dealing_with_csv import cards_csv, suits_csv, dealer_csv, money_csv, number_of_coordinates
import winsound

"""
filename = 'coordinates_of_images/coordinates_of_cards.csv'
def all_pos_and_cards(filename):

    with open(filename, 'r') as file: #odpremo neko datoteko csv s kooordinatami
        reader = csv.reader(file)

        data = [row for row in reader] #seznam koordinat

        for card in os.listdir('cards'): #karta v dir cards
            print(card)
            template = cv.imread(f'cards/{card}') #preberemo karto
            l, w, h = template.shape[::-1] #dimenzije karte
            
            for x, y in data: #koordinata v csv
                print(x,y)
                img = cv.imread('current_table.png') #slika mize, kjer iscemo template
                roi = img[int(x):int(x)+w, int(y):int(y)+h] #slika del mize, kjer so karte
                cv.imwrite('part_image.png', roi) #shranimo ta del mize
                trenutna_karta = f'cards/{card}'
                if not images_the_same(trenutna_karta, 'part_image.png'):
                    count = 0
                    for image in os.listdir('cards'):
                        druga_karta = f'cards/{image}'
                        if images_the_same(druga_karta, trenutna_karta):
                            print('sliki sta isti')
                            break
                    else:
                        print('zapisujem')
                        cv.imwrite('dodana.png', roi)

"""


def last_call_cards():
    """
    func opens csv file with coordinaes of images, then loops trough directory of 'tables', and for every table in 'tables'
    directory loops trough over all coordinates. With these coordinates and lc, hc we cut template image out of table image.
    Then function compares this template image to every image in 'cards' directory and if there is no match, we save this
    template image to 'cards' directory.
    :return: None, saves new card in 'cards' dir if there is not yet saved this card image
    """
    lc, hc = card_l_h = 59, 59 #lenght and height of cards
    #ls, hs = suit_l_h = 30, 30 #lenght and height of suits

    coor_cards = list_of_coordinates('coordinates_of_images/coordinates_of_cards.csv')
    #coor_suits = list_of_coordinates('coordinates_of_images/coordinates_of_suits.csv')
    #coor_money = list_of_coordinates('coordinates_of_images/coordinates_of_money.csv')
    for table in os.listdir('tables'):
        img_table = cv.imread(f'tables/{table}')

        for x, y in coor_cards: #for every coordinate in 'coordinates_of_cards.csv'
            x = int(x)
            y = int(y)
            card = img_table[y:y + lc, x:x+hc]
             #part of main image

            for saved_card in os.listdir('cards'): #for every card in 'cards' directory
                card1 = cv.imread(f'cards/{saved_card}') #read card
                if images_the_same_last_call(card, card1):
                    print('našli smo isto karto zato break')
                    break
            else:
                cv.imwrite(f'cards/{random_name()}.png', card)



def last_call_suits():
    """
        func opens csv file with coordinaes of images, then loops trough directory of 'tables', and for every table in 'suits'
        directory loops trough over all coordinates. With these coordinates and lc, hc we cut template image out of table image.
        Then function compares this template image to every image in 'cards' directory and if there is no match, we save this
        template image to 'suits' directory.
        :return: None, saves new card in 'cards' dir if there is not yet saved this suit image
        """
    #lc, hc = card_l_h = 59, 59 #lenght and height of cards
    ls, hs = suit_l_h = 30, 30 #lenght and height of suits

    #coor_cards = list_of_coordinates('coordinates_of_images/coordinates_of_cards.csv')
    coor_suits = list_of_coordinates('coordinates_of_images/coordinates_of_suits.csv')
    #coor_money = list_of_coordinates('coordinates_of_images/coordinates_of_money.csv')

    for table in os.listdir('tables'):
        img_table = cv.imread(f'tables/{table}')

        for x, y in coor_suits: #for every coordinate in 'coordinates_of_cards.csv'
            x = int(x)
            y = int(y)
            suit = img_table[y:y + ls, x:x+hs]
            #part of main image

            for saved_suit in os.listdir('suits'): #for every card in 'cards' directory
                suit1 = cv.imread(f'suits/{saved_suit}') #read card
                if images_the_same_last_call(suit, suit1):
                    print('našli smo isto karto zato break')
                    break
            else:
                cv.imwrite(f'suits/{random_name()}.png', suit)



if __name__ == '__main__':
    #last_call_cards()
    im = cv.imread('suits/375p.png')
    print(im.shape)


            #suit = cv.imread(img_table[x:x+hs, y:y + ls])




"""
img_table = 'current_table'
print('krneki', cv.imread('current_table.png')[16:66, 500:560])
#[16:66, 500:560]
img_firstone = cv.imread('cards/firstone.png')
print(img_firstone.shape)
"""


