import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret1,frame1 = cap.read()
    ret2,frame2 = cap.read()
    ret3,frame3 = cap.read()
    ret4,frame4 = cap.read()

    if ret1:
        frame1 = cv2.resize(frame1,(600,400))
        frame2 = cv2.resize(frame2,(600,400))
        frame3 = cv2.resize(frame3,(600,400))
        frame4 = cv2.resize(frame4,(600,400))

        frame_01 = np.hstack((frame1,frame2))
        frame_02 = np.hstack((frame3,frame4))
        frame_03 = np.vstack((frame_01,frame_02))

        cv2.imshow('video player',frame_03)
        if cv2.waitKey(1)==13:
            break

cap.release()
cv2.destroyAllWindows()