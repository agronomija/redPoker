import pyautogui as pt
import time
import os
import cv2
import sys



visina, sirina = pt.size()
print(visina, sirina)

currentMouseX, currentMouseY = pt.position()
print(currentMouseX, currentMouseY)

#pyautogui.click(1894, 12)


im = pt.locateOnScreen('chrome.png', region=(0,0, 300, 400))
if im:
    print('našli smo slikco')
    print(im)
else:
    print('nismo našli slike')

#1165,350    1313, 394
#count = 5
"""for i in range(50):
    count += 1
    ime = f'images/namizje{count}.png'
    pt.screenshot(f'{ime}', region=(16,389,67,62))"""
slovar = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []}

for image in os.listdir('images'):
    im1 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    im2 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    im3 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    im4 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    im5 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    im6 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    im7 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    im8 = pt.locateOnScreen(f'images/{image}', region=(16,389,67,62))
    cas = time.process_time()
    print(cas)
    sys.exit()







cas = time.process_time()
print(cas)






