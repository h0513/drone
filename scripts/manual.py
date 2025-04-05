import module
from ..module import drone as d
import time as t
import keyboard as k

d.start()
d.vt()
k.add_hotkey("w", lambda: d.mf(50))
k.add_hotkey("s", lambda: d.mb(50))
k.add_hotkey("a", lambda: d.ml(50))
k.add_hotkey("d", lambda: d.mr(50))
k.add_hotkey("q", lambda: d.vu(30))
k.add_hotkey("e", lambda: d.vd(30))
t.sleep(100)
d.vl()
