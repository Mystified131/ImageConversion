import cv2
import random


def redshift(imagename, connum):

    r = imagename
    r[:, :, 0] = 0
    r[:, :, 1] = 0

    outstr = "imgh" + str(connum) + ".jpg"

    cv2.imwrite(outstr, r)

    return

def blueshift(imagename, connum):

    b = imagename
    b[:, :, 1] = 0
    b[:, :, 2] = 0

    outstr = "imgh" + str(connum) + ".jpg"

    cv2.imwrite(outstr, b)

    return

img = cv2.imread('image.jpg')

for connum in range(12):
    ranhue = random.randrange(9)
    if ranhue < 4:
        x = grayshift(img, connum)
    if ranhue > 3 and ranhue < 7:
        x = redshift(img, connum)
    if ranhue > 7:
        x = blueshift(img, connum)
