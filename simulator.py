from call import MultiCall, Direction
from elevator import Elevator


class Simulator:
    def bid(self, e, call):
        time = 0
        pos = 0
        for c in e.calls:
            if isinstance(c, MultiCall):
                for cc in self.get_multi_sorted(c):
                    time += self.time_to_finish(e, pos, cc.src) + self.time_to_finish(e, cc.src, cc.dest)
                    pos = cc.dest
            else:
                time += self.time_to_finish(e, pos, c.src) + self.time_to_finish(e, c.src, c.dest)
                pos = c.dest
        if call is not None:
            time += self.time_to_finish(e, pos, call.src) + self.time_to_finish(e, call.src, call.dest)
        return time

    def get_multi_sorted(self, mc):
        ret = []
        for c in mc:
            ret.append(c.src)
            ret.append(c.dest)

        sorted(c, reverse=True if mc[0].dir == Direction.DOWN else False)

    def time_to_finish(self, e, src, dest):
        return e.close + e.start + (abs(dest - src) / e.speed) + e.stop + e.open

    def join_calls(self, calls):
        i = 0
        while i < len(calls) - 1:
            if calls[i].dir == calls[i + 1].dir:
                if abs(calls[i].time - calls[i + 1].time) > self.time_to_finish(Elevator.fastest_elev, calls[i].src,
                                                                                calls[i + 1].src):
                    multi_call = MultiCall([calls[i], calls[i + 1]])
                    calls[i] = multi_call
                    calls.remove(calls[i + 1])
                    i += 1
            i += 1
        return calls

    def can_pickup(self, e, c):
        last_call = e.calls[-1]
        if c.dir == last_call.dir:
            if last_call.time - c.time >= self.time_to_finish(Elevator.fastest_elev, c.src,
                                                              last_call.src):
                if c.dir == Direction.UP:
                    if c.src <= last_call.src:
                        return True
                if c.dir == Direction.DOWN:
                    if c.src >= last_call.src:
                        return True
            return False
