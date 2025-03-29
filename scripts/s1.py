import module
import drone as d
import output as o
import time

d.start()
d.vt()
d.vu(50, True)
for i in range(3):
    d.mf(70)
    d.qrc(0, 4)
    o.out(f"h {i+1}: {d.dh()}")
    time.sleep(1)
d.vl()
 
