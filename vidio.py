import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
_, frame = cap.read()
w = 900
h = int(frame.shape[0] * (w / float(frame.shape[1])))
size = (w, h)

fourcc = cv.VideoWriter_fourcc(*"MPEG")
fps = 30.
out = cv.VideoWriter('vidio.mp4', fourcc, fps, (640, 480))

while 1:
    ret, frame = cap.read()
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:
        break

while 1:
    ret, frame = cap.read()
    frame = cv.resize(frame, size)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv.destroyAllWindows()
