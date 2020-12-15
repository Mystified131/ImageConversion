import cv2
import random
import os
from PIL import Image 
from PIL import ImageFilter
from collections import defaultdict

srchstr =  "C:\\Users\\mysti\\Coding\\ImageConversion\\static"


finlst = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg") :

            finlst.append(str(filepath))

for elem in finlst:

    img = cv2.imread(elem)

    colval = random.randrange(2)
    colval2 = random.randrange(2)

    r = img
    r[:, :, colval] = 0
    r[:, :, 1] = 0

    cv2.imwrite(elem, r)
    
    imag = Image.open(elem)

    ranrad = random.randrange(15,35)

    b_image = imag.filter(ImageFilter.GaussianBlur(radius=ranrad))

    b_image.save(elem)

 


