from enum import Enum


class ViolationType(Enum):
    TAB_SWITCH = "TabSwitch"
    TIME_EXCEEDED = "TimeExceeded"
    CAMERA_OFF = "CameraOff"
