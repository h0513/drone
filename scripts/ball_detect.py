import module
import drone as d
import cv2 as cv
import numpy as np
import time
 
d.start()
d.vinit()
d.von()
d.vrec("image")
 
time.sleep(2)
for i in range(100):
    frame = d.vframe()
    bframe = d.vdet(frame, "blue")
    cv.imshow("ball detection", bframe[2])
    cv.waitKey(1)
    time.sleep(0.5)
 
cv.destroyAllWindows()
d.vstop()
d.vclose()
