import cv2
import numpy as np

vid = cv2.VideoCapture('default.mp4')

while(True):
    ret, vid_frame = vid.read()
    filt = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2GRAY)
    filt = cv2.GaussianBlur(filt, (5, 5), 0)
    mask = cv2.inRange(filt,150,255)
    edges = cv2.Canny(mask, 190, 200)

    lines = cv2.HoughLinesP(
        edges, 1, np.pi / 180,  threshold=100,  minLineLength=100, maxLineGap=10)


    for points in lines:

        x1, y1, x2, y2 = points[0]

        cv2.line(vid_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)




    cv2.imshow('video', vid_frame)
    cv2.imshow('edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



vid.release()
cv2.destroyAllWindows()