import cv2
from PIL import Image
import os

cap = cv2.VideoCapture('test.mp4')
if (cap.isOpened() == False):
    print("Error opening video  file")
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
