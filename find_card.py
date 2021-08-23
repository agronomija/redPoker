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
from capture_picture import capture_card, capture_dealer_coin, capture_suit, capture_table, capture_money
from dealing_with_csv import cards_csv, suits_csv, dealer_csv, money_csv, number_of_coordinates
import winsound

filename = 'coordinates_of_images/coordinates_of_cards.csv'
def all_pos_and_cards(filename):

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        data = [row for row in reader]

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

all_pos_and_cards(filename)
temp = cv.imread('current_table.png')
print(temp.shape)




