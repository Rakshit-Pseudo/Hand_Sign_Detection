import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgsize = 300
counter = 0

folder = "C:\\Users\\DELL\\OneDrive\\Desktop\\HSD_Project\\Data\\ILU"

while True :
    success , img = cap.read()
    hands , img = detector.findHands(img)
    if hands :
        hand = hands [0]
        x,y,w,h = hand ['bbox']

        imgWhite = np.ones((imgsize,imgsize,3),np.uint8)*255

        imgCrop = img[y-offset : y + h + offset , x-offset : x + w + offset]
        imgCropShape = imgCrop.shape

        aspectratio = h/w

        if aspectratio > 1 :
            k = imgsize / h
            wcal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop , (wcal , imgsize))
            imgResizeShape = imgResize.shape
            wgap = math.ceil((imgsize - wcal) / 2)
            imgWhite[: ,wgap : wcal + wgap] = imgResize

        else :
            k = imgsize / w
            hcal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop , (imgsize, hcal))
            imgResizeShape = imgResize.shape
            hgap = math.ceil((imgsize - hcal) / 2)
            imgWhite[hgap : hcal + hgap , : ] = imgResize

        cv2.imshow('ImageCrop', imgCrop)
        cv2.imshow('ImageWhite', imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s') :
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg' , imgWhite)
        print(counter)