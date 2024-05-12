# Custom Logger

from enum import Enum


class LogLevel(Enum):
    NOTSET = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

class CLogger():
    def __init__(self) -> None:
        pass

    def log(self, message: str, level: LogLevel):
        if level == LogLevel.ERROR:
            print("ERROR:", message)
        else: 
            print("GENEL|" + level.name, message) # devamını yapmaya uşendim