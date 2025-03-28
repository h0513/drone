import pyhula as hula
import output as out
import keyboard

led = [
    {'r': 0, 'g': 0, 'b': 0, 'mode': 1}, # null
    {'r': 255, 'g': 0, 'b': 0, 'mode': 1}, # red
    {'r': 255, 'g': 255, 'b': 0, 'mode': 1}, # yellow
    {'r': 0, 'g': 255, 'b': 0, 'mode': 1}, # green
    {'r': 0, 'g': 0, 'b': 255, 'mode': 1}, # blue
    {'r': 0, 'g': 255, 'b': 255, 'mode': 1}, # cyan
    {'r': 255, 'g': 0, 'b': 255, 'mode': 1}, # magenta
    {'r': 255, 'g': 255, 'b': 255, 'mode': 1} # white
]
ppref = False

def start(vb=True):
    print()
    out.inf("starting new drone session")
    if vb: out.inf("starting drone")
    suc = True
    if not connect(): suc = False
    if not pref(): suc = False
    if vb and suc: out.suc("completed drone startup")
    if vb and not suc: out.err(3)
    keyboard.add_hotkey("alt+f3", lambda: vl())
    return 0

def connect(vb=True):
    if vb: out.inf("initiating connection to drone")
    global api
    api = hula.UserApi()
    if vb: out.suc("completed drone connection")
    ckcon(True, True)
    if ckcon(): return 1
    else: return 0

def ckcon(ins=False, vb=False):
    if not "api" in globals():
        if vb: out.err(5)
        connect()
    if not "pckcon" in globals():
        if vb: out.err(6)
        global pckcon
        pckcon = False
        if vb: out.suc("completed pckcon variable global definition")
    if pckcon == True and not ins:
        if vb: out.suc("completed drone connection")
        return 1
    if not api.connect():
        if vb: out.err(1)
        pckcon = False
        return 0
    else:
        if vb: out.suc("drone successfully connected")
        pckcon = True
        return 1

def pref(ins=True, vb=True):
    if not ckcon():
        return 0
    if vb: out.inf("preflight check starting")
    if not ins and ppref:
        if vb: out.suc("completed preflight check")
        return 0
    else:
        bat = api.get_battery()
        suc = True
        if (bat < 10): out.err(2)
        elif (bat < 20): out.err(3)
        else: suc = False
        if vb: out.suc(f"preflight check completed [battery: {bat}]")
        if suc: return 0
        else: return 1

def mf(distance=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {distance}cm forwards with led {led}")
        api.single_fly_forward(distance, led)
        if vb: out.suc(f"completed {distance}cm forwards motion with led {led}")
    else: out.err(1)

def mb(distance=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {distance}cm backwards with led {led}")
        api.single_fly_back(distance, led)
        if vb: out.suc(f"completed {distance}cm backwards motion with led {led}")
    else: out.err(1)

def ml(distance=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {distance}cm left with led {led}")
        api.single_fly_left(distance, led)
        if vb: out.suc(f"completed {distance}cm left motion with led {led}")
    else: out.err(1)

def mr(distance=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {distance}cm right with led {led}")
        api.single_fly_right(distance, led)
        if vb: out.suc(f"completed {distance}cm right motion with led {led}")
    else: out.err(1)

def vt(vb=False, led=led[0]):
    ll(2, 1)
    if ckcon():
        if vb: out.inf(f"taking off with led {led}")
        api.single_fly_takeoff(led)
        if vb: out.suc(f"completed takeoff with led {led}")
    else: out.err(1)

def vl(vb=False, led=led[0]):
    ll(2, 1)
    if ckcon():
        if vb: out.inf(f"landing with led {led}")
        api.single_fly_touchdown(led)
        if vb: out.suc(f"completed landing with led {led}")
    else: out.err(1)

def vh(time=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"hovering for {time}s with led {led}")
        api.single_fly_hover_flight(time, led)
        if vb: out.suc(f"hovered for {time}s with led {led}")
    else: out.err(1)

def vu(distance=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {distance}cm up with led {led}")
        api.single_fly_up(distance, led)
        if vb: out.suc(f"completed {distance}cm up motion with led {led}")
    else: out.err(1)

def vd(distance=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {distance}cm down with led {led}")
        api.single_fly_down(distance, led)
        if vb: out.suc(f"completed {distance}cm down motion with led {led}")
    else: out.err(1)

def rl(angle=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"turning {angle} degree left with led {led}")
        api.single_fly_turnleft(angle, led)
        if vb: out.suc(f"completed {angle} degree left turn with led {led}")
    else: out.err(1)

def rr(angle=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"turning {angle} degree right with led {led}")
        api.single_fly_turnright(angle, led)
        if vb: out.suc(f"completed {angle} degree right turn with led {led}")
    else: out.err(1)

def cf(radius=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"flying {radius}cm radius circular path with led {led}")
        api.single_fly_radius_around(radius, led)
        if vb: out.suc(f"completed {radius}cm radius circular path with led {led}")
    else: out.err(1)

def dh(vb=False):
    if ckcon():
        if vb: out.inf("getting drone tof height")
        h = api.get_plane_distance()
        if vb: out.suc(f"completed drone tof height detection [output: {h}]")
        return h
    else: out.err(1)

def qra(id=0, md=0, vb=False):
    if ckcon():
        if vb: out.inf(f"aligning to qr {id} using mode {md}")
        suc = api.single_fly_Qrcode_align(md, id)
        if suc: out.suc(f"completed alignment to qr {id} using mode {md}")
        else: out.err(7)
    else: out.err(1)

def qrr(id=0, md=0, vb=False):
    if ckcon():
        if vb: out.inf(f"recognising qr {id} using mode {md}")
        suc = api.single_fly_recognition_Qrcode(md, id)
        if suc[0]: out.suc(f"completed recognition of qr {id} using mode {md}")
        else: out.err(8)
        return suc
    else: out.err(1)

def qrt(t=0, id=0, md=0, vb=False):
    if ckcon():
        if vb: out.inf(f"tracking qr {id} for {t}s")
        suc = api.single_fly_track_Qrcode(id, t)
        if suc: out.suc(f"completed tracking of qr {id} for {t}s")
        else: out.err(9)
    else: out.err(1)

def ll(pset=0, t=0, r=0, g=0, b=0, md=1, vb=False):
    if ckcon():
        if not pset == -1:
            if vb: out.inf(f"setting led color to {r}, {g}, {b} for {t}s")
            suc = api.single_fly_lamplight(led[pset]["r"], led[pset]["g"], led[pset]["b"], t, md)
            if suc: out.suc(f"completed setting led color to {r}, {g}, {b} for {t}s")
            else: out.err(10)
        else:
            if vb: out.inf(f"setting led color to {r}, {g}, {b} for {t}s")
            suc = api.single_fly_lamplight(r, g, b, t, md)
            if suc: out.suc(f"completed setting led color to {r}, {g}, {b} for {t}s")
            else: out.err(10)
    else: out.err(1)

def fly(func, sf=True, vb=False):
    if sf: func = "single_fly_" + func
    func = "api." + func
    if ckcon():
        if vb: out.inf("executing", func)
        exec(func)
        if vb: out.inf("completed", func)
    else: out.err(1)
