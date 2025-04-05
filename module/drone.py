import pyhula as hula
import output as out
import video as vid
import detect as det
import keyboard
from typing import Dict, Union, List
import numpy as np
import cv2


led: Dict[str, Dict[str, int]] = {
    "n": {'g': 0, 'b': 0, 'r': 0, 'mode': 1}, # null
    "g": {'g': 0, 'b': 0, 'r': 255, 'mode': 1}, # green
    "c": {'g': 255, 'b': 0, 'r': 255, 'mode': 1}, # cyan
    "b": {'g': 255, 'b': 0, 'r': 0, 'mode': 1}, # blue
    "r": {'g': 0, 'b': 255, 'r': 0, 'mode': 1}, # red
    "p": {'g': 255, 'b': 255, 'r': 0, 'mode': 1}, # purple
    "y": {'g': 0, 'b': 255, 'r': 255, 'mode': 1}, # yellow
    "w": {'g': 255, 'b': 255, 'r': 255, 'mode': 1} # white
}
PPREF: bool = False

def start(vb: bool=True):
    print()
    out.inf("starting new drone session")
    if vb: out.inf("starting drone")
    suc = True
    if not connect(vb): suc = False
    if not pref(True, vb): suc = False
    if vb and suc: out.suc("completed drone startup")
    if vb and not suc: out.err(3)
    keyboard.add_hotkey("ctrl+space", lambda: vl())
    return 0

def connect(vb: bool=True):
    if vb: out.inf("initiating connection to drone")
    global api
    api = hula.UserApi()
    ckcon(True, True)
    if ckcon():
        if vb: out.suc("completed drone connection")
        return 1
    else: return 0

def ckcon(ins: bool=False, vb: bool=False):
    if not "api" in globals():
        if vb: out.err(5)
        connect()
    if not "pcon" in globals():
        if vb: out.err(6)
        global pcon
        pcon = False
        if vb: out.suc("completed pcon variable global definition")
    if globals()["pcon"] == True and not ins:
        if vb: out.suc("completed drone connection using pcon")
        return 1
    if not api.connect():
        if vb: out.err(1)
        pcon = False
        return 0
    else:
        if vb: out.suc("drone successfully connected without pcon")
        pcon = True
        return 1

def pref(ins=True, vb=True):
    if not ckcon():
        return 0
    if vb: out.inf("conducting preflight check")
    if not ins and PPREF:
        if vb: out.suc("completed preflight check using ppref")
        return 0
    else:
        bat = api.get_battery()
        suc = False
        if (bat < 10): out.err(2)
        elif (bat < 20): out.err(3)
        else: suc = True
        if vb: out.suc(f"preflight check completed [battery: {bat}]")
        PPREF = True
        if suc: return 1
        else: return 0

