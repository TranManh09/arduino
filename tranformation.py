import cv2 as cv

import numpy as np
from cv2 import imread 

img = imread('vidu/qaz.png')
cv.imshow('img', img)

def traslate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])# ma tran diem anh(lay diem anh) M
    dimensions = (img.shape[1], img.shape[0])# dung de lay dia chi hinh anh. chieu cao img.shape[0], chieu rong img.shape[1] so kenh[2]
    return cv.warpAffine(img, transmat, dimensions)# lenh dung thay doi kich thuoc diem anh

translated = traslate(img,100,50)
cv.imshow('translated',translated)



# xoay hinh
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
         rotPoint = (width//2, height//2)
    rotMat = cv. getRotationMatrix2D(rotPoint, angle, 1.0)# lenh dung de xoay diem anh(tam, goc, ty le)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated= rotate(img, 90)
cv.imshow('rotated', rotated)

cv.waitKey(0)