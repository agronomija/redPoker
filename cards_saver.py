import cv2 as cv
import time
import pyautogui as pt
import keyboard
import sys
import os
import numpy as np

#flags = [i for i in dir(cv) if i.startswith('COLOR_')]
#print( flags )

#For color conversion, we use the function cv.cvtColor(input_image, flag) where flag determines the type of conversion.

#img = cv.imread(cv.samples.findFile("starry_night.jpg"))
#cv.imwrite("starry_night.png", img)
#cv.COLOR_BGR2GRAY
#spremeni sliko v sivo
#ptime.sleep(2)
#slika = pt.screenshot('slikar.png')
#photo = cv.imread('slikar.png')
#photo = cv.cvtColor(photo, cv.COLOR_BGR2GRAY)
#cv.imwrite('slikarsiv.png', photo)
#img = cv.imread('images/namizje1.png')
#hsv = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imwrite('namizjesivo.png', img)
#cv.imwrite('namizjesivohsv.png', hsv)
#print(time.process_time())

#res = cv.matchTemplate(img,template,method)
#img = cv.imread('slikarsiv.png',0)
#template = cv.imread('namizjesivo.png',0)
#w, h = template.shape[::-1]
#print(w, h)
#res = cv.matchTemplate(img,template, cv.TM_SQDIFF)
#img = cv.imread('namizje.png', 1)
#tag = img[0:200, 0:200]
#img[500:700, 700:900] = tag
#cv.imshow('kopija', img)
#cv.waitKey(0)


#import keyboard  # using module keyboard
#img = cv.imread('krneki.png')
#cv.imshow('slikar', img)
#k = cv.waitKey(0)



def number_of_files(directory):
    return len(os.listdir(f'{directory}'))


def convert_to_gray(image_path):
    image = cv.imread(image_path)
    image_copy = image.copy()
    cv.cvtColor(image_copy, cv.COLOR_BGR2GRAY)






if number_of_files('images') == 0:
    print('no files in directory')
else:
    print('directory is not empty')


method = eval('cv.TM_SQDIFF_NORMED') #comparison method
count = 6
while True:
    pressed_key = keyboard.read_key()  #my pressed key on keyboard
    if pressed_key == "p":
        print("You pressed p, so i made screenshot and saved it in current directory as table_screenShot.png")
        screen_shot = pt.screenshot(f'table_screenShot.png') #makes a screenhot and saves it in current memory
        img = cv.imread(f'table_screenShot.png')
        hsv = cv.cvtColor(img, cv.COLOR_BGR2GRAY)





        for image in os.listdir('newimages'):
            print(image)
            image_copy = cv.imread(f'newimages/{image}')

            #cv.imshow('ime slike', image_copy)
            #cv.waitKey(0)
            gray_image = cv.cvtColor(image_copy, cv.COLOR_BGR2GRAY) #image to gray image that can be compared later with hsv image
            res = cv.matchTemplate(hsv, gray_image, method)
            if res[0][0] < 0.9:
                cv.imwrite(f'newimages/table_screenShot{count}.png', hsv)

            if all(res[0][0])


            print(res[0])
            print(res)

            threshold = 0.99
            loc = np.where(res >= threshold)
            print(loc)



        if number_of_files('newimages') == 52:
            print('imamo 52 slik...')
            break
        #cv.imshow('table_screenShot', img)
        count += 1