def mf(ds=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm forwards with led {led}")
        api.single_fly_forward(ds, led)
        if vb: out.suc(f"completed {ds}cm forwards motion with led {led}")

def mb(ds=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm backwards with led {led}")
        api.single_fly_back(ds, led)
        if vb: out.suc(f"completed {ds}cm backwards motion with led {led}")

def ml(ds=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm left with led {led}")
        api.single_fly_left(ds, led)
        if vb: out.suc(f"completed {ds}cm left motion with led {led}")

def mr(ds=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm right with led {led}")
        api.single_fly_right(ds, led)
        if vb: out.suc(f"completed {ds}cm right motion with led {led}")

def vt(vb=False, led=led["y"]):
    if ckcon():
        if vb: out.inf(f"taking off with led {led}")
        api.single_fly_takeoff(led)
        if vb: out.suc(f"completed takeoff with led {led}")

def vl(vb=False, led=led["y"]):
    if ckcon():
        if vb: out.inf(f"landing with led {led}")
        api.single_fly_touchdown(led)
        if vb: out.suc(f"completed landing with led {led}")

def vh(t=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"hovering for {t}s with led {led}")
        api.single_fly_hover_flight(t, led)
        if vb: out.suc(f"hovered for {t}s with led {led}")

def vu(ds=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm up with led {led}")
        api.single_fly_up(ds, led)
        if vb: out.suc(f"completed {ds}cm up motion with led {led}")

def vd(ds=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm down with led {led}")
        api.single_fly_down(ds, led)
        if vb: out.suc(f"completed {ds}cm down motion with led {led}")

def rl(an=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"turning {an} degree left with led {led}")
        api.single_fly_turnleft(an, led)
        if vb: out.suc(f"completed {an} degree left turn with led {led}")

def rr(an=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"turning {an} degree right with led {led}")
        api.single_fly_turnright(an, led)
        if vb: out.suc(f"completed {an} degree right turn with led {led}")

def cf(r=0, vb=False, led=led["n"]):
    if ckcon():
        if vb: out.inf(f"flying {r}cm r circular path with led {led}")
        api.single_fly_radius_around(r, led)
        if vb: out.suc(f"completed {r}cm r circular path with led {led}")

def dh(vb=False):
    if ckcon():
        if vb: out.inf("getting drone tof height")
        h = api.get_plane_ds()
        if vb: out.suc(f"completed drone tof height detection [output: {h}]")
        return h

def qra(id=0, md=0, vb=False):
    if ckcon():
        if vb: out.inf(f"aligning to qr {id} using mode {md}")
        suc = api.single_fly_Qrcode_align(md, id)
        if suc: out.suc(f"completed alignment to qr {id} using mode {md}")
        else: out.err(7)

def qrr(id=0, md=0, vb=False):
    if ckcon():
        if vb: out.inf(f"recognising qr {id} using mode {md}")
        suc = api.single_fly_recognition_Qrcode(md, id)
        if suc[0]: out.suc(f"completed recognition of qr {id} using mode {md}")
        else: out.err(8)
        return suc

def qrt(t=0, id=0, md=0, vb=False):
    if ckcon():
        if vb: out.inf(f"tracking qr {id} for {t}s")
        suc = api.single_fly_track_Qrcode(id, t)
        if suc: out.suc(f"completed tracking of qr {id} for {t}s")
        else: out.err(9)

def ll(pset="-1", t=0, r=0, g=0, b=0, md=1, vb=False):
    if ckcon():
        if not pset == "-1":
            if vb: out.inf(f"setting led color to {led[pset]} for {t}s")
            suc = api.single_fly_lamplight(led[pset]["r"], led[pset]["g"], led[pset]["b"], t, md)
            if suc and vb: out.suc(f"completed setting led color to {led[pset]} for {t}s")
            else: out.err(10)
        else:
            if vb: out.inf(f"setting led color to r: {r}, g: {g}, b: {b} for {t}s")
            suc = api.single_fly_lamplight(r, g, b, t, md)
            if suc and vb: out.suc(f"completed setting led color to r: {r}, g: {g}, b: {b} for {t}s")
            else: out.err(10)

def fly(func, sf=True, vb=False):
    if sf: func = "single_fly_" + func
    func = "api." + func
    if ckcon():
        if vb: out.inf("executing", func)
        exec(func)
        if vb: out.inf("completed", func)

def vinit(vb=False):
    if ckcon():
        if vb: out.inf("initialising video")
        global v
        v = vid.hula_video(hula_api=api)
        if vb: out.suc("completed video initalisation")

def vc(vb=False):
    if ckcon():
        if vb: out.inf("closing video stream")
        v.close()
        if vb: out.suc("completed video stream closing")

def von(vb=False):
    if ckcon():
        if vb: out.inf("starting video stream")
        v.video_mode_on()
        if vb: out.suc("completed video")

def vrec(file, vb=False):
    if ckcon():
        if vb: out.inf("starting video recording")
        v.start_recording(file)
        if vb: out.suc("stored video recording")

def vstop(vb=False):
    if ckcon():
        if vb: out.inf("stopping video recording")
        v.stop_recording()
        if vb: out.suc("stopped video recording")

def vsize(vb=False):
    if ckcon():
        if vb: out.inf("getting video resolution")
        vr = v.get_image_size()
        if vb: out.suc("completed video resolution retrieval")
        return vr

def vsr(vb=False):
    if ckcon():
        if vb: out.inf("stoping live display")
        v.stop_live()
        if vb: out.suc("stopped live display")

def vframe(vb=False):
    if ckcon():
        if vb: out.inf("getting video frame")
        frame = v.get_video()
        if vb: out.suc("completed getting video frame")
        return frame

def vdec(frame, color):
    colors = {
        'blue': (np.array([100, 150, 70]), np.array([140, 255, 255])),
        'red': (np.array([0, 90, 100]), np.array([10, 255, 255])),
        'green': (np.array([40, 100, 100]), np.array([80, 255, 255])),
        'yellow': (np.array([20, 100, 100]), np.array([30, 255, 255])),
        'purple': (np.array([130, 100, 100]), np.array([160, 255, 255])),
    }
    if color not in colors: raise ValueError(f"Color '{color}' is not defined. Available colors: {list(colors.keys())}")
    lower_hsv, upper_hsv = colors[color]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_color = cv2.inRange(hsv, lower_hsv, upper_hsv)
    contours, _ = cv2.findContours(mask_color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        center_x = x + w // 2
        center_y = y + h // 2
        cv2.drawContours(frame, [largest_contour], -1, (255, 0, 0), 3)
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
        return center_x, center_y, frame
    else:
        return None, None, frame

def tfinit(model):
    if ckcon():
        global td
        td = det.tflite_detector(model)

def tfdet(frame):
    if ckcon():
        nframe = td.detect(frame)
        return nframe
