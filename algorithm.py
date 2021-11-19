from functools import cmp_to_key

from simulator import Simulator


class Algo:
    def __init__(self, b, c):
        self.building = b
        self.calls = c
        self.max_call = (b.max_floor - b.min_floor) / len(b.elev)
    """
    the algorithm is balancing the elevator "work" time
    every elevator has different attributes , every elevator can complete the same call whitish a different time stamp.
    the algo balancing calls between elevators by balancing the time that it takes to every elevator to complete all of
    the calls that assigned to this elevator.
    """

    def run(self):
        self.building.elev = sorted(self.building.elev, key=cmp_to_key(lambda item1, item2: item2.speed - item1.speed))
        sim = Simulator()
        for c in self.calls:
            if c.elev != -1:
                continue
            min_time = 2147483647
            min_elev = None
            bids = []
            for e in self.building.elev:
                time_wasted = sim.bid(e, c)
                bids.append(time_wasted)
                if time_wasted <= min_time:
                    min_time = time_wasted
                    min_elev = e
            c.alloc(min_elev)
