import math
from enum import Enum


class State(Enum):
    INIT = 0
    GOING2SRC = 1
    GOING2DEST = 2
    DONE = 3


class Call:
    def __init__(self, src, dest, time):
        self.src = int(src)
        self.dest = int(dest)
        self.time = math.ceil(float(time))
        self.elev = -1
        self.state = State.INIT

    def alloc(self, elev):
        self.elev = elev
        self.state = State.GOING2SRC
        self.elev.add_call(self)

    def de_alloc(self, elev):
        self.elev.remove_call(self)
        self.elev = -1
        self.state = State.INIT

    def pickup(self):
        self.state = State.GOING2DEST

    def drop_off(self):
        self.state = State.DONE

    def __repr__(self):
        return "Elevator call,{},{},{},0,{}\n".format(self.time, self.src, self.dest, self.elev.id)

    def __str__(self):
        return "Elevator call,{},{},{},0,{}\n".format(self.time, self.src, self.dest, self.elev.id)
