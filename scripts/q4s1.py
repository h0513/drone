import pyhula as ph
import time
api =  ph.UserApi()
if not api.connect():
    print("[output] connect fail")
else:
    api.single_fly_takeoff()
    i=0
    while(i<10):
        if api.single_fly_recognition_Qrcode(0,0)["result"]:
            api.single_fly_lamplight(0, 0, 255, 3, 1)
            api.single_fly_touchdown()
        time.sleep(2)
        i+=1
        print(f"[output] finished iteration {i}")
    api.single_fly_touchdown()