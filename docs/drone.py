# variables
vb # verbose output
ins # insistent checking
led # lamp light
ds # distance
t # time
an # angle
r # radius
id # qrcode id
md # mode
pset # preset
r, g, b # red, green, blue

# aux functions
start(vb=True) # connect to drone and preflight check
connect(vb=True) # connect to drone
ckcon(ins=False, vb=False) # check connection to drone 
pref(ins=True, vb=True) # preflight check 

# horizontal motion
mf(ds=0, vb=False, led=led[0]) # move forwards 
mb(ds=0, vb=False, led=led[0]) # move backwards 
ml(ds=0, vb=False, led=led[0]) # move left 
mr(ds=0, vb=False, led=led[0]) # move right 

# vertical motion
vt(vb=False, led=led[0]) # vertical takeoff
vl(vb=False, led=led[0]) # vertical landing
vh(t=0, vb=False, led=led[0]) # vertical hover
vu(ds=0, vb=False, led=led[0]) # vertical up
vd(ds=0, vb=False, led=led[0]) # vertical down

# rotational motion
rl(an=0, vb=False, led=led[0]) # rotate left
rr(an=0, vb=False, led=led[0]) # rotate right

# circular motion
cf(r=0, vb=False, led=led[0]) # circular flight

# sensors
dh(vb=False) # drone height

# qrcode
qra(id=0, md=0, vb=False) # qrcode alignment
qrr(id=0, md=0, vb=False) # qrcode recognition
qrt(t=0, id=0, md=0, vb=False) # qrcode tracking

# lights
ll(pset=0, t=0, r=0, g=0, b=0, md=1, vb=False) # lamp light

# custon execution
fly(func, sf=True, vb=False)
