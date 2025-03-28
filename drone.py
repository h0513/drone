    import pyhula as hula
    import output as out
    import keyboard
     
     
     
    pled = {'r': 0, 'g':0, 'b': 0, 'mode': 1}
    rled = {'r': 255, 'g':0, 'b': 0, 'mode': 1}
    gled = {'r': 0, 'g':255, 'b': 0, 'mode': 1}
    bled = {'r': 0, 'g':0, 'b': 255, 'mode': 1}
    ppref = False
     
    def docs():
        docs = """
    \033[1;35m\033[4mfunctions\033[0m
    \033[1m\033[92mstart()\033[0m: start flight \033[94m[completes: connect(), pref()]\033[0m
    \033[1m\033[92mconnect()\033[0m: connects to drone
    \033[1m\033[92mckcon()\033[0m: check connection \033[94m[param: ins]\033[0m
    \033[1m\033[92mpref()\033[0m: preflight check \033[94m[param: ins]\033[0m
     
    \033[1;35m\033[4mmovement functions\033[0m
    \033[1m\033[93mhorizontal plane motion\033[0m: \033[92mm<dir>(distance, vb, led)\033[0m \033[94m[avail: mf(), mb(), ml(), mr()]\033[0m
    \033[1m\033[93mvertical plane motion\033[0m: \033[92mv<dir>(distance, vb, led)\033[0m \033[94m[avail: vt()-takeoff, vl()-land, vh()-hover, vu(), vd()]\033[0m
    \033[1m\033[93mrotational motion\033[0m: \033[92mr<dir>(angle, vb, led)\033[0m \033[94m[avail: rl(), rr()]\033[0m
    \033[1m\033[93mcircular motion\033[0m: \033[92mcf(radius, vb, led)\033[0m
     
    \033[1;35m\033[4mcustom execution\033[0m
    \033[1m\033[92mfly(func, sf=True, vb)\033[0m: execute custom function \033[91m(note: "api." is appended)\033[0m \033[94m[sf: append "single_fly_" to front]\033[0m
     
    \033[1;35m\033[4mfunction parameters\033[0m
    \033[1m\033[93mvb\033[0m: verbose output \033[94m[default: False]\033[0m
    \033[1m\033[93mled\033[0m: lamplight \033[94m[default: pled]\033[0m
    \033[1m\033[93mins\033[0m: insistent checking \033[91m(else default to persistent checking)\033[0m \033[94m[default: True]\033[0m
        """
        print()
        out.inf("Documentation")
        print(docs)
        print()
     
    def start(vb=True):
        print()
        out.inf("new drone session starting")
        if vb: out.inf("starting drone")
        suc = True
        if not connect(): suc = False
        if not pref(): suc = False
        if vb and suc: out.suc("complete drone startup")
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
            if vb: out.suc("preflight check completed [battery: " + str(bat) + "]")
            if suc: return 0
            else: return 1
     
    def mf(distance, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("moving", distance + "cm forwards with led", led)
            api.single_fly_forward(distance, led)
            if vb: out.suc("completed", distance + "cm forwards motion with led", led)
        else: out.err(1)
     
    def mb(distance, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("moving", distance + "cm backwards with led", led)
            api.single_fly_back(distance, led)
            if vb: out.suc("completed", distance + "cm backwards motion with led", led)
        else: out.err(1)
     
    def ml(distance, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("moving", distance + "cm left with led", led)
            api.single_fly_left(distance, led)
            if vb: out.suc("completed", distance + "cm left motion with led", led)
        else: out.err(1)
     
    def mr(distance, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("moving", distance, "right with led", led)
            api.single_fly_right(distance, led)
            if vb: out.suc("completed", distance, "right motion with led", led)
        else: out.err(1)
     
    def vt(vb=False, led=pled):
        if ckcon():
            if vb: out.inf("taking off with led", led)
            api.single_fly_takeoff(led)
            if vb: out.suc("completed takeoff with led", led)
        else: out.err(1)
     
    def vl(vb=False, led=pled):
        if ckcon():
            if vb: out.inf("landing with led", led)
            api.single_fly_touchdown(led)
            if vb: out.suc("completed landing with led", led)
        else: out.err(1)
     
    def vh(time, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("hovering for", time + "s with led", led)
            api.single_fly_hover_flight(time, led)
            if vb: out.suc("hovered for", time + "s with led", led)
        else: out.err(1)
     
    def vu(distance, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("moving" + str(distance) + "cm up with led" + str(led))
            api.single_fly_up(distance, led)
            if vb: out.suc("completed"+ str(distance) + "cm down motion with led"+ str(led))
        else: out.err(1)
     
    def vd(distance, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("moving", distance, "cm down with led", led)
            api.single_fly_down(distance, led)
            if vb: out.suc("completed", distance, "cm down motion with led", led)
        else: out.err(1)
     
    def rl(angle, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("turning", angle, "degree left with led", led)
            api.single_fly_turnleft(angle, led)
            if vb: out.suc("completed", angle, "degree left turn with led", led)
        else: out.err(1)
     
    def rr(angle, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("turning", angle, "degree with led", led)
            api.single_fly_turnright(angle, led)
            if vb: out.suc("completed", angle, "degree left turn with led", led)
        else: out.err(1)
     
    def cf(radius, vb=False, led=pled):
        if ckcon():
            if vb: out.inf("flying", radius + "cm radius cirular path with led", led)
            api.single_fly_radius_around(radius, led)
            if vb: out.suc("completed", radius + "cm radius circular path with led", led)
        else: out.err(1)
     
    def dh(vb=False):
        if ckcon():
            if vb: out.inf("getting drone time-of-flight height")
            h = api.get_plane_distance()
            if vb: out.suc("completed drone time-of-flight height detection [output:", h + "]")
            return h
        else: out.err(1)
     
    def qra(id=0, md=0, vb=False):
        if ckcon():
            if vb: out.inf("aligning to qr " + str(id) + " using mode " + str(md))
            suc = api.single_fly_Qrcode_align(md, id)
            if suc: out.suc("completed alignment to qr " + str(id) + " using mode " + str(md))
            else: out.err(7)
        else: out.err(1)
     
    def qrr(id=0, md=0, vb=False):
        if ckcon():
            if vb: out.inf("recognising qr " + id, "using mode", md)
            suc = api.single_fly_recognition_Qrcode(md, id)
            if suc[0]: out.suc("completed recognition of qr", id, "using mode", md)
            else: out.err(8)
            return suc
        else: out.err(1)
     
    def qrc(id, t):
        qra(id, 0, True)
        #qrt(t, id, 0, True)
        api.single_fly_lamplight(255, 255, 255, 2, 1)
     
    def qrt(t, id=0, md=0, vb=False):
        if ckcon():
            if vb: out.inf("tracking qr " + str(id) + " for " + str(t) + "s")
            suc = api.single_fly_track_Qrcode(id, t)
            if suc: out.suc("completed tracking of qr " + str(id) + " for " + str(t) + "s")
            else: out.err(9)
        else: out.err(1)
     
    def fly(func, sf=True, vb=False):
        if sf: func = "single_fly_" + func
        func = "api." + func
        if ckcon():
            if vb: out.inf("executing", func)
            exec(func)
            if vb: out.inf("completed", function)
        else: out.err(1)
