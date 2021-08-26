import keyboard
import pyautogui as pt
import time
from capture_picture import beep_beep
import cv2 as cv

def calculatewh(topleft, bottormright):
    """

    :param topleft: touple of mouse coordinates of top left corner of mouse position
    :param bottormright: touple of mouse coordinates of top bottom right corner of mouse position
    :return: touple w-width of our template image, h-height of our template image
    """
    x, y = topleft
    x1, y1 = bottormright
    w = x1 - x
    h = y1 - y
    return w, h


a = 10, 20
b = 30, 30
print(calculatewh(a, b))

"""
spodnji programček, je narejen zato, da si preden zaženemo main.py, približno pogledamo template,
 ki jih bomo nato uporabljali v main.py programu. če so nam slike templatov dovolj dobre,
  nato iz naslova slik x_y_w_h_ime.png ali pa iz terminala po
   končanem programu preberemo koordinati in pa width in height določenega templata.
Template naredimo tako, da zaženemo for_user.py in, nato imamo 3 sekunde časa, da odpremo željen program,
 ki ga želimo imeti na zaslonu (full screen website poker igro). Ko imamo odprto mizo za poker na full screen način,
 se lotimo izrezovanja naših templatov. To naredimo tako, da se z miško postavimo na zgornji levi kot slike, ki jo želimo izrezati
 in pritisnemo tipko 'g'. Po tem se postavimo v spodnji desni kot te slike, ki jo trenutno izrezujemo in pritisnemo tipko 'd'.
 S tem je ta template shranjen. to ponovimo še 3x, da dobimo vse željene template (karto, barvo, denar, kovanec).
 To pa mora biti nujno izvedeno v tem vrstnem redu 1.karta, 2.barva, 3.denar, 4.kovanec
 Ko smo s slikami zadovoljni, kooordinate in w in h prepišemo v main.py v funkcije capture_picture.capture_card,
 capture_picture.capture_suit, capture_picture.capture_dealer_coin, capture_picture.capture_money. Po tem lahko zaženemo 
 main.py in pričnemo z igro pokra v full screen formatu. Ob tem ob vsaki novi mizi, ali ko se pokaže turn, ali river, pritisnemo 
 tipko 'p'. Če se je program zagnal bomo vedeli s piskom. Če piska ni, to pomeni, da program še vedno melje prejšnjo nalogo, 
 ki bi morala biti končana v največ 1 minuti. Ne smemo pa pozabiti tudi na last_call_cards in last_call_suits-tudi tam je treba spremeniti parametra
 

"""
if __name__ == '__main__':
    time.sleep(3)
    beep_beep()

    print('krneki')

    im = pt.screenshot('miza.png')
    img = cv. imread('miza.png')
    cv.imwrite('proba.png', img[107:107 + 82, 427:427 + 316])
    cv.imwrite('proba2.png', img[ 427:427 + 316, 107:107 + 82])
    x, y = topleft = 0, 0
    x1, y1 = bottomright = 0, 0
    for i in range(4):
        keyboard.wait('g')

        time.sleep(0.2)
        x, y = topleft = pt.position()
        px = im.getpixel((x, y))
        print(f'X: {x}, Y: {y}, RGB: {px}')

        keyboard.wait('d')
        time.sleep(0.2)
        x1, y1 = bottomright = pt.position()
        px = im.getpixel((x1, y1))
        print(f'X: {x1}, Y: {y1}, RGB: {px}')


        #img = cv.imread('for_user.py')
        w, h = calculatewh(topleft, bottomright)
        print(w, h)
        save = img[y : y + h, x : x + w]
        if i == 0:
            print('karta')
            cv.imwrite(f'template_images/{x}_{y}_{w}_{h}_karta.png', save)
        elif i == 1:
            print('barva')
            cv.imwrite(f'template_images/{x}_{y}_{w}_{h}_barva.png', save)
        elif i == 2:
            print('denar')
            cv.imwrite(f'template_images/{x}_{y}_{w}_{h}_denar.png', save)
        elif i == 3:
            print('kovanec')
            cv.imwrite(f'template_images/{x}_{y}_{w}_{h}_kovanec.png', save)


        print('-' * 50)



