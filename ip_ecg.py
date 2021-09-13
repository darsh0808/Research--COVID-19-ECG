
import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('s',cv2.WINDOW_NORMAL)
cv2.resizeWindow('s', 1000,600)
cv2.createTrackbar('R','s',0,255,nothing)
cv2.createTrackbar('min','s',0,255,nothing)

cv2.createTrackbar('max','s',0,255,nothing)
kernel = np.ones((3,3),np.uint8)


path='Enter path of your image'

img=cv2.imread(path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while True:
    
    r = cv2.getTrackbarPos('R','s')
    mn = cv2.getTrackbarPos('min','s')
    mx = cv2.getTrackbarPos('max','s')
    _,thr=cv2.threshold(img,r,255,cv2.THRESH_BINARY)
    thr=cv2.bitwise_not(thr)
    thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel)

    thr=cv2.cvtColor(thr,cv2.COLOR_HSV2BGR)
    thr=cv2.cvtColor(thr,cv2.COLOR_BGR2GRAY)
    _,thr=cv2.threshold(thr,155,255,cv2.THRESH_BINARY)
    thr=cv2.bitwise_not(thr)
    thr = cv2.erode(thr,kernel,iterations = 1)

    cv2.imshow('s',thr)
    if cv2.waitKey(1) & 0xFF==ord('q'):
    
        
        break
    
