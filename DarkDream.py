import cv2
import random
import os
from PIL import Image 
from PIL import ImageFilter
from collections import defaultdict

srchstr =  "C:\\Users\\mysti\\Coding\\ImageConversion\\static"


contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

totch = random.randrange(totlen)

fitch = newply[totch]

fich = str(newplyd[totch])

finlst = []


for ctr in range(20):
 
    sublst = []

    for elem in range(totlen):
        tesstr = newply[elem]
        testr = str(newplyd[elem])
        piv2str = testr[-10:-8]

        if piv2str in fich:
            sublst.append(tesstr)

    if len(sublst) > 1:   

        subl = len(sublst)    

        trok = random.randrange(subl) 

        fich = sublst[trok]

        finlst.append(fich)

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = newply[totch]

        finlst.append(fich)

print(finlst)

for elem in finlst:

    img = cv2.imread(elem)

    colval = random.randrange(2)
    colval2 = random.randrange(2)

    r = img
    r[:, :, colval] = 0
    r[:, :, 1] = 0

    cv2.imwrite("image.jpg", r)
    
    imag = Image.open("image.jpg")

    ranrad = random.randrange(15,35)

    b_image = imag.filter(ImageFilter.GaussianBlur(radius=ranrad))

    b_image.show()

 


