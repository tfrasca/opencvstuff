import numpy as np
import cv2

camera = cv2.VideoCapture(0)
camera.read()
#for x in xrange(19):
#    print camera.get(x)
frame_width = int(camera.get(3))
frame_height = int(camera.get(4))
print frame_width,frame_height
while camera.isOpened():
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.line(gray,(0,0),(10,640),(0,255,0),5)
    cv2.circle(gray,((frame_width/2),(frame_height/2)),50,(0,255,0),-1)
    cv2.rectangle(gray,(frame_width/4,frame_height/4),(frame_width*3/4,frame_height*3/4),(0,255,2),3)
    cv2.imshow("frame",gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


print camera.isOpened()
camera.release()
print camera.isOpened()
cv2.destroyAllWindows()
