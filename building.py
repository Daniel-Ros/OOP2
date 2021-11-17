class Building(object):
    def __init__(self, min_floor, max_floor) -> None:
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elev = []

    def set_active_minmax(self, tmin, tmax):
        self.min_floor = tmin
        self.max_floor = tmax

    def add_elevator(self, elev) -> None:
        self.elev.append(elev)

    def num_elev(self):
        return len(self.elev) - 1
