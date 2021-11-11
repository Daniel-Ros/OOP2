class Algo:
    def __init__(self, b, c):
        self.building = b
        self.calls = c

    def run(self):
        for c in self.calls:
            min_time = 2147483647
            min_elev = None
            for e in self.building.elev:
                time_wasted = e.bid(c)
                if time_wasted <= min_time:
                    min_time = time_wasted
                    min_elev = e
            c.alloc(min_elev)
