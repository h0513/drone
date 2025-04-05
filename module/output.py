pctxt: str = "\033[95m"
rctxt: str = "\033[91m"
gctxt: str = "\033[92m"
bctxt: str = "\033[94m"
retxt: str = "\033[0m"
oftxt: str = pctxt + "[output]" + retxt
eftxt: str = rctxt + "[error]" + retxt
sftxt: str = gctxt + "[success]" + retxt
iftxt: str = bctxt + "[info]" + retxt
nftxt: str = retxt + "[normal]" + retxt
 
errc: list[str] = [
    "g-0 special error",
    "g-1 connection to drone failed [func: ckcon()]",
    "b-2 drone battery level less than 10 [func: pref()]",
    "b-3 drone battery level less than 20 [func: pref()]",
    "pf-4 drone startup failed [func: start()]",
    "g-5 connection to drone userapi failed [func: connect()]",
    "g-6 pcon not defined [func: ckcon()]",
    "c-7 qrcode alignment failed [func: qra()]",
    "c-8 qrcode recognition failed [func: qrr()]",
    "c-9 qrcode tracking failed [func: qrt()]"
]
 
def out(info: str):
    print(oftxt, info)
 
def err(code: int, info="auto"):
    if info == "auto":
        print(eftxt, errc[code])
    else:
        print(eftxt, "SC-" + str(code) + ":", info)
 
def suc(info: str):
    print(sftxt, info)
 
def inf(info: str):
    print(iftxt, info)
 
def nor(info: str):
    print(nftxt, info)
