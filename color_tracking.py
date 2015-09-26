import numpy as np
import cv2

def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
camera = cv2.VideoCapture(0)
cv2.namedWindow("trackers")
cv2.createTrackbar("HL","trackers",90,179,nothing)
cv2.createTrackbar("HH","trackers",130,179,nothing)
cv2.createTrackbar("SL","trackers",90,255,nothing)
cv2.createTrackbar("SH","trackers",255,255,nothing)
cv2.createTrackbar("VL","trackers",90,255,nothing)
cv2.createTrackbar("VH","trackers",255,255,nothing)

blue = np.uint8([[[255,0,0]]])
erode_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
while camera.isOpened():
    ret,frame = camera.read()
    cv2.imshow("trackers",img)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hh = cv2.getTrackbarPos("HH","trackers")
    hl = cv2.getTrackbarPos("HL","trackers")
    sh = cv2.getTrackbarPos("SH","trackers")
    sl = cv2.getTrackbarPos("SL","trackers")
    vh = cv2.getTrackbarPos("VH","trackers")
    vl = cv2.getTrackbarPos("VL","trackers")


    lower_blue = np.array([hl,sl,vl])
    upper_blue = np.array([hh,sh,vh])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    mask_open = cv2.erode(mask,erode_kernel,iterations = 2)
    mask_dialate = cv2.dilate(mask_open,dilate_kernel, iterations = 1)
    results = cv2.bitwise_and(frame,frame,mask=mask_open)
    cv2.imshow("frame",hsv)
    cv2.imshow("mask",mask)
    cv2.imshow("result",results)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
