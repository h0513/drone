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
    if not connect(vb): suc = False
    if not pref(True, vb): suc = False
    if vb and suc: out.suc("completed drone startup")
    if vb and not suc: out.err(3)
    keyboard.add_hotkey("ctrl+space", lambda: vl())
    return 0

def connect(vb=True):
    if vb: out.inf("initiating connection to drone")
    global api
    api = hula.UserApi()
    ckcon(True, True)
    if ckcon():
        if vb: out.suc("completed drone connection")
        return 1
    else: return 0

def ckcon(ins=False, vb=False):
    if not "api" in globals():
        if vb: out.err(5)
        connect()
    if not "pcon" in globals():
        if vb: out.err(6)
        global pcon
        pcon = False
        if vb: out.suc("completed pcon variable global definition")
    if pcon == True and not ins:
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
    if not ins and ppref:
        if vb: out.suc("completed preflight check using ppref")
        return 0
    else:
        bat = api.get_battery()
        suc = False
        if (bat < 10): out.err(2)
        elif (bat < 20): out.err(3)
        else: suc = True
        if vb: out.suc(f"preflight check completed [battery: {bat}]")
        if suc: return 1
        else: return 0

def mf(ds=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm forwards with led {led}")
        api.single_fly_forward(ds, led)
        if vb: out.suc(f"completed {ds}cm forwards motion with led {led}")

def mb(ds=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm backwards with led {led}")
        api.single_fly_back(ds, led)
        if vb: out.suc(f"completed {ds}cm backwards motion with led {led}")

def ml(ds=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm left with led {led}")
        api.single_fly_left(ds, led)
        if vb: out.suc(f"completed {ds}cm left motion with led {led}")

def mr(ds=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm right with led {led}")
        api.single_fly_right(ds, led)
        if vb: out.suc(f"completed {ds}cm right motion with led {led}")

def vt(vb=False, led=led[2]):
    if ckcon():
        if vb: out.inf(f"taking off with led {led}")
        api.single_fly_takeoff(led)
        if vb: out.suc(f"completed takeoff with led {led}")

def vl(vb=False, led=led[2]):
    if ckcon():
        if vb: out.inf(f"landing with led {led}")
        api.single_fly_touchdown(led)
        if vb: out.suc(f"completed landing with led {led}")

def vh(t=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"hovering for {t}s with led {led}")
        api.single_fly_hover_flight(t, led)
        if vb: out.suc(f"hovered for {t}s with led {led}")

def vu(ds=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm up with led {led}")
        api.single_fly_up(ds, led)
        if vb: out.suc(f"completed {ds}cm up motion with led {led}")

def vd(ds=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"moving {ds}cm down with led {led}")
        api.single_fly_down(ds, led)
        if vb: out.suc(f"completed {ds}cm down motion with led {led}")

def rl(an=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"turning {an} degree left with led {led}")
        api.single_fly_turnleft(an, led)
        if vb: out.suc(f"completed {an} degree left turn with led {led}")

def rr(an=0, vb=False, led=led[0]):
    if ckcon():
        if vb: out.inf(f"turning {an} degree right with led {led}")
        api.single_fly_turnright(an, led)
        if vb: out.suc(f"completed {an} degree right turn with led {led}")

def cf(r=0, vb=False, led=led[0]):
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

def ll(pset=0, t=0, r=0, g=0, b=0, md=1, vb=False):
    if ckcon():
        if not pset == -1:
            if vb: out.inf(f"setting led color to {led[pset]} for {t}s")
            suc = api.single_fly_lamplight(led[pset]["r"], led[pset]["g"], led[pset]["b"], t, md)
            if suc: out.suc(f"completed setting led color to {led[pset]} for {t}s")
            else: out.err(10)
        else:
            if vb: out.inf(f"setting led color to r: {r}, g: {g}, b: {b} for {t}s")
            suc = api.single_fly_lamplight(r, g, b, t, md)
            if suc: out.suc(f"completed setting led color to r: {r}, g: {g}, b: {b} for {t}s")
            else: out.err(10)

def fly(func, sf=True, vb=False):
    if sf: func = "single_fly_" + func
    func = "api." + func
    if ckcon():
        if vb: out.inf("executing", func)
        exec(func)
        if vb: out.inf("completed", func)
