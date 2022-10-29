import cv2 as cv
import numpy as np
from cv2 import imread 
import dlib

img = imread('vidu/qaz.png')
cv.imshow('img', img)

a=img.shape[2:3]
print(a)

    


cv.waitKey(0)