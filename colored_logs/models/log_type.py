from enum import Enum

class LogType(Enum):
    Info = 0
    Success = 1
    Fail = 2
    Error = 3
    Subtle = 4
    Process = 5