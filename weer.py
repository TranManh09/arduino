import cv2 as cv
e= int(input("n="))
f= int(input("n="))
def wer(a,b):
    return abs(a-b)<0.01

wer(e,f)