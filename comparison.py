import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('newimages/table_screenShot5.png',0)
img2 = img.copy()
template = cv.imread('chrome.png',0)
w, h = template.shape[::-1]
print('začetek')

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']



img = img2.copy()
method = eval('cv.TM_SQDIFF_NORMED') #s to metodo išče, za to metodo vzamemo top_left = min_loc
# Apply template Matching
res = cv.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
print(f'min_val: {min_val}, max_val: {max_val}, min_loc: {min_loc}, max_loc: {max_loc}')
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum


threshold = 0.8
loc = np.where( res >= threshold)
print(loc)
print(type(loc))


top_left = min_loc
print(f'top left: {top_left}')
print(f'top_left: matchana koordinata... (w, h)')


bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img,top_left, bottom_right, 255, 2)

print('zdaj sem tukaj')
plt.subplot(121),plt.imshow(res,cmap = 'gray')
cv.waitKey(0)
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(method)
    #cv.waitKey(0)
plt.show()
    #cv.waitKey(0)

