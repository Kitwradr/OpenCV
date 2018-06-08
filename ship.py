# This file is used to detect the ship in a video.
import numpy as np
import cv2

ship_cascade = cv2.CascadeClassifier('cascade.xml')


cap = cv2.VideoCapture('sample8.mpg')

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ships = ship_cascade.detectMultiScale(gray,20,20)
    
    for (x,y,w,h) in ships:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print('x:'+str(x)+'y:'+str(y))
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()