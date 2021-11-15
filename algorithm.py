from functools import cmp_to_key

from call import MultiCall
from simulator import Simulator


class Algo:

    def __init__(self, b, c):
        self.building = b
        self.calls = c
        self.max_call = (b.max_floor - b.min_floor) / len(b.elev)

    def run(self):
        self.building.elev = sorted(self.building.elev, key=cmp_to_key(lambda item1, item2: item2.speed - item1.speed))
        sim = Simulator()
        self.calls = self.join_calls(self.calls)
        print(len(self.calls))
        for c in self.calls:
            if c.elev != -1:
                continue
            min_time = 2147483647
            min_elev = None
            for e in self.building.elev:
                time_wasted = sim.bid(e, c)
                if time_wasted <= min_time:
                    min_time = time_wasted
                    min_elev = e
            c.alloc(min_elev)

    def join_calls(self, calls):
        sim = Simulator()
        i = 0
        while i < len(calls) - 1:
            if calls[i].dir == calls[i + 1].dir:
                if calls[i + 1].time - calls[i].time >= sim.time_to_finish(self.building.elev[0], calls[i].src,
                                                                           calls[i + 1].src):
                    multi_call = MultiCall([calls[i], calls[i + 1]])
                    calls[i] = multi_call
                    calls.remove(calls[i + 1])
                    i += 1
            i += 1
        return calls
