import math

from call import State


class Elevator:
    def __init__(self, building, id, speed, close, open, start, stop) -> None:
        self.id = id
        self.speed = speed
        self.open = open
        self.close = close
        self.start = start
        self.stop = stop
        self.pos = 0
        self.calls = []
        self.state = 0  # up = 1, level = 0 , down = -1

    def goto(self, floor):
        time_to_floor = 0
        if self.pos != floor:
            time_to_floor = self.open + self.start + (math.abs((self.pos - floor)) / self.speed) + self.stop + self.open

        self.pos = floor

    def sim(self, call):
        if call is not None:
            call.alloc(self)
        tmp_calls = self.calls.copy()
        if len(self.calls) == 0:
            return 0
        last_call = self.calls[-1]
        active_calls = []
        done_calls = []
        dest = 0
        last_active_call = 0
        for i in range(0, math.ceil(float(last_call.time)) + 120):
            if len(active_calls) != len(tmp_calls) and math.ceil(float(tmp_calls[last_active_call].time)) <= i:
                active_calls.append(tmp_calls[last_active_call])
                last_active_call += 1

            # changed a little was comparing dest which is 0 (line 34)
            for j in active_calls:
                if self.state == 1:
                    if j.state == State.GOING2SRC and self.pos <= j.src < j.dest:
                        dest = j.src
                    elif j.state == State.GOING2DEST and self.pos <= j.src < j.dest:
                        dest = j.src
                elif self.state == -1:
                    if j.state == State.GOING2SRC and j.dest <= j.src < self.pos:
                        dest = j.src
                    elif j.state == State.GOING2DEST and j.dest <= j.src < self.pos:
                        dest = j.src

            if self.pos == dest:
                for j in active_calls:
                    if j.state == State.GOING2SRC and j.src == dest:
                        j.state = State.GOING2DEST
                    if j.state == State.GOING2DEST and j.dest == dest:
                        j.state = State.DONE
                        done_calls.append(j)
                        active_calls.remove(j)

            if self.state == 1:
                self.pos += 1
            if self.state == -1:
                self.pos -= 1
            pass

        call.de_alloc(self)
        return 0

    def add_call(self, c):
        self.calls.append(c)

    def remove_call(self, c):
        self.calls.remove(c)
