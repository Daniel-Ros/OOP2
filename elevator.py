import math


class Elevator:
    def __init__(self, building, id, speed, close, open, start, stop) -> None:
        self.id = id
        self.speed = speed
        self.open = open
        self.close = close
        self.start = start
        self.stop = stop
        self.pos = 0

    def goto(self, floor):
        time_to_floor = 0
        if self.pos != floor:
            time_to_floor = self.open + self.start + (math.abs((self.pos - floor)) / self.speed) + self.stop + self.open

        self.pos = floor
