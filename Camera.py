import cv2
import os
import datetime

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

if not os.path.exists(date):
    os.makedirs(date)

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()

frame1 = cv2.resize(frame1, (1920, 1080))
frame2 = cv2.resize(frame2, (1280, 720))


