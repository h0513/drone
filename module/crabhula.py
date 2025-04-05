from collections import namedtuple
from types import UnionType
from typing import Optional, TypedDict, Literal, TypeAlias, Dict
import pyhula as hula

from typing import TypedDict, Literal, TypeAlias, Union

class Led(TypedDict):
    r: int
    b: int
    g: int
    mode: Literal[1, 2, 4, 16, 32]

LedT: TypeAlias = Union[Led, Literal[0]]

class userAPI:
    """
    A class representing a programmable drone with various capabilities like flying,
    camera usage, LED control, and interaction with tags and QR codes.
    """
    api: hula.userAPI

    def __init__(self):
        self.api = hula.UserApi()

    def connect(self, server_ip: Optional[str] = None):
        '''
        connects to the drone
        '''
        return self.api.connect(server_ip)
    def single_fly_takeoff(self, led: LedT = 0):
        '''
        drone takes off
        '''
        return self.api.single_fly_takeoff(led)
    def single_fly_touchdown(self, led: LedT = 0):
        '''
        drone lands
        '''
        return self.api.single_fly_touchdown(led)
    def single_fly_left(self, distance: int, led: LedT = 0):
        '''
        flies in left direction
        '''
        return self.api.single_fly_left(distance, led)
    def single_fly_forward(self, distance: int, led: LedT = 0):
        '''
        flies in forward direction
        '''
        return self.api.single_fly_forward(distance, led)
    def single_fly_right(self, distance: int, led: LedT = 0):
        '''
        flies in right direction
        '''
        return self.api.single_fly_right(distance, led)
    def single_fly_back(self, distance: int, led: LedT = 0):
        '''
        flies in back direction
        '''
        return self.api.single_fly_back(distance, led)
    def single_fly_up(self, height: int, led: LedT = 0):
        '''
        flies in up direction
        '''
        return self.api.single_fly_up(height, led)
    def single_fly_down(self, height: int, led: LedT = 0):
        '''
        flies in down direction
        '''
        return self.api.single_fly_down(height, led)
    def single_fly__turnleft(self, angle: int, led: LedT = 0):
        '''
        turns left
        '''
        return self.api.single_fly_turnleft(angle, led)
    def single_fly__turnright(self, angle: int, led: LedT = 0):
        '''
        turns right
        '''
        return self.api.single_fly_turnright(angle, led)
    def single_fly__bounce(self, bounces: int, height: int, led: LedT = 0):
        '''
        bounces, quite anticlimatic
        '''
        return self.api.single_fly_turnright(bounces, height, led)
    def single_fly_straight_flight(self, x: int, y: int, z: int, led: LedT = 0):
        '''
        flies to that cartision coordinate
        '''
        return self.api.single_fly_straight_flight(x, y, z, led)
    def single_fly_radius_around(self, radius: int, led: LedT = 0):
        '''
        flies around a set point
        '''
        return self.api.single_fly_radius_around(radius, led)
    def single_fly_autogyration360(self, num, led: LedT = 0):
        '''
        rotates the drone 360 degress counterclockwise for num times
        '''
        return self.api.single_fly_autogyration360(num, led)
    def single_fly_somersault(self, direction: Literal[0, 1, 2, 3], led: LedT = 0):
        '''
        flips
        '''
        return self.api.single_fly_somorsault(direction, led)
    def single_fly_curvilinearFlight(self, x:int, y: int, z: int, direction: bool = True, led: LedT = 0):
        '''
        what the fish is this
        '''
        return self.api.single_fly_curvilinearFlight(direction, x, y, z, led)
    def single_fly_hover_flight(self, time: int, led: LedT = 0):
        '''
        hover at a point for a time; use instead of time.sleep
        '''
        return self.api.single_fly_hover_flight(time, led)
    def single_fly_barrier_aircraft(self, mode: bool):
        '''
        enable/disable obstacle avoidance
        '''
        return self.api.single_fly_barrier_aircraft(mode)
    def line_walking(self, fun_id: Literal[1], dist: int, way_color: int):
        '''
        fun id 0 following lines, ignoring detection
        '''
        return self.api.single_fly_Line_walking(fun_id, dist, way_color)
    def AiIdentifies(self, mode: int):
        '''
        recognises various signs
        TODO
        '''
        return self.api.single_flyAiIdentifies(mode)
    def Qrcode_align(self, mode: int, qr_id: int):
        '''
        alings to the qr code
        TODO test
        '''
        return self.api.single_fly_Qrcode_align(mode, qr_id)
    def Qrcode_recognition(self, mode: int, qr_id: int) -> Dict[str, Union[str, bool]]:
        '''
        returns data about a qr code in frame
        '''
        return self.api.single_fly_recognition_Qrcode(mode, qr_id)












