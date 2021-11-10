from functools import cmp_to_key


class Algo:
    def __init__(self, b, c):
        self.building = b
        self.calls = c

    def run(self):
        sorted(self.building.elev, key=cmp_to_key(lambda item1, item2: item1.speed - item2.speed))  # sort the elevators
        for c in self.calls:
            for e in self.building.elev:
                time_wasted = e.sim(c) - e.sim(None)
