from configparser import Interpolation
from sre_constants import SUCCESS
from cv2 import COLOR_BAYER_BG2BGR, COLOR_BAYER_BG2GRAY, COLOR_LAB2BGR, VideoCapture, cvtColor, waitKey
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np



cap = VideoCapture(0)
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]* scale)
    height= int(frame.shape[0]* scale)
    dimension = (width, height)
    return cv2.resize ( frame, dimension, interpolation = cv2.INTER_AREA#chỉnh size
    )
#waitKey(0)

while True:
    SUCCESS, frame = cap.read()
    frame_resize = rescaleFrame(frame, scale=.5)
    cv2.imshow("video",frame)
    cv2.imshow("videoq",frame_resize)
    if SUCCESS:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("video_gray", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.release()
cv2.destroyAllWindows()