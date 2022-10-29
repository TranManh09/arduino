import cv2 as cv
from cv2 import imread
from cv2 import imshow
import numpy as np
img = imread("vidu/qaz.png")
cv.imshow('abcd',img)

# lam anh xam
img_gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow("gray", img_gray)

#lam mo
#(3,3): chi ghi dc so le, dung de dieu chinh do mo
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow("anh mo", blur)

# ham tim cac canh trong anh(len den vien trang)
canny = cv.Canny(img_gray, 125,175)
cv.imshow('trangden',canny)
# lam gian hinh anh(suw ly trong anh trang den)
dilated = cv.dilate(canny, (3,3), iterations = 1)

cv.imshow('dilated',dilated)

# lam soi mon hinh anh
eroded = cv.erode(dilated, (3,3), iterations= 5)
cv.imshow('eroded',eroded)

# thay doi kich thuoc 
# (300,300) la kich thuoc anh
# interpolation dung de chia hinh anh theo ti le xem vidu.py
resize = cv.resize(canny,(300,300), interpolation= cv.INTER_AREA    )
cv.imshow('resize', resize)

# cat hinh anh
# 0:50 tu tren xuong, 0:100 hien thi hinh anh tu trai qua
cropped = img [0:50, 0: 100]
cv.imshow('cropped',cropped)


cv.waitKey(0)

cv.release()
cv.destroyAllWindows()