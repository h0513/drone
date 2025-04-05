import module
import drone as d
import output as out
import cv2 as cv
import numpy as np
import time
 
d.start()
d.vinit()
d.von()
d.vrec("photo")
 
time.sleep(2)
for i in range(100):
    frame = d.vframe()
    cv.imshow("Ball Detection", bframe[2])
    cv.waitKey(1)
    time.sleep(0.5)
 
cv.destroyAllWindows()
d.vstop()
d.vclose()
