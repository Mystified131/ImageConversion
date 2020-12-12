import cv2
import random
import os
from PIL import Image 
from PIL import ImageFilter


srchstr =  "C:\\Users\\mysti\\Coding\\ImageConversion\\static"

contenttot= []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg"):

            tim = os.path.getctime(filepath)

            contenttot.append(filepath)

for elem in contenttot:

    img = cv2.imread(elem)

    r = img
    r[:, :, 0] = 0
    r[:, :, 1] = 0

    cv2.imwrite(elem, r)
    
    imag = Image.open(elem)

    ranrad = random.randrange(15,35)

    b_image = imag.filter(ImageFilter.GaussianBlur(radius=ranrad))

    b_image.show()

 


