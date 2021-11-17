from enum import Enum


class State(Enum):
    INIT = 0
    GOING2SRC = 1
    GOING2DEST = 2
    DONE = 3


class Direction(Enum):
    UP = 1
    DOWN = 0


class Call:
    def __init__(self, src, dest, time):
        self.src = int(src)
        self.dest = int(dest)
        self.time = float(time)
        self.elev = -1
        self.state = State.INIT
        self.dir = Direction.DOWN if self.src >= self.dest else Direction.UP

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
        if self.elev == -1:
            return "Elevator call,{},{},{},0,-1,{}\n".format(self.time, self.src, self.dest, self.dir)
        return "Elevator call,{},{},{},0,{},{}\n".format(self.time, self.src, self.dest, self.elev.id, self.dir)
