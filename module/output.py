    pctxt = "\033[95m"
    rctxt = "\033[91m"
    gctxt = "\033[92m"
    bctxt = "\033[94m"
    retxt = "\033[0m"
    oftxt = pctxt + "[output]" + retxt
    eftxt = rctxt + "[error]" + retxt
    sftxt = gctxt + "[success]" + retxt
    iftxt = bctxt + "[info]" + retxt
    nftxt = retxt + "[normal]" + retxt
     
    errc = [
        "g-0 you did nothing wrong, but heres an error because im borded and why not",
        "g-1 connection to drone failed [func: ckcon()]",
        "b-2 drone battery level less than 10 [func: pref()]",
        "b-3 drone battery level less than 20 [func: pref()]",
        "pf-4 drone startup failed [func: start()]",
        "g-5 connection to drone userapi failed [func: connect()]",
        "g-6 pckcon not defined [func: ckcon()]",
        "c-7 qrcode alignment failed [func: qra()]",
        "c-8 qrcode recognition failed [func: qrr()]",
        "c-9 qrcode tracking failed [func: qrt()]"
    ]
     
    def out(info):
        print(oftxt, info)
     
    def err(code, info="auto"):
        if info == "auto":
            print(eftxt, errc[code])
        else:
            print(eftxt, "SC-" + str(code) + ":", info)
     
    def suc(info):
        print(sftxt, info)
     
    def inf(info):
        print(iftxt, info)
     
    def nor(info):
        print(nftxt, info)
