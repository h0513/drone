import module
import drone as d
import output as out
import cv2 as cv
import numpy as np
import time
 
d.start()
d.vinit()
d.von()
d.vrec()
d.tfinit(model="path/model3.tflite", label="path/label.txt")
 
time.sleep(2)
for i in range(100):
    frame = d.vframe()
    dframe = d.tfdet(frame)
    cv.imshow("logo detection", dframe[1])
    cv.waitKey(1)
    time.sleep(0.5)
 
cv.destroyAllWindows()
d.vstop()
d.vclose()
