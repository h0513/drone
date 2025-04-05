purple: str = "\033[95m"
red: str = "\033[91m"
green: str = "\033[92m"
blue: str = "\033[94m"
white: str = "\033[0m"
output: str = purple + "[output]" + white
error: str = red + "[error]" + white
success: str = green + "[success]" + white
info: str = blue + "[info]" + white
normal: str = white + "[normal]" + white

errors = [
    "g-0 special error",
    "g-1 connection to drone failed [func: ckcon()]",
    "b-2 drone battery level less than 10 [func: pref()]",
    "b-3 drone battery level less than 20 [func: pref()]",
    "pf-4 drone startup failed [func: start()]",
    "g-5 connection to drone userapi failed [func: connect()]",
    "g-6 pcon not defined [func: ckcon()]",
    "c-7 qrcode alignment failed [func: qra()]",
    "c-8 qrcode recognition failed [func: qrr()]",
    "c-9 qrcode tracking failed [func: qrt()]",
    "tf-10 model file or label file not found [module: detect] [func: __init__]"
]

def out(info: str):
    print(output, info)

def err(code: int, info="auto"):
    if info == "auto":
        print(error, errors[code])
    else:
        print(f"{error}, c-{code}: {info}")

def suc(info: str):
    print(success, info)

def inf(info: str):
    print(info, info)

def nor(info: str):
    print(normal, info)
